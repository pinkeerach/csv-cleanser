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


def handleUnicodeError(error, filename):
    print(error.reason)

    with open(filename, 'rb') as file:
        header = file.readline()
        next(file)

        for line in file:
            # print(line)
            try: # TODO replace the characters!
                myString = line.decode(encoding='utf-8', errors='replace')
                print(myString)
            except UnicodeDecodeError as ue:
                print('==== failure! ===== In Decoding at position {}'.format(ue.start))

        print(header)            

def parseCsvFile():
    filename = 'sample-with-broken-utf8.csv'
    # filename = 'sample.csv'
    with open(filename, 'r') as file:
        try: # TODO refactor out to use the csv library and make that method throw an exception
            header = file.readline()
            next(file)
            for line in file:
                print(line)
            print(header)
        except UnicodeDecodeError as ue:
            handleUnicodeError(ue, filename)

parseCsvFile()