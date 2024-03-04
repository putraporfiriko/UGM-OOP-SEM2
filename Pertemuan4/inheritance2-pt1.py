# classes
class orang():
    def __init__(self, nd:str, nb:str, id:int):
        self.namadepan = nd
        self.namabelakang = nb
        self.nomorid = str(id)

class mahasiswa(orang):
    jenjanglist = ("SARJANA","MASTER","DOKTOR")

    def __init__(self, nd, nb, id, lv): # inheritance method 1: all attr
        super().__init__(nd, nb, id)
        self.jenjang = lv
        self.matkul = []

    def enrol(self, mkname):
        self.matkul.insert(mkname)

class karyawan(orang):
    statuslist = ("PERMANENT", "NONPERMANENT")

    def __init__(self, nd: str, nb: str, id: int, sk):
        super().__init__(nd, nb, id)
        self.statuskaryawan = sk

class dosen(karyawan):
    def __init__(self, nd: str, nb: str, id: int, sk, **kwargs):
        super().__init__(nd, nb, id, sk, **kwargs)
        self.matkul_diajar = []
    
    def addmk(self, mkname):
        self.matkul_diajar.insert(mkname)
    
class pelajar():
    def __init__(self):
        self.matkul = []

    def enrol(self, mkname):
        self.matkul.insert(mkname)

class pengajar():
    def __init__(self):
        self.matkul_diajar = []

    def addmk(self, mkname):
        self.matkul_diajar.insert(mkname)

class asdos(orang, pelajar, pengajar):
    def __init__(self, nd: str, nb: str, id: int):
        super().__init__(nd, nb, id)

# objects
bowo = mahasiswa("Bowo", "Nugroho", 987654, mahasiswa.jenjanglist[0])
rizki = dosen("Rizki", "Setiabudi", 456789, karyawan.statuslist[0])
uswatun = asdos("Uswatun", "Hasanah", 456456)

# method calls
bowo.enrol("Basis Data")
rizki.addmk("Statistik")
uswatun.enrol("Big Data")
uswatun.addmk("Kecerdasan Artifisial")
