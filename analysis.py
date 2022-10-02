#Venuja Perera
#01/10/2022
#A module with functions capable of reading a file and analysing its contents

#Helper Functions
def addCompliment(prev, curr):
    if curr not in results:
        results[curr] = {'maxComp':[0,[]], 'frequency':1}
    
    elif curr in results:
        results[curr]['frequency']+=1
    
    if prev != None:
        if curr not  in results[prev]:
            results[prev][curr] = 1
        elif curr in results[prev]:
            results[prev][curr]+=1

        if results[prev][curr]>results[prev]['maxComp'][0]:
            results[prev]['maxComp'][0] = results[prev][curr]
            results[prev]['maxComp'][1] = [curr]
        elif results[prev][curr] == results[prev]['maxComp'][0]:
            results[prev]['maxComp'][1].append(curr)

#Global Variables
results = {}

#Functions
def load(str):
    results.clear()
    results['totalCount'] = 0
    file = open(str)
    fileData = file.read()
    prevWord = None
    currWord=''
    for i in range (len(fileData)):
        if (fileData[i] == ' '):
            results['totalCount']+=1
            addCompliment(prevWord,currWord)
            prevWord=currWord
            currWord = ''
            continue
        currWord+=fileData[i]#Add the current element to the current string
        if (i == len(fileData)-1):#If its the last element in the file
            results['totalCount']+=1
            addCompliment(prevWord,currWord)
    file.close()
    
def countall():
    return results['totalCount']

def countunique():
    return len(results)-1

def commonword(list):
    if len(list) == 0:
        return None

    resArray=[0,[None]]
    for x in list:
        if x not in results:
            continue
        elif results[x]['frequency'] > resArray[0]:
            resArray[0] = results[x]['frequency']
            resArray[1] = [x]
        elif results[x]['frequency'] == resArray[0]:
            resArray[1].append(x)
    return resArray

def commonpair(str):
    if str not in results:
        return None
    return results[str]['maxComp']
    