## Author: Feras
## Description: Word length comparer that chooses the shortest word first

def shortestString(strList):
    minimum = min(len(i) for i in strList)
    for i in strList:
        if len(i) == minimum:
            return i      
print("The first shortest word is: ", 
    shortestString(["rose", "flower", "nice", "light", "beautiful"]))