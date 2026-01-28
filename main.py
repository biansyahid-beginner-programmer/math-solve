import os
import datetime
import matematika
import matematika1

def jalankan_aplikasi():

    def bersihkan_layar():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def dapatkan_sapaan():
        jam = datetime.datetime.now().hour
        if 5 <= jam < 11:
            return "Selamat Pagi ☀️"
        elif 11 <= jam < 15:
            return "Selamat Siang 🌤️"
        elif 15 <= jam < 18:
            return "Selamat Sore 🌤️"
        else:
            return "Selamat Malam 🌙"

    salam = dapatkan_sapaan()

    while True:
        bersihkan_layar()
        print("=" * 40)
        print(f"{salam}, dan selamat datang!")
        print("Apakah ada yang bisa saya bantu berhitung hari ini?")
        print("=" * 40)
        print("\n\n" + "="*40)
        print("             MATH Solve")
        print("="*40)
        
        jawaban = input("Apakah anda ingin menggunakan aplikasi ini? (ya/tidak): ").lower()
        if jawaban == "tidak":
            print("Sampai jumpa, semoga hari-hari anda beruntung hari ini!")
            break

        elif jawaban == "ya":
            print("\nPilihan: \n1. Bangun datar\n2. Bangun ruang")
            bangun = input("\nMasukkan pilihannya dengan mengetik 1 atau 2: ")

            if bangun == "1":
                print("\n\nPilihan:\n1. Luas\n2. Keliling")
                bangun_datar = input("Masukkan pilihan dengan memasukkan angka 1 atau 2: ")

                if bangun_datar == "1":
                    print("\n\n1. Segitiga\n2. Persegi Panjang\n3. Lingkaran\n4. Persegi\n5. Trapesium\n6. Jajar Genjang\n7. Belah Ketupat/Layang-layang")
                    angka = input("\nMasukkan pilihannya ya... (1-7): ")

                    print("-" * 30)
                    match angka:
                        case "1": matematika.luas_segitiga()
                        case "2": matematika.luas_persegi_panjang()
                        case "3": matematika.luas_lingkaran()
                        case "4": matematika.luas_persegi()
                        case "5": matematika.luas_trapesium()
                        case "6": matematika.luas_jajar_genjang()
                        case "7": matematika.luas_belah_ketupat_layang()
                        case _: print("[!] Pilihan tidak tersedia. Mohon masukkan angka antara 1-7!")
                    print("-" * 30)

                elif bangun_datar == "2":
                    print("\n\n1. Segitiga\n2. Persegi Panjang\n3. Lingkaran\n4. Persegi\n5. Trapesium\n6. Jajar Genjang\n7. Belah Ketupat\n8. Layang-layang")
                    angka_bangun_datar = input("Masukkan pilihan antara (1-8): ")

                    print("-" * 30)
                    match angka_bangun_datar:
                        case "1":matematika.keliling_segitiga()
                        case "2":matematika.keliling_persegi_panjang()
                        case "3":matematika.keliling_lingkaran()
                        case "4":matematika.keliling_persegi()
                        case "5":matematika.keliling_trapesium()
                        case "6":matematika.keliling_jajar_genjang()
                        case "7":matematika.keliling_belah_ketupat()
                        case "8":matematika.keliling_layang_layang()
                        case _: print("[!] Pilihan tidak tersedia. Mohon masukkan angka antara 1-8!")
                    print("-" * 30)
                
                else:
                    print("[!] Mohon masukkan pilihan dengan mengetik angka 1 atau 2!")

            elif bangun == "2":
                print("\nPilihan:\n1. Luas\n2. Volume")
                bangun_ruang = input("Masukkan angka pilihan antara 1 atau 2: ")

                if bangun_ruang == "1":
                    print("\n1. Persegi\n2. Balok\n3. Tabung\n4. Kerucut\n5. Bola")
                    angka_Luas_bangun_ruang = input("Masukkan pilihan antara 1-5: ")

                    print("-" * 30)
                    match angka_Luas_bangun_ruang:
                        case "1":matematika1.luas_ruang_kubus()
                        case "2":matematika1.luas_ruang_balok()
                        case "3":matematika1.luas_ruang_tabung()
                        case "4":matematika1.luas_ruang_kerucut()
                        case "5":matematika1.luas_ruang_bola()
                        case _: print("[!] Pilihan tidak tersedia. Mohon masukkan angka antara 1-5!")
                    print("-" * 30)

                elif bangun_ruang == "2":
                    print("\n1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Bola\n6. Prisma segitiga\n7. Limas segi empat (persegi)")
                    angka_volume_bangun_ruang = input("Masukkan pilihan antara 1-7: ")

                    print("-" * 30)
                    match angka_volume_bangun_ruang:
                        case "1":matematika1.volume_ruang_kubus()
                        case "2":matematika1.volume_ruang_balok()
                        case "3":matematika1.volume_ruang_tabung()
                        case "4":matematika1.volume_ruang_kerucut()
                        case "5":matematika1.volume_ruang_bola()
                        case "6":matematika1.volume_ruang_prisma()
                        case "7":matematika1.volume_limas_segiempat()
                        case _: print("[!] Pilihan tidak tersedia. Mohon masukkan angka antara 1-7!")
                    print("-" * 30)
                
                else:
                    print("[!] Mohon masukkan angka antara 1 atau 2")

            else:
                print("[!] Mohon kesediaannya untuk mengetik dan memilih antara 1 atau 2! Terimakasih")

        else:
            print("\n[!] Mohon bantuannya untuk mengetik 'ya' atau 'tidak'")
            
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    jalankan_aplikasi()