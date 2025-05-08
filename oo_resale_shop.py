from computer import Computer
from typing import Optional
class ResaleShop:

    # What attributes will it need?
    inventory: list
    item_id = int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.item_id = 0

    # What methods will you need?

    def buy(self, price: int, operating_system: str, description: str, processor_type: str, hard_drive_capacity: int, memory: int, year_made: int):
        new_computer = Computer(price, operating_system, description, processor_type, hard_drive_capacity, memory, year_made)
        self.item_id +=1
        new_computer.item_id = self.item_id
        self.inventory.append(new_computer)
        return self.inventory.index(new_computer)
    
    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory):
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, " not found. Item can't be sell.")
    
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if 0 <= item_id < len(self.inventory):
            computer = self.inventory[item_id] # locate the computer
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    def print_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("Inevntory unavailable.")
        else: 
            for computer in self.inventory:
                print(computer)

def main():
    computerShop = ResaleShop()

    item_id = computerShop.buy(price = 1100, operating_system = "macOS Big Sur", description = "MacBook Air 15-inch", processor_type = "M3", hard_drive_capacity = 256, memory = 16 , year_made = 2024)
    computerShop.refurbish(item_id, "M4")
    computerShop.sell(item_id)
    
main()
