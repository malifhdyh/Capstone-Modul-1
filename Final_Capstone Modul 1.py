import os
from tabulate import tabulate
from datetime import datetime

# Collection data types untuk menyimpan data penjualan
data_barang = [
    {
        'id': '001',
        'nama': 'Jamu Kunyit Asam',
        'kategori': 'Jamu',
        'harga': 15000,
        'stok': 50,
        'supplier': 'CV Jamu Sehat'
    },
    {
        'id': '002',
        'nama': 'Jamu Beras Kencur',
        'kategori': 'Jamu',
        'harga': 12000,
        'stok': 35,
        'supplier': 'PT Herbal Nusantara'
    },
    {
        'id': '003',
        'nama': 'Minyak Kayu Putih',
        'kategori': 'Obat',
        'harga': 25000,
        'stok': 20,
        'supplier': 'CV Jamu Sehat'
    },
    {
        'id': '004',
        'nama': 'Jamu Temulawak',
        'kategori': 'Jamu',
        'harga': 18000,
        'stok': 40,
        'supplier': 'UD Sehat Alami'
    },
    {
        'id': '005',
        'nama': 'Kapsul Sambiloto',
        'kategori': 'Suplemen',
        'harga': 35000,
        'stok': 25,
        'supplier': 'PT Herbal Nusantara'
    },
    {
        'id': '006',
        'nama': 'Tolak Angin',
        'kategori': 'Obat',
        'harga': 8000,
        'stok': 60,
        'supplier': 'CV Jamu Sehat'
    },
    {
        'id': '007',
        'nama': 'Vitamin Anak Herbal',
        'kategori': 'Suplemen',
        'harga': 45000,
        'stok': 15,
        'supplier': 'UD Sehat Alami'
    }
]

data_penjualan = [] # Data transaksi penjualan
nomor_transaksi = 1 
recycle_bin = [] # Data recycle bin untuk menyimpan barang yang dihapus


def clear_screen():
    # Fungsi untuk membersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    # Fungsi untuk menampilkan header aplikasi
    print("=" * 70)
    print("                PENJUALAN TOKO JAMU Mas AL")
    print("=" * 70)

def generate_id_baru():
    # Fungsi untuk generate ID baru
    if not data_barang:
        return '001'
    
    max_id = max([int(b['id']) for b in data_barang])
    return f"{max_id + 1:03d}"

