# 1) Kullanıcıdan yarıçapı al (string olarak)
my_radius = input("Yarıçapı girin: ")

# 2) my_radius'in tipini göster (string olduğunu gör)
print("my_radius değişkeninin tipi:", type(my_radius))

# 3) String'i float'a çevir ve yeni değişkene ata
my_radius_float = float(my_radius)

# 4) Yeni değişkenin tipini göster (float olduğunu gör)
print("my_radius_float değişkeninin tipi:", type(my_radius_float))

# 5) Yarıçapın karesini hesapla
rkare = my_radius_float ** 2

# 6) Alanı hesapla (pi = 3.1416 kullanılarak)
area = 3.1416 * rkare

# 7) Sonucu f-string ile virgülden sonra 2 basamak göstererek yazdır
print(f"Yarıçapı {my_radius_float} olan çemberin alanı: {area:.2f}")
