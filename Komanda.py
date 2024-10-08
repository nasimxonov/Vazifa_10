import json

class Komanda:


    def __init__(self, nomi, ishtirokchilari_soni, trener, kapitani):

        self.nomi = nomi
        self.ishtirokchilari_soni = ishtirokchilari_soni
        self.trener = trener
        self.kapitani = kapitani

    def show_info(self):

        print(f"Komanda nomi: {self.nomi}")
        print(f"Ishtirokchilar soni: {self.ishtirokchilari_soni}")
        print(f"Trener: {self.trener}")
        print(f"Kapitan: {self.kapitani}")
        print("---------------------------")

def saralab_chiqarish(komandalar):

    komandalar = sorted(komandalar, key=lambda x: x.nomi)
    print("Komandalar nomi bo'yicha saralangan:")
    for komanda in komandalar:
        komanda.show_info()

def bormi(komandalar, new_komanda):

    for komanda in komandalar:
        if komanda.nomi == new_komanda:
            print(f"Komanda '{new_komanda}' mavjud:")
            komanda.show_info()
            return
    print(f"Bunday komanda yo'q: '{new_komanda}'")

def jsondan_load(filename):

    with open(filename, 'r') as file:
        data = json.load(file)
        komandalar = [Komanda(**komanda) for komanda in data]
    return komandalar

komandalar = jsondan_load('kommanda.json')

saralab_chiqarish(komandalar)

new_komanda = input("Komanda nomini kiriting: ")
bormi(komandalar, new_komanda)
