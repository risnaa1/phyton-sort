def bubble_sort_buku (buku) :
    n = len(buku)
    for i in range (n-1) :
        for j in range (n-i-1) :
            if buku[j][2] > buku[j+1][2]:
                buku[j], buku[j+1] = buku[j+1], buku[j]
        
buku = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    ["To Kill a Mockingbird", "Harper Lee", 281],
    ["The Great Gatsby", "F Scott Fitzgerald", 180],
    ["Pride and Prejudice", "Jane Austen", 432],
    ["1984", "George Orwell", 328]
]

bubble_sort_buku(buku)

for buku in buku :
    print (f"Judul          : {buku[0]}")
    print (f"Penulis        : {buku[1]}")
    print (f"Jumlah Halaman : {buku[2]}")
