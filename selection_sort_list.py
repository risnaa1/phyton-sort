#Latihan 4

def selection_sort(angka) :
    n = len(angka)
    for i in range(n) :
        min_index = i
        for j in range (i+1, n) :
            if angka[j] < angka[min_index] :
                min_index = j
        angka[i], angka[min_index] = angka[min_index], angka[i]

AngkaAndi = [9, 5, 3, 8, 2]
selection_sort(AngkaAndi)
print("Daftar angka Andi yang sudah diurutkan yaitu : ", AngkaAndi)