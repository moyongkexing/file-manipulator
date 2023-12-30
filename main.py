import sys
args = sys.argv

command = args[1]
inputpath = args[2]
outputpath = args[3]
originalContents = ''

if command == 'reverse':
  inputpath = args[2]
  outputpath = args[3]
  with open(inputpath) as f:
    originalContents = f.read()
  with open(outputpath, 'w') as f:
    f.write(originalContents[::-1])

if command == 'copy':
  with open(inputpath) as f:
    originalContents = f.read()
  with open(outputpath, 'w') as f:
    f.write(originalContents)

if command == 'duplicate-contents':
  duplicateCount = args[4]
  with open(inputpath) as f:
    originalContents = f.read()
  with open(outputpath, 'w') as f:
    for i in range(int(duplicateCount)):
      f.write(originalContents)

if command == 'replace-string':
  searchString = args[4]
  newString = args[5]

  with open(inputpath) as f:
    originalContents = f.read()
  with open(outputpath, 'w') as f:
    f.write(originalContents.replace(searchString, newString))