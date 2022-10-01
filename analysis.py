
from lib2to3.pytree import _Results
from unittest import result


results = {}

def addCompliment(prev, curr):
    if curr not in results:
        results[curr] = {'maxComp':[0,''], 'frequency':1}
    
    elif curr in results:
        results[curr]['frequency']+=1
    
    if prev != None:
        if curr not  in results[prev]:
            results[prev][curr] = 1
        elif curr in results[prev]:
            results[prev][curr]+=1

        if results[prev][curr]>results[prev]['maxComp'][0]:
            results[prev]['maxComp'][0] = results[prev][curr]
            results[prev]['maxComp'][1] = curr



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
            print(currWord)
            currWord = ''
            continue
        currWord+=fileData[i]#Add the current element to the current string
        if (i == len(fileData)-1):#If its the last element in the file
            results['totalCount']+=1
            print(currWord)
    
load('testfile1.txt')
print(results['totalCount'])



