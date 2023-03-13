class Menu:
    def choice_menu(self):
        Menu = open(r'C:\Users\Ofh\Desktop\PizzaOrder\Menu.txt', 'r')
        for line in Menu.readlines():
            print(line, end='')
        Menu.close()

    def choice_the_compenent(self):
        Malzeme = open(r'C:\Users\Ofh\Desktop\PizzaOrder\Malzeme.txt', 'r')
        for line in Malzeme.readlines():
            print(line, end='')
        Malzeme.close()