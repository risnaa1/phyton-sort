#Percobaan 9
#Mengurutkan daftar string secara ascending

def selection_sort(arr) :
    n = len(arr)
    for i in range(n-1) :
        min_index = i
        for j in range(i+1, n) :
            if arr[j] < arr[min_index] :
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = ["z", "b", "a", "f", "c"]
selection_sort(arr)
print("Hasil pengurutan : ", arr)
