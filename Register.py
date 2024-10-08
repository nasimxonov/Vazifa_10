import json

class Register:


    def __init__(self, fullname, email, username, password):

        self.data = self.load_data()
        self.check_duplicates(fullname, email, username)

        self.check_name(fullname)
        self.fullname = fullname

        self.check_email(email)
        self.email = email

        self.check_username(username)
        self.username = username

        self.check_password(password)
        self.password = password

        self.data.append({
            "fullname": self.fullname,
            "email": self.email,
            "username": self.username,
            "password": self.password
        })
        self.save_data()

        print("Yaraldi")

    def load_data(self):
        """Fayldan ma'lumotlarni yuklab oladi."""
        try:
            with open("foydalanuvchilar.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        """Faylga ma'lumotlarni saqlaydi."""
        with open("foydalanuvchilar.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def check_duplicates(self, fullname, email, username):
        """Fullname, email va username oldin kiritilmaganligini tekshiradi."""
        for user in self.data:
            if user['fullname'] == fullname:
                raise Exception("Bu fullname oldin ro'yxatga olingan!")
            if user['email'] == email:
                raise Exception("Bu email oldin ro'yxatga olingan!")
            if user['username'] == username:
                raise Exception("Bu username oldin ro'yxatga olingan!")

    def check_name(self, new_name: str):
        
        if len(new_name.split()) != 4:
            raise Exception("Name Error! Iltimos F.I.Sh ni to'liq kiriting!")

        if not new_name.islower():
            raise Exception("F.I.Sh kichik harf bilan boshlanishi kerak!")

        assert new_name.endswith("o'g'li") or new_name.endswith("qizi"), "F.I.Sh qizi yoki o'g'li bilan tugashi kerak"

    def check_email(self, new_email: str):

        assert "@" in new_email, "@ belgisi bo'lishi kerak!"
        local_part = new_email[:new_email.find("@")]
        assert len(local_part) >= 5, "E-mail uzunligi '@' gacha kamida 5 ta belgi bo'lishi kerak"
        assert new_email.endswith(".com") or new_email.endswith(".ru"), "E-mail '.ru' yoki '.com' bilan tugashi kerak"

    def check_username(self, username: str):

        assert len(username) >= 5, "Username uzunligi kamida 5 ta bo'lishi kerak"
        assert username.isalnum(), "Username faqat raqam va harflardan iborat bo'lishi kerak"

    def check_password(self, password: str):

        assert len(password) >= 8, "Parol uzunligi kamida 8 ta belgi bo'lishi kerak"
        assert password.isalnum(), "Parol faqat harf va raqamlardan iborat bo'lishi kerak"
        assert any(c.isdigit() for c in password), "Parolda kamida bitta raqam bo'lishi kerak"
        assert any(c.isalpha() for c in password), "Parolda kamida bitta harf bo'lishi kerak"


a = Register(input("Fullname: "), input("E-mail: "), input("Username: "), input("Password: "))
