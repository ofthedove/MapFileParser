
f = ''

with open('inputMap.txt') as inFile:
    for line in inFile:
        f += str(line)

data = []

while(True):

    while not f.startswith('.text.'):
        f = f[1:]
        if(len(f) == 0):
            break
    
    if(len(f) == 0):
        break

    f = f[len('.text.'):]

    symbol = ''
    while not f.startswith((' ', '\t', '\n', '\r')):
        symbol += f[0]
        f = f[1:]

    while f.startswith((' ', '\t', '\n', '\r')):
        f = f[1:]

    location = ''
    while not f.startswith((' ', '\t', '\n', '\r')):
        location += f[0]
        f = f[1:]

    while f.startswith((' ', '\t', '\n', '\r')):
        f = f[1:]

    size = ''
    while not f.startswith((' ', '\t', '\n', '\r')):
        size += f[0]
        f = f[1:]

    while f.startswith((' ', '\t', '\n', '\r')):
        f = f[1:]

    path = ''
    while not f.startswith((' ', '\t', '\n', '\r')):
        path += f[0]
        f = f[1:]

    while f.startswith((' ', '\t', '\n', '\r')):
        f = f[1:]

    data.append({'symbol':symbol, 'location':location, 'size':size, 'path':path})

# print(data)

with open('outputMap.csv', "w") as outFile:
    for datum in data:
        outFile.write("{}\t{}\t{}\t{}\n".format(datum['symbol'], datum['location'], datum['size'], datum['path']))

summaryData = []
path = data[0]['path']
size = 0
for item in data:
    if item['path'] == path:
        size += int(item['size'], 0)
    else:
        summaryData.append({'size':size, 'path':path, 'file':path[path.find('('):][1:-1]})
        path = item['path']
        size = int(item['size'], 0)

summaryData.append({'size':size, 'path':path, 'file':path[path.find('('):][1:-1]})

with open('outputSummary.csv', "w") as outFile:
    for item in summaryData:
        outFile.write("{}\t{}\t{}\n".format(item['size'], item['path'], item['file']))
