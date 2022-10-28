# inport module math
from ctypes import FormatError
import math
from platform import java_ver

# Variable JariJari menampung nilai input yang dimasukan berupa string
JariJari = input('Masukan Jari-Jari lingkaran;')

"""

rumus Luas & Keliling Lingkaran
_________________________________

Luas            = phi * r^2 

Keliling        = 2 * phi * r
_________________________________

"""

# conver string to intege
JariJari = int(JariJari)

# Hitung Luas Lingkaran
Luas = math.pi * (JariJari * JariJari)

# Hitung Luas Keliling
Keliling = 2 * math.pi * JariJari

# output Luas & Keliling Lingkaran
# .2f => Mengambil 2 angka setelah (,)
print("Berikut Luas Lingkaran - ", format(Luas, '.2f'))
print("Berikut luas Keliling Lingkaran = ", format(Keliling, '.2f'))