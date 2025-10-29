class Item:

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"name: {self.name}, weight: {self.weight}, value: {self.value}"

    def describe(self):
        return f"{self.name} (W:{self.weight}, V:{self.value})"


class Weapon(Item):

    def __init__(self, name, weight, value, damage):
        self.damage = damage
        super().__init__(name, weight, value)

    def describe(self):
        return f"{super().describe()}, Damage: {self.damage}"


class Potion(Item):
    def __init__(self, name, weight, value, effect):
        self.effect = effect
        super().__init__(name, weight, value)

    def describe(self):
        return f"{super().describe()}, Effect: {self.effect}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items.remove(item_name)

    def total_weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        return total_weight

    def total_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.value
        return total_value

    def show_inventory(self):
        for item in self.items:
            print(item.describe())


class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = Inventory()

    def pick_item(self, item):
        self.inventory.add_item(item)

    def use_potion(self, effect):
        for item in self.inventory.items:
            if isinstance(item, Potion) and item.effect == effect:
                print(f"{self.name} used {item.name} and {item.effect}")
                self.inventory.remove_item(item)
                return True
        print(f"No potion with effect '{effect}' found")
        return False

    def attack(self):
        for item in self.inventory.items:
            if isinstance(item, Weapon):
                print(f"Item damage: {item.damage}")

    def __str__(self):
        return f"Player: {self.name} | Health: {self.health} | Inventory Items: {len(self.inventory.items)}"


sword = Weapon("Iron Sword", 10, 150, 35)
potion = Potion("Health Potion", 1, 50, "restore health")

player = Player("Archer", 100)
player.pick_item(sword)
player.pick_item(potion)

player.inventory.show_inventory()
# Output: lists both items with details

player.use_potion("restore health")
player.attack()
player.inventory.show_inventory()