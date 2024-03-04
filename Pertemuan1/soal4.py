## pip install sympy

import sympy as sp

num = int(input("input angka: "))

flag = sp.isprime(num)

if flag == True:
    print("Angka Primer")
else:
    print("Bukan Angka Primer")