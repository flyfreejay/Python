moreDatasets = True

def IsChords(a, b):
    if a == (b*2) or b == (a*2):
        return True
    else:
        return False

def SeperateIntoLists(x):
    l = x.split()
    l = [int(i) for i in str(x)]
    return l


# while moreDatasets:
#     numOfKeys = input()
#     if numOfKeys == "":
#         break
#         moreDatasets = False
#     numOfKeys = int(numOfKeys)
#     # get the frequencies
#     frequencies = input()
#     # seperate the frequencies into a list
#     frequencies = SeperateIntoLists(frequencies)
#     #now iterate through every item in the list to find a matching chords
#     for n in range(numOfKeys):

SeperateIntoLists('1 3 4 5 2 3')
