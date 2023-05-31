#Latihan 5

def selection_sort_pemain(pemain) :
    n = len(pemain)
    for i in range(n) :
        max_index = i
        for j in range (i+1, n) :
            if pemain[j][2] > pemain[max_index][2] :
                max_index = j
        pemain[i], pemain[max_index] = pemain[max_index], pemain[i]

pemain = [
    ["Kylian Mbappe", "Paris Saint Germain", 40],
    ["Victor Osimhen", "Napoli", 28],
    ["Robert Lewandownskin", "Barcelona", 33],
    ["Erling Haaland", "Manchester City", 52],
    ["Christopher Nkunku", "RB Leipzing", 22]
]

selection_sort_pemain(pemain)
print("Daftar pemain sepak bola yang sudah diurutkan : ")
for pemain in pemain :
    print(f"Nama Pemain : {pemain[0]}")
    print(f"Klub        : {pemain[1]}")
    print(f"Jumlah Gol  : {pemain[2]}")