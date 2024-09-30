class Talaba:
    def __init__(self, ismi, yoshi, kursi):
        self.ismi = ismi
        self.yoshi = yoshi
        self.kursi = kursi
        self.xona = None

    def __str__(self):
        return f"{self.ismi} (Yoshi: {self.yoshi}, Kurs: {self.kursi})"


class Xona:
    def __init__(self, raqami, maksimal_sigim):
        self.raqami = raqami
        self.maksimal_sigim = maksimal_sigim
        self.talabalar = []

    def joylash(self, talaba):
        if len(self.talabalar) < self.maksimal_sigim:
            self.talabalar.append(talaba)
            talaba.xona = self
            return True
        return False

    def bosh_joylar(self):
        return self.maksimal_sigim - len(self.talabalar)

    def __str__(self):
        return f"Xona {self.raqami} (Maksimal sigim: {self.maksimal_sigim}, Hozirgi talaba soni: {len(self.talabalar)})"


class Yotoqxona:
    def __init__(self):
        self.xonalar = []

    def xona_qosh(self, xona):
        self.xonalar.append(xona)

    def talabalarni_joylashtirish(self, talaba):
        for xona in self.xonalar:
            if xona.joylash(talaba):
                print(f"{talaba.ismi} {xona.raqami} xonaga joylashtirildi.")
                return
        print(f"{talaba.ismi} uchun bosh xona topilmadi.")

    def joy_almashtirish(self, talaba, yangi_xona):
        if talaba.xona:
            talaba.xona.talabalar.remove(talaba)
        self.talabalarni_joylashtirish(talaba)

    def statistika(self):
        toliq_xonalar = 0
        bosh_xonalar = 0
        for xona in self.xonalar:
            if xona.bosh_joylar() == 0:
                toliq_xonalar += 1
            else:
                bosh_xonalar += 1
        print(f"Toliq xonalar: {toliq_xonalar}, Bosh xonalar: {bosh_xonalar}")


yotoqxona = Yotoqxona()
xona1 = Xona(101, 3)
xona2 = Xona(102, 2)

yotoqxona.xona_qosh(xona1)
yotoqxona.xona_qosh(xona2)

talaba1 = Talaba("Ali", 19, 2)
talaba2 = Talaba("Sarina", 20, 3)
talaba3 = Talaba("Olim", 21, 1)
talaba4 = Talaba("Durdona", 22, 2)

yotoqxona.talabalarni_joylashtirish(talaba1)
yotoqxona.talabalarni_joylashtirish(talaba2)
yotoqxona.talabalarni_joylashtirish(talaba3)
yotoqxona.talabalarni_joylashtirish(talaba4)

yotoqxona.statistika()
