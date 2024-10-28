class Shaxs:
    def __init__(self, ism, yosh, jins):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins

    def get_info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Jins: {self.jins}"


class Professor(Shaxs):
    def __init__(self, ism, yosh, jins, fan, daraja):
        super().__init__(ism, yosh, jins)
        self.fan = fan
        self.daraja = daraja

    def get_info(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Fan: {self.fan}, Ilmiy daraja: {self.daraja}"

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, jins, login, email):
        super().__init__(ism, yosh, jins)
        self.login = login
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.ism}, Login: {self.login}, Email: {self.email}"



class Mijoz(Shaxs):
    def __init__(self, ism, yosh, jins, mijoz_id, xarid_soni):
        super().__init__(ism, yosh, jins)
        self.mijoz_id = mijoz_id
        self.xarid_soni = xarid_soni

    def get_info(self):
        return f"Mijoz: {self.ism}, ID: {self.mijoz_id}, Xaridlar soni: {self.xarid_soni}"

class Admin(Foydalanuvchi):
    def __init__(self, ism, yosh, jins, login, email, admin_daraja_bali):
        super().__init__(ism, yosh, jins, login, email)
        self.admin_daraja = admin_daraja_bali

    def get_info(self):
        return f"Admin: {self.ism}, Login: {self.login}, Email: {self.email}, Admin darajasi: {self.admin_daraja}"

    def ban_user(self):
        print("Foydalanuvchi bloklandi")



professor = Professor("Azamat", 45, "Erkak", "iqtisod", "Magistrant")
foydalanuvchi = Foydalanuvchi("Iroda", 39, "Ayol", "Iroda1979", "matkarimova6825@mail.com")
mijoz = Mijoz("Munisa", 21, "Ayol", "M007", 20)
admin = Admin("Azizbek", 18, "Erkak", "admin_az1zbek", "admin@az1ik.com", 5)

print(professor.get_info())
print(foydalanuvchi.get_info())
print(mijoz.get_info())
print(admin.get_info())


admin.ban_user()
