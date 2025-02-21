# variabel 
nama = 'sodikin'
print(f'nama saya : {nama}')

# function 
def get_nama(nama):
    return nama
print(get_nama('bara '))

# class 
class Orang():
    def __init__(self):
        self._nama = 'sodikin'

    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama
        
# membuat objek 
orang = Orang()
nama = orang.get_nama()
print('orang 1 ', nama)
orang2 = Orang()
orang2.set_nama('Anjasamara')
nama = orang2.get_nama()
print('orang 2 ', nama)