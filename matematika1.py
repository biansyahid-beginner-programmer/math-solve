def luas_ruang_kubus():
    print("[ LUAS PERMUKAAN KUBUS ]")
    s = float(input("Masukkan panjang salah satu sisi kubus: "))
    hasil = 6 * (s * s)
    print(f"Luas permukaan kubus tersebut adalah {hasil}")

def luas_ruang_balok():
    print("[ LUAS PERMUKAAN BALOK ]")
    p = float(input("Masukkan panjang dari balok: "))
    l = float(input("Masukkan juga lebar balok: "))
    t = float(input("Yang terakhir, masukkan tinggi balok: "))
    hasil = 2 * ((p * l) + (p * t) + (l * t))
    print(f"Hasilnya adalah {hasil}")

def luas_ruang_tabung():
    print("[ LUAS PERMUKAAN TABUNG ]")
    r = float(input("Masukkan jari-jari tabung: "))
    t = float(input("Masukkan tinggi tabung: "))
    if r % 7 == 0:
        hasil = 2 * 22/7 * r * (r + t)
        print(f"Menggunakan 22/7 karena {r} kelipatan 7")
    else:
        hasil = 2 * 3.14 * r * (r + t)
        print(f"Menggunakan 3.14 karena {r} bukan kelipatan 7")
    
    if hasil.is_integer():
        print(f"Berarti luas permukaannya: {int(hasil)}")
    else:
        print(f"Berarti luas permukaannya: {round(hasil, 2)}")

def luas_ruang_kerucut():
    print("[ LUAS PERMUKAAN KERUCUT ]")
    r = float(input("Masukkan jari-jari kerucut terlebih dahulu: "))
    s = float(input("Masukkan panjang garis pelukis kerucut: "))
    if r % 7 == 0:
        hasil = 22/7 * r * (r + s)
        print(f"Menggunakan 22/7 karena {r} kelipatan 7")
    else:
        hasil = 3.14 * r * (r + s)
        print(f"Menggunakan 3.14 karena {r} bukan kelipatan 7")
    
    if hasil.is_integer():
        print(f"Berarti luas permukaan kerucutnya adalah: {int(hasil)}")
    else:
        print(f"Berarti luas permukaan kerucutnya adalah: {round(hasil, 2)}")

def luas_ruang_bola():
    print("[ LUAS PERMUKAAN BOLA ]")
    r = float(input("Masukkan jari-jari bola terlebih dahulu: "))
    if r % 7 == 0:
        hasil = 4 * 22/7 * r * r
        print(f"Menggunakan 22/7 karena {r} kelipatan 7")
    else:
        hasil = 4 * 3.14 * r * r
        print(f"Menggunakan 3.14 karena {r} bukan kelipatan 7")

    if hasil.is_integer():
        print(f"Berarti luas permukaannya: {int(hasil)}")
    else:
        print(f"Berarti luas permukaannya: {round(hasil, 2)}")

# <<<<<<<<<< PERBATASAN LUAS - VOLUME >>>>>>>>>>

def volume_ruang_kubus():
    print(" [ VOLUME KUBUS ]")
    s = float(input("Masukkan panjang sisi kubus: "))
    hasil = s * s * s
    print(f"Hasilnya yaitu: {hasil}")

def volume_ruang_balok():
    print("[ VOLUME BALOK ]")
    p = float(input("Masukkan panjang balok terlebih dahulu: "))
    l = float(input("Masukkan juga lebar baloknya: "))
    t = float(input("Yang terakhir masukkan tinggi balok: "))
    hasil = p * l * t
    print(f"Hasil atau volume balok yang panjangnya {p}, lebarnya {l}, dan tingginya {t} adalah {hasil}")

def volume_ruang_tabung():
    print("[ VOLUME TABUNG ]")
    r = float(input("Masukkan terlebih dahulu jari-jari tabung: "))
    t = float(input("masukkan juga tinggi tabung: "))
    if r % 7 == 0:
        hasil = 22/7 * r * r * t
    else:
        hasil = 3.14 * r * r * t
    print(f"Berarti volume tabungnnya adalah: {hasil}")

def volume_ruang_kerucut():
    print("[ VOLUME KERUCUT ]")
    r = float(input("Yang pertama, masukkan jari-jari kerucut terlebih dahulu: "))
    t = float(input("Yang kedua, masukkan juga tingi kerucut: "))
    if r % 7 == 0:
        hasil = 1/3 * 22/7 * r * r * t
    else:
        hasil = 1/3 * 3.14 * r * r * t
    print(f"Berarti volume tabungnnya adalah: {hasil}")
    print(f"Volumenya adalah: {hasil}")

def volume_ruang_bola():
    print("[ VOLUME BOLA ]")
    r = float(input("masukkan jari-jari bola: "))
    if r % 7 == 0:
        hasil = 4/3 * 22/7 * r * r * r
    else:
        hasil = 4/3 * 3.14 * r * r * r
    print(f"Volume bolanya adalah: {hasil}")

def volume_ruang_prisma():
    print("[ VOLUME PRISMA SEGITIGA ]")
    a = float(input("Masukkan panjang alas segitiga pada prisma: "))
    b = float(input("masukkan juga tinggi segitiga pada prisma: "))
    t = float(input("Yang terakhir masukkan tinggi prisma: "))
    hasil = (1/2 * a * b) * t
    print(f"Jadi, hasilnya adalah: {hasil}")

def volume_limas_segiempat():
    print("[ VOLUME LIMAS SEGI EMPAT (PERSEGI) ]")
    s = float(input("Pertama-tama, masukkan panjang alas atau sisi persegi bagian bawah limas: "))
    t = float(input("Yang kedua, masukkan tinggi limas: "))
    hasil = 1/3 * (s * s) * t