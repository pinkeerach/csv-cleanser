

def parseFileWithCsvLibrary():
    import csv, sys
    filename = 'sample-with-broken-utf8.csv'
    # filename = 'sample.csv'
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f,strict='false')
        try:
            for row in reader:
                record = (x.encode('utf-8', errors='ignore').decode() for x in row)
                yield record
        except UnicodeDecodeError as ue: 
            # bad stuff happened
            sys.exit('bad unicode character at position {}'.format(ue.start))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

# def handleBadEncoding():
#     import 

generator = parseFileWithCsvLibrary()

for i in generator:
    print(i)
