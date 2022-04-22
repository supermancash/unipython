def selectionSort(liste):
    n = len(liste)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if liste[j] < liste[minIndex] :
                minIndex = j
        if minIndex != i :
            temp = liste[minIndex]
            liste[minIndex] = liste[i]
            liste[i] = temp
    return liste


def insertionSort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste

def bubbleSort_ausgabe(liste):
    n = len(liste)
    for i in range( n - 1 ) :
        for j in range(n-i-1) :
            if liste[j] > liste[j + 1] :
                tmp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = tmp
    return liste

def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quickSort(array):
    quick_sort(array, 0, len(array)-1)

def quick_sort(array, start, end):
    if start >= end:
        return
    p = pivot(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def mergeSort(inp_arr):
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        p = 0
        q = 0
        r = 0
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                inp_arr[r] = left_arr[p]
                p += 1
            else:
                inp_arr[r] = right_arr[q]
                q += 1
                r += 1
            while p < left_size:
                inp_arr[r] = left_arr[p]
                p += 1
                r += 1
            while q < right_size:
                inp_arr[r]=right_arr[q]
                q += 1
                r += 1

