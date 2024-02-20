class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def showdata(self):
        print('Nama:', self.nama)
        print('Umur:', self.umur)

# obj
        
budi = manusia('Budi', 20)

budi.showdata()