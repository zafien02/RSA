# ==========================================
# IMPLEMENTASI ALGORITMA RSA (FROM SCRATCH)
# ==========================================

def gcd(a, b):
    """Fungsi mencari Faktor Persekutuan Terbesar (FPB)"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Fungsi mencari modular multiplicative inverse (d)"""
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Mod inverse tidak ditemukan")

def generate_keypair(p, q):
    """Fungsi Pembangkitan Kunci RSA"""
    if not (p != q):
        raise ValueError("p dan q tidak boleh sama")
    
    # 1. Hitung n
    n = p * q
    
    # 2. Hitung Totient Euler (phi)
    phi = (p - 1) * (q - 1)
    
    # 3. Pilih e (Public Key exponent)
    # Biasanya e dipilih bilangan prima kecil, kita mulai dari 3
    e = 3
    while gcd(e, phi) != 1:
        e += 2 # Cari nilai ganjil berikutnya yang coprime dengan phi
        
    # 4. Hitung d (Private Key exponent)
    d = mod_inverse(e, phi)
    
    # Return (Public Key, Private Key)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Fungsi Enkripsi mengubah Teks -> Ciphertext (Angka)"""
    e, n = public_key
    print(f"  [ENKRIPSI] Menggunakan Public Key (e={e}, n={n})")
    
    cipher_angka = []
    for char in plaintext:
        # Konversi karakter ke ASCII
        m = ord(char)
        # Rumus: C = (M^e) mod n
        c = pow(m, e, n)
        cipher_angka.append(c)
        print(f"    '{char}' (ASCII: {m}) -> Enkripsi -> {c}")
        
    return cipher_angka

def decrypt(private_key, ciphertext):
    """Fungsi Dekripsi mengembalikan Ciphertext -> Teks Asli"""
    d, n = private_key
    print(f"  [DEKRIPSI] Menggunakan Private Key (d={d}, n={n})")
    
    plain_text = ""
    for c in ciphertext:
        # Rumus: M = (C^d) mod n
        m = pow(c, d, n)
        # Konversi angka ASCII kembali ke karakter
        char = chr(m)
        plain_text += char
        print(f"    Cipher {c} -> Dekripsi (ASCII: {m}) -> '{char}'")
        
    return plain_text

# ================= BAGIAN DEMO =================
if __name__ == '__main__':
    print("=== SIMULASI ALGORITMA RSA ===")
    
    # 1. Setup Bilangan Prima (Dalam dunia nyata angkanya sangat besar)
    # Gunakan bilangan prima kecil agar mudah didemonstrasikan
    p = 61
    q = 53
    print(f"\n1. Tahap Key Generation:")
    print(f"   Bilangan prima p = {p}, q = {q}")
    
    public_key, private_key = generate_keypair(p, q)
    print(f"   => KUNCI PUBLIK (e, n) : {public_key}")
    print(f"   => KUNCI PRIVAT (d, n) : {private_key}")
    
    # 2. Pesan yang ingin dikirim
    pesan_asli = "KAMPUS"
    print(f"\n2. Pesan Asli (Plaintext): {pesan_asli}")
    
    # 3. Proses Enkripsi
    print("\n3. PROSES ENKRIPSI:")
    ciphertext = encrypt(public_key, pesan_asli)
    print(f"\n>> HASIL ENKRIPSI (Ciphertext): {ciphertext}")
    
    # 4. Proses Dekripsi
    print("\n=============================================")
    print("\n4. PROSES DEKRIPSI:")
    hasil_dekripsi = decrypt(private_key, ciphertext)
    print(f"\n>> HASIL DEKRIPSI: {hasil_dekripsi}")