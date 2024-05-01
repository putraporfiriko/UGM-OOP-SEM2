from collections import namedtuple

koordinat = namedtuple('koordinat', ['x', 'y'])

titik1 = koordinat(2,4)

#calling using indexes
print(titik1[0], titik1[1])
#calling using attr name
print(titik1.x, titik1.y)
#calling using getattr  
print(getattr(titik1, 'x'), getattr(titik1, 'y'))