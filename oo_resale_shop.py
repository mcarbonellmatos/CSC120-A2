class ResaleShop:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, price: int, operating_system: str, description: str, processor_type: str, hard_drive_capacity: int, memory: int, year_made: int):
        self.price = price
        self.operating_system = operating_system
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.year_made = year_made

    # What methods will you need?
    
    def update_computers_price(self, updatePrice: int):
        self.price = updatePrice
        print("Price has been updated to: ", self.price)

    def store_inventory(self, newInventory: str):
        if 
        return {
            'description':self.description,
            'processor_type':self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price
        }


    def buy_computer(self, addInventory, price: int, operating_system: str, description: str, processor_type: str, hard_drive_capacity: int, memory: int, year_made: int):
        self.Computer() = addInventory
        


    def sell_computer(self):

    def refurbrish_computer(self):
    
