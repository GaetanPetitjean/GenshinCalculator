
from calcul import *

list = ['xp', 'jewels', 'j', 'materials', 'm']
choice = None

while not choice in list:
    choice = input("Choisir le calcul (xp/jewels/materials):")

if choice == list[0]:
        xp_white = int(input("Nb blanc:"))
        xp_blue = int(input("Nb bleu:"))
        xp_purple = int(input("Nb violet:"))

        xp = Experience(xp_white, xp_blue, xp_purple)
        xp.calcul_xp()
        print("Nombre de livre d'experience - Violet:", xp.get_nb_blue(), "/ Bleu:", xp.get_nb_green(), "/ Blanc", xp.get_nb_white())

elif choice == list[1] or choice == list[2]:
        jew_green = int(input("Nb vert:"))
        jew_blue = int(input("Nb bleu:"))
        jew_purple = int(input("Nb violet:"))
        jew_orange = int(input("Nb orange:"))

        jewels = Jewels(jew_green, jew_blue, jew_purple, jew_orange)
        jewels.calcul_jewels()
        print("Nombre de joyaux - Orange:", jewels.get_nb_purple(), "/ Violet:",jewels.get_nb_blue(), "/ Bleu:", jewels.get_nb_green(), "/ Vert:", jewels.get_nb_white())

elif choice == list[3] or list[4] == choice:
        mat_white = int(input("Nb blanc:"))
        mat_green = int(input("Nb vert:"))
        mat_blue = int(input("Nb bleu:"))

        materials = Material(mat_white, mat_green, mat_blue)
        materials.calcul_material()
        print("Nombre de matériaux - Bleu:", materials.get_nb_blue(), "/ Vert:", materials.get_nb_green(), "/ Blanc:", materials.get_nb_white())
