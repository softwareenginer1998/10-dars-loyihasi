from datetime import datetime

class Dori:
    def __init__(self, nomi, narxi, miqdori, amal_qilish_muddati):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdori = miqdori
        self.amal_qilish_muddati = datetime.strptime(amal_qilish_muddati, '%Y-%m-%d')

    def __repr__(self):
        return f"Dori(nomi='{self.nomi}', narxi={self.narxi}, miqdori={self.miqdori}, amal_qilish_muddati='{self.amal_qilish_muddati.date()}')"


class Dorixona:
    def __init__(self):
        self.dorilar = []

    def dori_qoshish(self, dori):
        self.dorilar.append(dori)

    def dori_ochirish(self, dori_nomi):
        self.dorilar = [dori for dori in self.dorilar if dori.nomi != dori_nomi]

    def miqdorini_yangilash(self, dori_nomi, yangi_miqdor):
        for dori in self.dorilar:
            if dori.nomi == dori_nomi:
                dori.miqdori = yangi_miqdor
                if dori.miqdori < 5:
                    self.ogohlantirish(dori)
                break

    def ogohlantirish(self, dori):
        print(f"Ogohlantirish: '{dori.nomi}' dori miqdori 5 dan kam. Hozirgi miqdori: {dori.miqdori}.")

    def amal_qilish_muddati_tekshirish(self):
        hozir = datetime.now()
        self.dorilar = [dori for dori in self.dorilar if dori.amal_qilish_muddati > hozir]

    def dori_royxati(self):
        return self.dorilar



dorixona = Dorixona()


dorixona.dori_qoshish(Dori('Paracetamol', 5000, 10, '2025-12-31'))
dorixona.dori_qoshish(Dori('Ibuprofen', 7000, 4, '2024-01-01'))
dorixona.dori_qoshish(Dori('Aspirin', 3000, 0, '2023-05-10'))


dorixona.amal_qilish_muddati_tekshirish()


print(dorixona.dori_royxati())


dorixona.miqdorini_yangilash('Paracetamol', 3)


print(dorixona.dori_royxati())
