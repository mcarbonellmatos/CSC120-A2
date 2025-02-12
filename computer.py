class Computer:

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

    # What methods/functions will you need based on step 2?

    def update_operating_system(self, updatedOS: str):
        self.operating_system = updatedOS
        print("operating system was updated to: ", self.operating_system)
    
    def pcInformation(self):
        return {
            'description':self.description,
            'processor_type':self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price
        }
    

def main():
    myComputer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    myComputer.update_operating_system("Sequoia 15.3")
    print(myComputer.pcInformation())

main()
