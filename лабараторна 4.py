# Патерн Composite
class MenuComponent:
    def show(self):
        pass

class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"- {self.name}")

class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: MenuComponent):
        self.items.append(component)

    def show(self):
        print(f"{self.name}:")
        for item in self.items:
            item.show()

# Патерн Facade
class RestaurantFacade:
    def __init__(self):
        self.main_menu = Menu("Main Menu")
        pizza_menu = Menu("Pizza")
        pizza_menu.add(MenuItem("Margherita"))
        pizza_menu.add(MenuItem("Pepperoni"))
        drink_menu = Menu("Drinks")
        drink_menu.add(MenuItem("Water"))
        drink_menu.add(MenuItem("Cola"))
        self.main_menu.add(pizza_menu)
        self.main_menu.add(drink_menu)

    def show_menu(self):
        self.main_menu.show()

# Основна програма
if __name__ == "__main__":
    restaurant = RestaurantFacade()
    restaurant.show_menu()
