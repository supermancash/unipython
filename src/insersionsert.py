import random


def insertionSort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
        print("=================== list iteration no. " + str(i) + " ==================")
        print("\t" + str(liste))
        print("===========================================================\n")
    return liste


randomlist = []
for i in range(0, 10):
    n = random.randint(1, 1000)
    randomlist.append(n)
print("====================== unsorted list ======================")
print("\t" + str(randomlist))
print("===========================================================\n")

insertionSort(randomlist)
