Nama=input("masukan nama lengkap anda: ").lower().strip().title()
user=input("masukan username anda: ").lower().strip()

while len(user)<6 or len(user)>12 or not user.isalpha():
     if not user.isalpha():
            print("Username hanya boleh mengandung huruf")
     elif len(user)<6 :
            print("Username terlalu pendek")
     elif len(user)>12:
            print("Username terlalu panjang")
     user=input("masukan username anda: ").lower().strip()

kode=user[:3].upper() + "-" + str(len(user))
profile= Nama.lower().replace(" ", "-")

print("===Akun Smart Locker===")
print(f"Nama: {Nama}")
print(f"Username: {user}")
print(f"Kode: {kode}")
print(f"Profile Slug: {profile}")
print("Status: Username valid")
