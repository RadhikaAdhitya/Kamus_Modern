meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROLF":"Tanggapan terhadap lelucon",
            "SHEESH":"Sedikit ketidaksetujuan"
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print('Makna dari',word,'adalah',meme_dict[word])
else:
    print('Kata itu tidak ditemukan')
