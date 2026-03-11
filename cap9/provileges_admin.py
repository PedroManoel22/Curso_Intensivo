from user import User


class Admin(User):
    def __init__(self):
        super().__init__()
        self.privileges_admin = [
            "can add post",
            "can delete post",
            "can ban user",
        ]

    def show_privileges(self):
        print("\n---- Privileges Admin ----\n")
        for p in self.privileges_admin:
            print(p)
        print()


class Privileges(Admin):
    def __init__(self, *args):
        super().__init__()
        self.privileges_admin = self.privileges_admin
        self.privileges = args
        for a in self.privileges:
            self.privileges_admin.append(a)

    def show_privileges(self):
        return super().show_privileges()


if __name__ == "__main__":
    new_privileges = Privileges("OI sou novo", "ehhe", "testando")
    new_privileges.show_privileges()

    adm = Admin()
    adm.show_privileges()
