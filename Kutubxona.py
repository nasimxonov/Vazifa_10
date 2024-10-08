class Kitob:


    def __init__(self, nomi, muallif, janr, narx):

        self.__nomi = nomi
        self.__muallif = muallif
        self.__janr = janr
        self.__narx = narx
    
    def get_nomi(self):
        return self.__nomi

    def get_muallif(self):
        return self.__muallif
    
    def get_janr(self):
        return self.__janr

    def get_narx(self):
        return self.__narx

class Kutubxona:


    def __init__(self):

        self.kitoblar = []
    
    def kitob_qoshish(self, kitob):

        self.kitoblar.append(kitob)
    
    def kitob_ochirish(self, nomi):

        for kitob in self.kitoblar:
            if kitob.get_nomi() == nomi:
                self.kitoblar.remove(kitob)
                return f"{nomi} o'chirildi."
        return f"{nomi} topilmadi."
    
    def kitob_qidirish(self, nomi):

        for kitob in self.kitoblar:
            if kitob.get_nomi() == nomi:
                return kitob
        return f"{nomi} topilmadi."

class Foydalanuvchi:


    def __init__(self, ism, login, parol):

        self.ism = ism
        self.login = login
        self.parol = parol
        self.q_kitoblar = []

    def kitob_olish(self, kutubxona, kitob_nomi):

        kitob = kutubxona.kitob_qidirish(kitob_nomi)
        if isinstance(kitob, Kitob):
            self.q_kitoblar.append(kitob)
            kutubxona.kitob_ochirish(kitob_nomi)
            return f"{kitob_nomi} kitobi qarzga olindi."
        return f"{kitob_nomi} topilmadi."
    
    def kitob_qaytarish(self, kutubxona, kitob_nomi):

        for kitob in self.q_kitoblar:
            if kitob.get_nomi() == kitob_nomi:
                self.q_kitoblar.remove(kitob)
                kutubxona.kitob_qoshish(kitob)
                return f"{kitob_nomi} kitobi qaytarildi."
        return f"{kitob_nomi} sizda yo'q."

class KutubxonaTizimi:


    def __init__(self):

        self.foydalanuvchilar = []
        self.kutubxona = Kutubxona()
    
    def foydalanuvchi_royxatga_olish(self, ism, login, parol):

        foydalanuvchi = Foydalanuvchi(ism, login, parol)
        self.foydalanuvchilar.append(foydalanuvchi)
    
    def tizimga_kirish(self, login, parol):

        for foydalanuvchi in self.foydalanuvchilar:
            if foydalanuvchi.login == login and foydalanuvchi.parol == parol:
                return foydalanuvchi
        return "Login yoki parol xato."

tizim = KutubxonaTizimi()

tizim.foydalanuvchi_royxatga_olish("Ali", "ali123", "parol123")
tizim.foydalanuvchi_royxatga_olish("Vali", "vali456", "parol456")

tizim.kutubxona.kitob_qoshish(Kitob("Sherlock Holms", "Shekspir", "Roman", 15000))
tizim.kutubxona.kitob_qoshish(Kitob("O'tgan kunlar", "Abdulla Qodiriy", "Roman", 20000))


foydalanuvchi = tizim.tizimga_kirish("ali123", "parol123")

if isinstance(foydalanuvchi, Foydalanuvchi):
    print(f"Xush kelibsiz, {foydalanuvchi.ism}!")
    natija = foydalanuvchi.kitob_olish(tizim.kutubxona, "Yulduzli tunlar")
    print(natija)


    natija = foydalanuvchi.kitob_qaytarish(tizim.kutubxona, "Yulduzli tunlar")
    print(natija)


    natija = foydalanuvchi.kitob_olish(tizim.kutubxona, "Sherlock Holms")#agar buyerdagi kiob yoq bolsa topilmadi deydi
    print(natija)

else:
    print(foydalanuvchi) 