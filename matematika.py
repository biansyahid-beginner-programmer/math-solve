def luas_segitiga():
    print("[ LUAS SEGITIGA ]")
    alas = float(input("Pertama, masukkan dulu panjang alasnya: "))
    tinggi = float(input("Kedua, masukkan tinggi segitiganya: "))
    hasil = 1/2 * alas * tinggi
    print(f"Input diterima!\nLuas dari segitiga yang alasnya berukuran {alas} dan tingginya {tinggi} adalah {hasil}")

def luas_persegi_panjang():
    print("[ LUAS PERSEGI PANJANG ]")
    panjang = float(input("Pertama, masukkan dulu panjangnya: "))
    lebar = float(input("Kedua, masukkan juga lebarnya: "))
    hasil = panjang * lebar
    print(f"Input diterima!\nLuas dari persegi panjang yang panjangnya {panjang} dan lebarnya {lebar} adalah {hasil}")

def luas_lingkaran():
    print("[ LUAS LINGKARAN ]")
    perhitungan = input("Gunakan (r) Jari-jari atau (d) Diameter?: ").lower()
    
    if perhitungan == "r":
        r = float(input("Masukkan jari-jari: "))
        if r % 7 == 0:
            hasil = 22/7 * r * r
            print(f"Menggunakan 22/7 karena {r} kelipatan 7")
        else:
            hasil = 3.14 * r * r
            print(f"Menggunakan 3.14 karena {r} bukan kelipatan 7")
    elif perhitungan == "d":
        d = float(input("Masukkan diameter: "))
        if d % 7 == 0:
            hasil = 1/4 * 22/7 * d * d
            print(f"Menggunakan 22/7 karena {d} kelipatan 7")
        else:
            hasil = 1/4 * 3.14 * d * d
            print(f"Menggunakan 3.14 karena {d} bukan kelipatan 7")
    else:
        print("Mohon kerja samanya untuk hanya menuliskan huruf 'd' atau 'r'!")
        return

    if hasil.is_integer():
        print(f"Berarti luas Lingkarannya: {int(hasil)}")
    else:
        print(f"Berarti luas Lingkarannya: {round(hasil, 2)}")

def luas_persegi():
    print("[ LUAS PERSEGI ]")
    s = float(input("Silahkan masukkan panjang sisi persegi: "))
    hasil = s * s
    print(f"Input diterima!\nLuas dari persegi yang panjang sisinya {s} adalah: {hasil}")

def luas_trapesium():
    print("[ LUAS TRAPESIUM ]")
    a = float(input("Silahkan masukkan panjang trapesium sebelah atas (a): "))
    b = float(input("Sekarang masukkan juga panjang trapesium bagian bawah (b) "))
    t = float(input("Yang terakhir, masukkan pula tinggi trapesiumnya: "))
    hasil = 0.5 * (a + b) * t
    print(f"Hasilnya menjadi {hasil} dengan a = {a}, b = {b} dan t = {t}")

def luas_jajar_genjang():
    print("[ LUAS JAJAR GENJANG ]")
    alas = float(input("Pertama, masukkan dulu alasnya: "))
    tinggi = float(input("Kedua, masukkan juga tingginya: "))
    hasil = alas * tinggi
    print(f"Input diterima!\nLuas dari jajar genjang yang alasnya {alas} dan tingginya {tinggi} adalah {hasil}")

def luas_belah_ketupat_layang():
    print("[ BELAH KETUPAT DAN LAYANG LAYANG ]")
    d1 = float(input("Masukkan dulu diagonal 1: "))
    d2 = float(input("Masukkan lagi diagonal yang ke 2: "))
    hasil = 0.5 * d1 * d2
    print(f"Sudah selesai!\nHasilnya adalah {hasil}")



def keliling_segitiga():
    print("[ KELILING SEGITIGA ]")
    s1 = float(input("Masukkan panjang sisi segitiga yang pertama: "))
    s2 = float(input("Masukkan panjang sisi segitiga yang kedua: "))
    s3 = float(input("Masukkan panjang sisi segitiga yang ketiga: "))
    hasil = s1 + s2 + s3
    print(f"Okey, hasilnya adalah {hasil}")

def keliling_persegi_panjang():
    print("[ KELILING PERSEGI PANJANG ]")
    panjang = float(input("Masukkan panjang dari persegi panjang: "))
    lebar = float(input("Masukkan juga lebarnya: "))
    hasil = 2 * (panjang + lebar)
    print(f"Sudah selesai!\nJawabannya adalah {hasil}")

def keliling_lingkaran():
    print("[ KELILING LINGKARAN ]")
    pilihan = input("Ingin menggunakan diameter atau jari-jari? Jika diameter ketik 'd' kalu jari-jari ketik 'r': ").lower()

    if pilihan == "d":
        diameter = float(input("Masukkan panjang diameter lingkaran: "))
        if diameter % 7 == 0:
            hasil = 22/7 * diameter
            print(f"Menggunakan 22/7 karena {diameter} kelipatan 7")
        else:
            hasil = 3.14 * diameter
            print(f"Menggunakan 3.14 karena {diameter} bukan kelipatan 7")
    elif pilihan == "r":
        r = float(input("Masukkan panjang jari-jarinya: "))
        if r % 7 == 0:
            hasil = 2 * 22/7 * r 
            print(f"Menggunakan 22/7 karena {r} kelipatan 7")
        else:
            hasil = 2 * 3.14 * r 
            print(f"Menggunakan 3.14 karena {r} bukan kelipatan 7")

    if hasil.is_integer():
        print(f"Berarti luas Lingkarannya: {int(hasil)}")
    else:
        print(f"Berarti luas Lingkarannya: {round(hasil, 2)}")

def keliling_persegi():
    print("[ KELILING PERSEGI ]")
    s = float(input("Masukkan panjang salah satu sisi persegi: "))
    hasil = s * 4
    print(f"Hasil keliling dari persegi yang salah satu panjang sisinya {s} adalah {hasil}")

def keliling_trapesium():
    s1 = float(input("Masukkan sisi trapesium ke 1: "))
    s2 = float(input("Masukkan sisi trapesium ke 2: "))
    s3 = float(input("Masukkan sisi trapesium ke 3: "))
    s4 = float(input("Masukkan sisi trapesium ke 4: "))
    hasil = s1 + s2 + s3 + s4
    print(f"Siap, keliling dari trapesium yang panjang sisinya {s1}, {s2}, {s3}, dan {s4} adalah {hasil}")

def keliling_jajar_genjang():
    a = float(input("Masukkan panjang alas trapesiumnya dulu: "))
    b = float(input("Masukkan juga panjang sisi miringnya: "))
    hasil = 2 * (a + b)
    print(f"Hasil dari trapesium yang memiliki panjang alas {a} dan sisi miring {b} adalah {hasil}")

def keliling_layang_layang():
    a = float(input("Masukkan salah satu sisi layang-layang yang terpendek: "))
    b = float(input("Masukkan juga salah satu sisi layang-layang yang terpanjang: "))
    hasil = 2 * (a + b)
    print(f"Keliling dari layang-layang tersebut adalah {hasil}")

def keliling_belah_ketupat():
    a = float(input("Masukkan panjang salah satu sisi miringnya: "))
    hasil = a * 4
    print(f"Keliling dari belah ketupat yang panjang salah satu sisinya {a} adalah {hasil}")