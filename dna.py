import sys, csv, re
with open(sys.argv[2]) as sequence_file:
    sequence = open(sys.argv[2]).read()
with open(sys.argv[1]) as database_file:
    database_read = csv.DictReader(database_file, delimiter=',')
    database = [{name: (int(entry[name]) if entry[name].isnumeric() else entry[name]) for name in entry} for entry in database_read]
    results = {strs: len(max(re.findall(r'((?:' + strs + ')+)', sequence) + ['']))//len(strs) for strs in database_read.fieldnames if strs != 'name'}
print(([person['name'] for person in database if list(results.values()) == list(person.values())[1:]] + ["No match"])[0])
