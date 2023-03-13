class Pizza:
    def get_cost(self, cost):
        return cost

    def get_description(self, desc):
        return desc


# It forms the subclasses of the pizza class.
class Classic(Pizza):
    def get_cost(self, cost):
        return super().get_cost(cost)

    def get_description(self, description):
        return super().get_description(description)


class Margherita(Pizza):
    def get_cost(self, cost):
        return super().get_cost(cost)

    def get_description(self, description):
        return super().get_description(description)


class BBQ(Pizza):
    def get_cost(self, cost):
        return super().get_cost(cost)

    def get_description(self, description):
        return super().get_description(description)


class FourCheese(Pizza):
    def get_cost(self, cost):
        return super().get_cost(cost)

    def get_description(self, description):
        return super().get_description(description)
