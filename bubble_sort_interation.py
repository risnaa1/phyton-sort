#Percobaan 7
#Menghitung jumlah iterasi

def bubble_sort(arr) :
    n = len(arr)
    count = 0
    for i in range(n-1) :
        for j in range(n-i-1) :
            count += 1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count 

arr = [64, 34, 25, 12, 22, 11, 90]
interations = bubble_sort(arr)
print ("Hasil pengurutan : ", arr)
print ("Jumlah iterasi : ", interations)