#!/usr/bin/env python

def formatData(fieldData, columnIndex):
    # header guide: Timestamp,Address,ZIP,FullName,FooDuration,BarDuration,TotalDuration,Notes
    import datetime

    stringToReturn = fieldData #default, do nothing

    if columnIndex == 0:
        #format timestamp: ISO-8601 format, convert Pacific -> Eastern
        datetimeFromField = datetime.datetime.strptime(stringToReturn, '%m/%d/%y %I:%M:%S %p')
        stringToReturn = datetimeFromField.strftime('%Y-%m-%d %H:%M:%S')

    elif columnIndex == 2:
        #format zip; 5 chars, less than 5 digits, assume 0 as the prefix
        while (len(stringToReturn) < 5):
            stringToReturn = '0' + stringToReturn
            
    elif columnIndex == 3:
        #format fullname: uppercase, nonenglish
        stringToReturn = stringToReturn.upper()

    elif columnIndex == 4 or columnIndex == 5: 
        #format duration; HH:MM:SS.MS format (where MS is milliseconds); please convert them to a floating point seconds format
        try:
            timeObject = datetime.datetime.strptime(stringToReturn, '%I:%M:%S.%f')
            stringToReturn = timeObject.timestamp() * 1000
        except ValueError:
            stringToReturn = 0

    print(stringToReturn)
    return(stringToReturn)

def manuallyParseCsv(filename):
    
    with open(filename, 'rb') as csvFile: # read as binary to check for encoding
        header = csvFile.readline()        
        try: 
            headerString = header.decode()
            columns = headerString.split(',')
            # 0 Timestamp, 1 Address, 2 ZIP, 3 FullName, 4 FooDuration, 5 BarDuration, 6 TotalDuration, 7 Notes
        except UnicodeDecodeError:
            return '''if we can't get a header, the rest of this approach falls apart.'''

        if len(columns) != 8:
            return # unexpected number of columns

        for line in csvFile:
            import re
            regExPattern = '''(?:^|,)("(?:[^"]+|"")*"|[^,]*)'''
            decodedLine = str(line, 'utf-8', 'replace')
            splitDecodedLine = re.compile(regExPattern).split(decodedLine)

            # a bit of a hack because my regex is rusty and i'm a python newb
            decodedFields = []
            for item in splitDecodedLine:
                if item != '':
                    decodedFields.append(item)

            fieldCounter = 0
            fieldList = []
            totalDuration = 0

            for field in decodedFields:    # apply formatting logic
                # print(field) 
                if fieldCounter != 6:
                    formattedField = formatData(field, fieldCounter)
                else:
                    formattedField = totalDuration
                
                #  - add foo + bar durations = totalduration
                if fieldCounter == 4:
                    totalDuration = formattedField
                elif fieldCounter == 5:
                    totalDuration += formattedField

                fieldCounter += 1
                fieldList.append(formattedField)
        
        # TODO build the new CSV file here

def parseCsvFile():
    # filename = 'sample-with-broken-utf8.csv'
    filename = 'sample.csv'
    with open(filename, 'r') as csvFile:
        try: # TODO refactor out to use the csv library and make that method throw an exception
            header = csvFile.readline()
            next(csvFile)
            for line in csvFile:
                print(line) # TODO - add the formatting!
            print(header)
        except UnicodeDecodeError:
            manuallyParseCsv(filename)

parseCsvFile()