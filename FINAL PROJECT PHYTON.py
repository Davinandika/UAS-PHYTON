data_product = {
    1:"laptop",
    2:"Mouse ",
    3:"monitor",
    4:"mousepad",
    5:"charger",
}
daftar_harga = {
    1: 2000000,
    2: 50000,
    3: 60000,
    4: 3000,
    5: 15000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on delivery",
    4:"kartu kredit"
}
print("==========List Product==========")
for i in data_product:
    print("Id Product : ",i,"\t Nama Product :",
          data_product[i],"\t Harga product : ",daftar_harga[i])
pilih_id = int(input("Pilih Id Product : "))
if pilih_id in data_product :
    pilih_beli = input("ingin beli ? (Y/N):")
    if pilih_beli == "y" or pilih_beli=="Y":
        nama_penerima       = input("Nama Penerima      : ")
        alamat_penerima     = input("alamat Penerima    : ")
        telepon             = input("no HP              : ")
        kurir_pengiriman    = input("kurir Pengiriman   : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No HP":telepon,
            "kurir Pengiriman":kurir_pengiriman,
            "product id":data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("=====Metode Pembayaran=====")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("pilih ID metode pembayaran:"))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : " , dict_trx["nama penerima"])
        print("alamat Penerima : " , dict_trx["alamat penerima"])
        print("No Hp : " , dict_trx["No Hp"])
        print("Kurir Pengiriman : " , dict_trx["Kurir pengiriman"])
        print("Product : " , data_product[pilih_id])
        print("Harga : " , daftar_harga[pilih_id])
        print("Metode Pembayaran : " , daftar_metode_pembayaran[pilih_id])
        konfirmasi = input("Apakah Anda yakin ingin melakukan pembayaran? (Y?N) : " )
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Anda sudah berhasil melakukan pembayaran")
        else:
            pass
    else:
        print("Id metode pembayaran tidak tersedia")
