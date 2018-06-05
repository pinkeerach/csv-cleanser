

def attemptToParseFile():
    import csv, sys
    filename = 'sample-with-broken-utf8.csv'
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        try:
            for row in reader:
                print(row)
        except UnicodeDecodeError as ue: 
            # bad stuff happened
            sys.exit('bad unicode character at position {}'.format(ue.start))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

attemptToParseFile()