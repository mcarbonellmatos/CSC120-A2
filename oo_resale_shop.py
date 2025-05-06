from computer import Computer
class ResaleShop:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.item_id = 0

    # What methods will you need?

    def buy(self, price: int, operating_system: str, description: str, processor_type: str, hard_drive_capacity: int, memory: int, year_made: int):
        new_computer = Computer(price, operating_system, description, processor_type, hard_drive_capacity, memory, year_made)
        self.item_id +=1
        self.inventory.append(new_computer)
        return self.item_id
    
    def update_price(self, item_id: int, new_price int):
        update_price = 
    
    def refurbish(item_id: int, new_os: Optional[str] = None):
        if inventory[item_id] is not None:
            computer = inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
