#!/usr/bin/env python

def parseFileWithCsvLibrary():
    import csv, sys
    filename = 'sample-with-broken-utf8.csv'
    # filename = 'sample.csv'
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f,strict='false')
        try: # TODO refactor this back to basic happy path parsing
            for row in reader:
                record = (x.encode('utf-8', errors='ignore').decode() for x in row)
                yield record
        except UnicodeDecodeError as ue: # TODO raise the exception
            # bad stuff happened
            sys.exit('bad unicode character at position {}'.format(ue.start))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

def formatData(fieldData, columnIndex):
    '''Timestamp,Address,ZIP,FullName,FooDuration,BarDuration,TotalDuration,Notes'''

    decodedString = str(fieldData, 'utf-8', 'replace')

    stringToReturn = decodedString

    if columnIndex == 0:
        import datetime
        #format timestamp: ISO-8601 format, convert Pacific -> Eastern
        datetimeFromField = datetime.datetime.strptime(decodedString, '%m/%d/%y %I:%M:%S %p')
        stringToReturn = datetimeFromField.strftime('%Y-%m-%d %H:%M:%S')
    # elif columnIndex == 1 - format address; unicode validation only
    elif columnIndex == 2:
        #format zip; 5 chars, less than 5 digits, assume 0 as the prefix
        while (len(stringToReturn) < 5):
            stringToReturn = '0' + stringToReturn
            
    elif columnIndex == 3:
        #format fullname: uppercase, nonenglish
        stringToReturn = decodedString.upper()
    elif columnIndex == 4 or columnIndex == 5 or columnIndex == 5: 
        #format duration; HH:MM:SS.MS format (where MS is milliseconds); please convert them to a floating point seconds format
        stringToReturn = decodedString

    print(stringToReturn)
    return(stringToReturn)

def manuallyParseCsv(filename):
    
    with open(filename, 'rb') as csvFile: # read as binary to check for encoding
        header = csvFile.readline()
        
        try: #not sure i need this anymore
            headerString = header.decode()
            columns = headerString.split(',')
            '''Timestamp,Address,ZIP,FullName,FooDuration,BarDuration,TotalDuration,Notes'''
        except UnicodeDecodeError:
            return '''if we can't get a header, the rest of this approach falls apart.'''

        next(csvFile)

        for line in csvFile:
            # print(line)
            fieldBytes = line.split(b',')

            fieldCounter = 0
            fieldList = []
            for field in fieldBytes:    # apply formatting logic
                # print(field) 
                formattedField = formatData(field, fieldCounter)
                fieldList.append(formattedField)
                fieldCounter += 1
        
            # print(fieldList)
            # business logic to apply:
            #  - add foo + bar durations = total



def parseCsvFile():
    filename = 'sample-with-broken-utf8.csv'
    # filename = 'sample.csv'
    with open(filename, 'r') as csvFile:
        try: # TODO refactor out to use the csv library and make that method throw an exception
            header = csvFile.readline()
            next(csvFile)
            for line in csvFile:
                print(line)
            print(header)
        except UnicodeDecodeError:
            manuallyParseCsv(filename)

parseCsvFile()