def main_menu():
    # Fungsi untuk menampilkan menu utama
    while True:
        clear_screen()
        tampilkan_header()
        print("\n🏪 MENU UTAMA TOKO JAMU:")
        print("1. 🛍️  Penjualan Barang")
        print("2. 📦 Display Stok Barang")
        print("3. ➕ Tambah Barang Baru")
        print("4. 🔄 Update Data Barang")
        print("5. 🗑️  Hapus Data Barang")
        print("6. 📊 Laporan Penjualan")
        print("7. 🚪 Keluar")
        print("-" * 70)
        
        try:
            pilihan = input("Pilih menu (1-7): ").strip()
            
            if pilihan == '1':
                penjualan_menu()
            elif pilihan == '2':
                read_menu()
            elif pilihan == '3':
                create_menu()
            elif pilihan == '4':
                update_menu()
            elif pilihan == '5':
                delete_menu()
            elif pilihan == '6':
                laporan_penjualan()
            elif pilihan == '7':
                print("\n✅ Terima kasih telah menggunakan Sistem Penjualan Toko Jamu!")
                print("Semoga sehat selalu! 🌿")
                break
            else:
                print("\n❌ Pilihan tidak valid! Silakan pilih 1-7.")
                input("Tekan Enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("\n\n✅ Program dihentikan oleh user.")
            break

def penjualan_menu():
    # Fungsi untuk menu penjualan barang dengan shopping cart
    global nomor_transaksi
    
    clear_screen()
    tampilkan_header()
    print("\n🛍️ PENJUALAN BARANG")
    print("-" * 70)
    
    # Inisialisasi shopping cart
    shopping_cart = []
    total_belanja = 0
    
    while True:
        clear_screen()
        tampilkan_header()
        print("\n🛒 SHOPPING CART")
        print("-" * 70)
        
        # Tampilkan daftar barang yang tersedia
        print("\n📦 DAFTAR BARANG TERSEDIA:")
        headers = ["ID", "Nama Barang", "Kategori", "Harga", "Stok"]
        table_data = []
        
        for barang in data_barang:
            if barang['stok'] > 0:  # Hanya tampilkan barang yang masih ada stoknya
                table_data.append([
                    barang['id'],
                    barang['nama'],
                    barang['kategori'],
                    f"Rp {barang['harga']:,}",
                    barang['stok']
                ])
        
        if not table_data:
            print("❌ Tidak ada barang yang tersedia untuk dijual.")
            input("Tekan Enter untuk kembali...")
            return
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        # Tampilkan isi shopping cart jika ada
        if shopping_cart:
            print("\n🛒 ISI KERANJANG BELANJA:")
            cart_headers = ["No", "Nama Barang", "Jumlah", "Harga Satuan", "Subtotal"]
            cart_data = []
            
            for idx, item in enumerate(shopping_cart, 1):
                cart_data.append([
                    idx,
                    item['nama_barang'],
                    item['jumlah'],
                    f"Rp {item['harga_satuan']:,}",
                    f"Rp {item['subtotal']:,}"
                ])
            
            print(tabulate(cart_data, headers=cart_headers, tablefmt="grid"))
            print(f"\n💰 TOTAL BELANJA: Rp {total_belanja:,}")
        
        print("\n📋 MENU:")
        print("1. Tambah Barang ke Keranjang")
        print("2. Hapus Barang dari Keranjang")
        print("3. Proses Pembayaran")
        print("4. Kosongkan Keranjang")
        print("5. Kembali ke Menu Utama")
        print("-" * 70)
        
        try:
            pilihan = input("Pilih menu (1-5): ").strip()
            
            if pilihan == '1':  # Tambah barang ke keranjang
                id_barang = input("\nMasukkan ID barang yang akan dibeli: ").strip()
                barang = next((b for b in data_barang if b['id'] == id_barang), None)
                
                if not barang:
                    print(f"\n❌ Barang dengan ID {id_barang} tidak ditemukan.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                if barang['stok'] <= 0:
                    print(f"\n❌ Maaf, {barang['nama']} sedang habis.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                print(f"\n📋 Barang dipilih: {barang['nama']}")
                print(f"💰 Harga: Rp {barang['harga']:,}")
                print(f"📦 Stok tersedia: {barang['stok']}")
                
                jumlah = int(input("\nMasukkan jumlah yang akan dibeli: "))
                
                if jumlah <= 0:
                    print("\n❌ Jumlah harus lebih dari 0!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                if jumlah > barang['stok']:
                    print(f"\n❌ Stok tidak mencukupi! Stok tersedia: {barang['stok']}")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                # Cek apakah barang sudah ada di keranjang
                item_exist = next((item for item in shopping_cart if item['id_barang'] == id_barang), None)
                
                if item_exist:
                    # Update jumlah jika barang sudah ada di keranjang
                    new_qty = item_exist['jumlah'] + jumlah
                    if new_qty > barang['stok']:
                        print(f"\n❌ Total jumlah melebihi stok yang tersedia! Stok tersedia: {barang['stok']}")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    item_exist['jumlah'] = new_qty
                    item_exist['subtotal'] = new_qty * barang['harga']
                else:
                    # Tambahkan barang baru ke keranjang
                    shopping_cart.append({
                        'id_barang': barang['id'],
                        'nama_barang': barang['nama'],
                        'kategori': barang['kategori'],
                        'jumlah': jumlah,
                        'harga_satuan': barang['harga'],
                        'subtotal': jumlah * barang['harga']
                    })
                
                # Update total belanja
                total_belanja = sum(item['subtotal'] for item in shopping_cart)
                
                print(f"\n✅ {barang['nama']} berhasil ditambahkan ke keranjang!")
                input("Tekan Enter untuk melanjutkan...")
                
            elif pilihan == '2':  # Hapus barang dari keranjang
                if not shopping_cart:
                    print("\n❌ Keranjang belanja kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                try:
                    no_item = int(input("\nMasukkan nomor barang yang akan dihapus: ")) - 1
                    if 0 <= no_item < len(shopping_cart):
                        removed_item = shopping_cart.pop(no_item)
                        total_belanja -= removed_item['subtotal']
                        print(f"\n✅ {removed_item['nama_barang']} berhasil dihapus dari keranjang!")
                    else:
                        print("\n❌ Nomor barang tidak valid!")
                except ValueError:
                    print("\n❌ Input harus berupa angka!")
                
                input("Tekan Enter untuk melanjutkan...")
                
            elif pilihan == '3':  # Proses pembayaran
                if not shopping_cart:
                    print("\n❌ Keranjang belanja kosong!")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                print("\n🧾 DETAIL PEMBELIAN:")
                for item in shopping_cart:
                    print(f"- {item['nama_barang']} ({item['jumlah']} x Rp {item['harga_satuan']:,}) = Rp {item['subtotal']:,}")
                print(f"\n💰 TOTAL BELANJA: Rp {total_belanja:,}")
                
                konfirmasi = input("\nLanjutkan ke pembayaran? (y/n): ").strip().lower()
                
                if konfirmasi in ['y', 'yes', 'ya']:
                    # Proses pembayaran
                    berhasil_bayar = proses_pembayaran(total_belanja)
                    
                    if berhasil_bayar:
                        # Kurangi stok dan simpan transaksi
                        for item in shopping_cart:
                            barang = next(b for b in data_barang if b['id'] == item['id_barang'])
                            barang['stok'] -= item['jumlah']
                            
                            # Simpan transaksi
                            transaksi = {
                                'no_transaksi': f"TRX{nomor_transaksi:03d}",
                                'id_barang': item['id_barang'],
                                'nama_barang': item['nama_barang'],
                                'kategori': item['kategori'],
                                'jumlah': item['jumlah'],
                                'harga_satuan': item['harga_satuan'],
                                'total_harga': item['subtotal']
                            }
                            
                            data_penjualan.append(transaksi)
                        
                        nomor_transaksi += 1
                        
                        print(f"\n✅ Transaksi berhasil!")
                        print(f"📄 Nomor transaksi: TRX{nomor_transaksi-1:03d}")
                        print("=" * 50)
                        print("🧾 STRUK PEMBELIAN")
                        print("=" * 50)
                        print(f"🏪 Toko Jamu Mas Al")
                        print(f"📞 Telp: 089513363429")
                        print(f"📍 Jl. Sehat No. 123, Jakarta")
                        print(f"📅 {datetime.now().strftime('%d-%m-%Y %H:%M')}")
                        print(f"📄 No. Transaksi: TRX{nomor_transaksi-1:03d}")
                        print("-" * 50)
                        
                        for item in shopping_cart:
                            print(f"{item['nama_barang']}")
                            print(f"{item['jumlah']} x Rp {item['harga_satuan']:,}")
                            print(f"{'':>20} = Rp {item['subtotal']:,}")
                        
                        print("-" * 50)
                        print(f"{'TOTAL':>30} : Rp {total_belanja:,}")
                        print("=" * 50)
                        print("🌿 Terima kasih telah berbelanja!")
                        print("🙏 Semoga lekas sembuh dan sehat selalu!")
                        print("=" * 50)
                        
                        # Kosongkan keranjang setelah transaksi selesai
                        shopping_cart = []
                        total_belanja = 0
                    else:
                        print("\n❌ Transaksi dibatalkan karena pembayaran tidak berhasil.")
                else:
                    print("\n❌ Pembelian dibatalkan.")
                
                input("Tekan Enter untuk melanjutkan...")
                
            elif pilihan == '4':  # Kosongkan keranjang
                if not shopping_cart:
                    print("\n❌ Keranjang belanja sudah kosong!")
                else:
                    konfirmasi = input("\nYakin ingin mengosongkan keranjang belanja? (y/n): ").strip().lower()
                    if konfirmasi in ['y', 'yes', 'ya']:
                        shopping_cart = []
                        total_belanja = 0
                        print("\n✅ Keranjang belanja berhasil dikosongkan!")
                    else:
                        print("\n❌ Keranjang belanja tidak dikosongkan.")
                
                input("Tekan Enter untuk melanjutkan...")
                
            elif pilihan == '5':  # Kembali ke menu utama
                if shopping_cart:
                    konfirmasi = input("\nAnda memiliki barang di keranjang. Yakin ingin kembali? (y/n): ").strip().lower()
                    if konfirmasi in ['y', 'yes', 'ya']:
                        break
                else:
                    break
            else:
                print("\n❌ Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
                
        except ValueError:
            print("\n❌ Jumlah harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")
            input("Tekan Enter untuk melanjutkan...")

def read_menu():
    # Fungsi untuk menu kelola stok barang
    while True:
        clear_screen()
        tampilkan_header()
        print("\n📦 MENU DISPLAY STOK BARANG:")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan ID")
        print("3. Cari Barang Berdasarkan Nama")
        print("4. Filter Berdasarkan Kategori")
        print("5. Kembali ke Menu Utama")
        print("-" * 70)
        
        pilihan = input("Pilih opsi (1-5): ").strip()
        
        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            cari_barang_by_id()
        elif pilihan == '3':
            cari_barang_by_nama()
        elif pilihan == '4':
            filter_by_kategori()
        elif pilihan == '5':
            break
        else:
            print("\n❌ Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

def tampilkan_semua_barang():
    # Fungsi untuk menampilkan semua barang
    clear_screen()
    tampilkan_header()
    print("\n📦 DAFTAR SEMUA BARANG:")
    
    if not data_barang:
        print("❌ Tidak ada data barang.")
    else:
        headers = ["ID", "Nama Barang", "Kategori", "Harga", "Stok", "Supplier"]
        table_data = []
        
        for barang in data_barang:
            table_data.append([
                barang['id'],
                barang['nama'],
                barang['kategori'],
                f"Rp {barang['harga']:,}",
                barang['stok'],
                barang['supplier']
            ])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    input("\nTekan Enter untuk kembali...")

def cari_barang_by_id():
    # Fungsi untuk mencari barang berdasarkan ID
    id_cari = input("\nMasukkan ID barang yang dicari: ").strip()
    barang = next((b for b in data_barang if b['id'] == id_cari), None)
    
    if barang:
        print("\n✅ Barang ditemukan:")
        tampilkan_detail_barang(barang)
    else:
        print(f"\n❌ Barang dengan ID {id_cari} tidak ditemukan.")
    
    input("Tekan Enter untuk melanjutkan...")

def cari_barang_by_nama():
    # Fungsi untuk mencari barang berdasarkan nama
    nama_cari = input("\nMasukkan nama barang yang dicari: ").strip().lower()
    hasil = [b for b in data_barang if nama_cari in b['nama'].lower()]
    
    if hasil:
        print(f"\n✅ Ditemukan {len(hasil)} barang:")
        headers = ["ID", "Nama Barang", "Kategori", "Harga", "Stok", "Supplier"]
        table_data = []
        
        for barang in hasil:
            table_data.append([
                barang['id'],
                barang['nama'],
                barang['kategori'],
                f"Rp {barang['harga']:,}",
                barang['stok'],
                barang['supplier']
            ])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print(f"\n❌ Tidak ada barang dengan nama yang mengandung '{nama_cari}'.")
    
    input("Tekan Enter untuk melanjutkan...")

def filter_by_kategori():
    # Fungsi untuk filter barang berdasarkan kategori
    kategori_list = ['Jamu', 'Obat', 'Suplemen']
    
    print("\n📂 Pilih Kategori:")
    for i, kategori in enumerate(kategori_list, 1):
        print(f"{i}. {kategori}")
    
    try:
        pilihan = int(input(f"\nPilih kategori (1-{len(kategori_list)}): ")) - 1
        if 0 <= pilihan < len(kategori_list):
            kategori_pilihan = kategori_list[pilihan]
            hasil = [b for b in data_barang if b['kategori'] == kategori_pilihan]
            
            if hasil:
                print(f"\n✅ Barang dalam kategori '{kategori_pilihan}':")
                headers = ["ID", "Nama Barang", "Kategori", "Harga", "Stok", "Supplier"]
                table_data = []
                
                for barang in hasil:
                    table_data.append([
                        barang['id'],
                        barang['nama'],
                        barang['kategori'],
                        f"Rp {barang['harga']:,}",
                        barang['stok'],
                        barang['supplier']
                    ])
                
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print(f"\n❌ Tidak ada barang dalam kategori '{kategori_pilihan}'.")
        else:
            print("\n❌ Pilihan kategori tidak valid!")
    except ValueError:
        print("\n❌ Input harus berupa angka!")
    
    input("Tekan Enter untuk melanjutkan...")

def create_menu():
    # Fungsi untuk menu tambah barang baru
    clear_screen()
    tampilkan_header()
    print("\n➕ TAMBAH BARANG BARU:")
    print("-" * 70)
    
    try:
        new_id = generate_id_baru()
        
        nama = input("Nama Barang: ").strip()
        if not nama:
            print("\n❌ Nama barang tidak boleh kosong!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        print("\n📂 Pilih Kategori:")
        kategori_list = ['Jamu', 'Obat', 'Suplemen']
        for i, kat in enumerate(kategori_list, 1):
            print(f"{i}. {kat}")
        
        pilihan_kat = int(input("Pilih kategori (1-3): ")) - 1
        if not (0 <= pilihan_kat < len(kategori_list)):
            print("\n❌ Pilihan kategori tidak valid!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        kategori = kategori_list[pilihan_kat]
        
        harga = int(input("Harga: Rp "))
        if harga <= 0:
            print("\n❌ Harga harus lebih dari 0!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        stok = int(input("Stok: "))
        if stok < 0:
            print("\n❌ Stok tidak boleh negatif!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        supplier = input("Supplier: ").strip()
        if not supplier:
            print("\n❌ Supplier tidak boleh kosong!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        # Buat data baru
        barang_baru = {
            'id': new_id,
            'nama': nama,
            'kategori': kategori,
            'harga': harga,
            'stok': stok,
            'supplier': supplier
        }
        
        # Konfirmasi
        print("\n📋 DATA BARANG BARU:")
        tampilkan_detail_barang(barang_baru)
        
        konfirmasi = input("\nSimpan data ini? (y/n): ").strip().lower()
        if konfirmasi in ['y', 'yes', 'ya']:
            data_barang.append(barang_baru)
            print(f"\n✅ Barang '{nama}' berhasil ditambahkan dengan ID {new_id}!")
        else:
            print("\n❌ Data tidak disimpan.")
            
    except ValueError:
        print("\n❌ Input harga dan stok harus berupa angka!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
    
    input("Tekan Enter untuk melanjutkan...")

def update_menu():
    # Fungsi untuk menu update data barang
    while True:
        clear_screen()
        tampilkan_header()
        print("\n🔄 MENU UPDATE DATA:")
        print("1. Lihat Semua Barang")
        print("2. Update Data Barang")
        print("3. Kembali ke Menu Utama")
        print("-" * 70)
        
        pilihan = input("Pilih opsi (1-3): ").strip()
        
        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            update_barang()
        elif pilihan == '3':
            break
        else:
            print("\n❌ Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

def update_barang():
    # Fungsi untuk mengupdate data barang
    try:
        id_update = input("\nMasukkan ID barang yang akan diupdate: ").strip()
        barang = next((b for b in data_barang if b['id'] == id_update), None)
        
        if not barang:
            print(f"\n❌ Barang dengan ID {id_update} tidak ditemukan.")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        print("\n📋 DATA SAAT INI:")
        tampilkan_detail_barang(barang)
        
        print("\n🔄 MASUKKAN DATA BARU (kosongkan jika tidak ingin mengubah):")
        
        # Update nama
        nama_baru = input(f"Nama Barang [{barang['nama']}]: ").strip()
        if nama_baru:
            barang['nama'] = nama_baru
        
        # Update kategori
        print(f"\nKategori saat ini: {barang['kategori']}")
        print("Pilih kategori baru:")
        kategori_list = ['Jamu', 'Obat', 'Suplemen']
        for i, kat in enumerate(kategori_list, 1):
            print(f"{i}. {kat}")
        
        kat_input = input("Pilih kategori (1-3, kosongkan jika tidak diubah): ").strip()
        if kat_input:
            try:
                pilihan_kat = int(kat_input) - 1
                if 0 <= pilihan_kat < len(kategori_list):
                    barang['kategori'] = kategori_list[pilihan_kat]
                else:
                    print("❌ Pilihan kategori tidak valid! Kategori tidak diubah.")
            except ValueError:
                print("❌ Input kategori harus berupa angka! Kategori tidak diubah.")
        
        # Update harga
        harga_input = input(f"Harga [Rp {barang['harga']:,}]: ").strip()
        if harga_input:
            harga_baru = int(harga_input)
            if harga_baru > 0:
                barang['harga'] = harga_baru
            else:
                print("❌ Harga harus lebih dari 0! Harga tidak diubah.")
        
        # Update stok
        stok_input = input(f"Stok [{barang['stok']}]: ").strip()
        if stok_input:
            stok_baru = int(stok_input)
            if stok_baru >= 0:
                barang['stok'] = stok_baru
            else:
                print("❌ Stok tidak boleh negatif! Stok tidak diubah.")
        
        # Update supplier
        supplier_baru = input(f"Supplier [{barang['supplier']}]: ").strip()
        if supplier_baru:
            barang['supplier'] = supplier_baru
        
        print("\n📋 DATA SETELAH UPDATE:")
        tampilkan_detail_barang(barang)
        
        konfirmasi = input("\nSimpan perubahan? (y/n): ").strip().lower()
        if konfirmasi in ['y', 'yes', 'ya']:
            print(f"\n✅ Data barang ID {id_update} berhasil diupdate!")
        else:
            print("\n❌ Perubahan tidak disimpan.")
            
    except ValueError:
        print("\n❌ Input harga dan stok harus berupa angka!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
    
    input("Tekan Enter untuk melanjutkan...")

def delete_menu():
    # Fungsi untuk menu hapus data barang
    while True:
        clear_screen()
        tampilkan_header()
        print("\n🗑️ MENU HAPUS DATA:")
        print("1. Lihat Semua Barang")
        print("2. Hapus Data Barang")
        print("3. Recycle Bin")
        print("4. Kembali ke Menu Utama")
        print("-" * 70)
        
        pilihan = input("Pilih opsi (1-4): ").strip()
        
        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            delete_barang()
        elif pilihan == '3':
            manage_recycle_bin()
        elif pilihan == '4':
            break
        else:
            print("\n❌ Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

def delete_barang():
    # Fungsi untuk menghapus data barang
    try:
        id_hapus = input("\nMasukkan ID barang yang akan dihapus: ").strip()
        barang = next((b for b in data_barang if b['id'] == id_hapus), None)
        
        if not barang:
            print(f"\n❌ Barang dengan ID {id_hapus} tidak ditemukan.")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        print("\n📋 DATA YANG AKAN DIHAPUS:")
        tampilkan_detail_barang(barang)
        
        print("\n⚠️ PERINGATAN: Data akan dipindahkan ke Recycle Bin!")
        konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ").strip().lower()
        
        if konfirmasi in ['y', 'yes', 'ya']:
            # Memindahkan ke recycle bin sebelum dihapus
            recycle_bin.append(barang)
            data_barang.remove(barang)
            print(f"\n✅ Barang '{barang['nama']}' dengan ID {id_hapus} berhasil dipindahkan ke Recycle Bin!")
        else:
            print("\n❌ Data tidak dihapus.")
            
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
    
    input("Tekan Enter untuk melanjutkan...")
    
def manage_recycle_bin():
    # Fungsi untuk mengelola recycle bin
    while True:
        clear_screen()
        tampilkan_header()
        print("\n🗑️ RECYCLE BIN MANAGEMENT:")
        print("1. Lihat Isi Recycle Bin")
        print("2. Restore Barang dari Recycle Bin")
        print("3. Kosongkan Recycle Bin (Hapus Permanen)")
        print("4. Kembali ke Menu Utama")
        print("-" * 70)
        
        pilihan = input("Pilih opsi (1-4): ").strip()
        
        if pilihan == '1':
            view_recycle_bin()
        elif pilihan == '2':
            restore_from_recycle_bin()
        elif pilihan == '3':
            empty_recycle_bin()
        elif pilihan == '4':
            break
        else:
            print("\n❌ Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

def view_recycle_bin():
    # Fungsi untuk melihat isi recycle bin
    clear_screen()
    tampilkan_header()
    print("\n🗑️ ISI RECYCLE BIN:")
    
    if not recycle_bin:
        print("\n❌ Recycle Bin kosong.")
    else:
        headers = ["No", "ID", "Nama Barang", "Kategori", "Harga", "Stok", "Supplier"]
        table_data = []
        
        for idx, barang in enumerate(recycle_bin, 1):
            table_data.append([
                idx,
                barang['id'],
                barang['nama'],
                barang['kategori'],
                f"Rp {barang['harga']:,}",
                barang['stok'],
                barang['supplier']
            ])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    input("\nTekan Enter untuk kembali...")

def restore_from_recycle_bin():
    # Fungsi untuk restore barang dari recycle bin
    if not recycle_bin:
        print("\n❌ Recycle Bin kosong.")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    try:
        view_recycle_bin()
        nomor = int(input("\nMasukkan nomor barang yang akan direstore: ")) - 1
        
        if 0 <= nomor < len(recycle_bin):
            barang = recycle_bin[nomor]
            
            # Cek apakah ID sudah ada di data_barang
            if any(b['id'] == barang['id'] for b in data_barang):
                print("\n❌ Barang dengan ID yang sama sudah ada di database.")
                print("Silakan update ID barang terlebih dahulu sebelum merestore.")
                input("Tekan Enter untuk melanjutkan...")
                return
            
            print("\n📋 DATA YANG AKAN DIRESTORE:")
            tampilkan_detail_barang(barang)
            
            konfirmasi = input("\nYakin ingin merestore data ini? (y/n): ").strip().lower()
            if konfirmasi in ['y', 'yes', 'ya']:
                data_barang.append(barang)
                recycle_bin.pop(nomor)
                print(f"\n✅ Barang '{barang['nama']}' berhasil direstore!")
            else:
                print("\n❌ Restore dibatalkan.")
        else:
            print("\n❌ Nomor barang tidak valid!")
    except ValueError:
        print("\n❌ Input harus berupa angka!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
    
    input("Tekan Enter untuk melanjutkan...")

def empty_recycle_bin():
    # Fungsi untuk mengosongkan recycle bin secara permanen
    if not recycle_bin:
        print("\n❌ Recycle Bin sudah kosong.")
        input("Tekan Enter untuk melanjutkan...")
        return
    
    print(f"\n⚠️ PERINGATAN: Anda akan menghapus {len(recycle_bin)} item secara permanen!")
    konfirmasi = input("Yakin ingin mengosongkan Recycle Bin? (y/n): ").strip().lower()
    
    if konfirmasi in ['y', 'yes', 'ya']:
        recycle_bin.clear()
        print("\n✅ Recycle Bin telah dikosongkan secara permanen!")
    else:
        print("\n❌ Pengosongan Recycle Bin dibatalkan.")
    
    input("Tekan Enter untuk melanjutkan...")

def laporan_penjualan():
    # Fungsi untuk menampilkan laporan penjualan
    clear_screen()
    tampilkan_header()
    print("\n📊 LAPORAN PENJUALAN:")
    
    if not data_penjualan:
        print("\n❌ Belum ada transaksi penjualan.")
        input("Tekan Enter untuk kembali...")
        return
    
    headers = ["No. Transaksi", "ID Barang", "Nama Barang", "Kategori", "Jumlah", "Harga Satuan", "Total"]
    table_data = []
    total_keseluruhan = 0
    
    for transaksi in data_penjualan:
        table_data.append([
            transaksi['no_transaksi'],
            transaksi['id_barang'],
            transaksi['nama_barang'],
            transaksi['kategori'],
            transaksi['jumlah'],
            f"Rp {transaksi['harga_satuan']:,}",
            f"Rp {transaksi['total_harga']:,}"
        ])
        total_keseluruhan += transaksi['total_harga']
    
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\n💰 TOTAL PENJUALAN KESELURUHAN: Rp {total_keseluruhan:,}")
    print(f"📈 JUMLAH TRANSAKSI: {len(data_penjualan)} transaksi")
    
    input("\nTekan Enter untuk kembali...")

def proses_pembayaran(total_harga):
    # Fungsi untuk memproses pembayaran dan kembalian
    print(f"\n💳 PROSES PEMBAYARAN")
    print(f"💰 Total yang harus dibayar: Rp {total_harga:,}")
    print("-" * 50)
    
    while True:
        try:
            uang_bayar = int(input("💵 Masukkan jumlah uang yang dibayarkan: Rp "))
            
            if uang_bayar < 0:
                print("❌ Jumlah uang tidak boleh negatif!")
                continue
            elif uang_bayar < total_harga:
                kekurangan = total_harga - uang_bayar
                print(f"❌ Uang tidak cukup! Kekurangan: Rp {kekurangan:,}")
                
                ulang = input("Coba lagi? (y/n): ").strip().lower()
                if ulang not in ['y', 'yes', 'ya']:
                    return False
                continue
            else:
                kembalian = uang_bayar - total_harga
                
                print(f"\n✅ PEMBAYARAN BERHASIL!")
                print("-" * 30)
                print(f"💰 Total belanja    : Rp {total_harga:,}")
                print(f"💵 Uang diterima    : Rp {uang_bayar:,}")
                print(f"💸 Kembalian        : Rp {kembalian:,}")
                print("-" * 30)
                
                if kembalian > 0:
                    print(f"🔄 Berikan kembalian: Rp {kembalian:,}")
                else:
                    print("✨ Pembayaran pas! Tidak ada kembalian.")
                
                return True
                
        except ValueError:
            print("❌ Input harus berupa angka!")
            ulang = input("Coba lagi? (y/n): ").strip().lower()
            if ulang not in ['y', 'yes', 'ya']:
                return False

def tampilkan_detail_barang(barang):
    # Fungsi untuk menampilkan detail barang
    print("-" * 50)
    print(f"ID           : {barang['id']}")
    print(f"Nama Barang  : {barang['nama']}")
    print(f"Kategori     : {barang['kategori']}")
    print(f"Harga        : Rp {barang['harga']:,}")
    print(f"Stok         : {barang['stok']} unit")
    print(f"Supplier     : {barang['supplier']}")
    print("-" * 50)

# Program utama
if __name__ == "__main__":
    print("🌿 Selamat datang di Toko Jamu Mas Al! 🌿")
    main_menu()