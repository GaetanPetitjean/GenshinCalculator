
class Inventory():
    def __init__(self, nb_white, nb_green, nb_blue,):
        self.nb_white = nb_white
        self.nb_green = nb_green
        self.nb_blue = nb_blue

    def get_nb_white(self):
        return self.nb_white

    def get_nb_green(self):
        return self.nb_green

    def get_nb_blue(self):
        return self.nb_blue

class Experience(Inventory):
    def __init__(self, nb_white, nb_green, nb_blue):
        super().__init__(nb_white, nb_green, nb_blue)

    def calcul_xp(self):
        while self.nb_white >= 5:
            self.nb_white -= 5
            self.nb_green += 1

        while self.nb_green >= 4:
            self.nb_green -= 4
            self.nb_blue += 1

class Material(Inventory):
    def __init__(self, nb_white, nb_green, nb_blue):
        super().__init__(nb_white, nb_green, nb_blue)

    def calcul_material(self):
        while self.nb_white >= 3:
            self.nb_white -= 3
            self.nb_green += 1

        while self.nb_green >= 3:
            self.nb_green -= 3
            self.nb_blue += 1

class Jewels(Inventory):
    def __init__(self, nb_white, nb_green, nb_blue, nb_purple):
        super().__init__(nb_white, nb_green, nb_blue)
        self.nb_purple = nb_purple

    def calcul_jewels(self):
        while self.nb_white >= 3:
            self.nb_white -= 3
            self.nb_green += 1

        while self.nb_green >= 3:
            self.nb_green -= 3
            self.nb_blue += 1

        while self.nb_blue >= 3:
                self.nb_blue -= 3
                self.nb_purple += 1

    def get_nb_purple(self):
        return self.nb_purple