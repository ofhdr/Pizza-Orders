from Pizza import Pizza


# The superclass is created and uses the properties of the pizza class.
class Decorator(Pizza):
    def __init__(self):
        pass


class Olive(Decorator):
    @staticmethod
    def OliveDesc():
        return Pizza.get_description(Pizza, "Olive")

    @staticmethod
    def OliveCost():
        return Pizza.get_cost(Pizza, 4)


class Mushroom(Decorator):
    @staticmethod
    def MushroomDesc():
        return Pizza.get_description(Pizza, "Mushroom")

    @staticmethod
    def MushroomCost():
        return Pizza.get_cost(Pizza, 3)


class Cheese(Decorator):
    @staticmethod
    def CheeseDesc():
        return Pizza.get_description(Pizza, "Cheese")

    @staticmethod
    def CheeseCost():
        return Pizza.get_cost(Pizza, 5)


class Sausage(Decorator):
    @staticmethod
    def SausageDesc():
        return Pizza.get_description(Pizza, "Sausage")

    @staticmethod
    def SausageCost():
        return Pizza.get_cost(Pizza, 9)


class Onion(Decorator):
    @staticmethod
    def OnionDesc():
        return Pizza.get_description(Pizza, "Onion")

    @staticmethod
    def OnionCost():
        return Pizza.get_cost(Pizza, 3)


class Sweetcorn(Decorator):
    @staticmethod
    def SweetcornDesc():
        return Pizza.get_description(Pizza, "Sweetcorn")

    @staticmethod
    def SweetcornCost():
        return Pizza.get_cost(Pizza, 2)


class Nothing(Decorator):
    @staticmethod
    def NothingDesc():
        return Pizza.get_description(Pizza, "")

    @staticmethod
    def NothingCost():
        return Pizza.get_cost(Pizza, 0)
