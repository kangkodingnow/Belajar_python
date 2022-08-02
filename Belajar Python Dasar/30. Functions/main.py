#membuat fungsi sederhana

def suaranya():
    print("kukuruyuk!!!")

def harganya():
    suaranya()
    print("harga ayam per 1 kg adalah Rp. 20.000")

#membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaranya()
    harga = 20000
    hargaTotal = kg*harga
    print("harga",kg,"kg ayam adalah",hargaTotal)

harganya()
hargatotalayam(20)