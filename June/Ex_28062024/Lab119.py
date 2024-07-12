class Car:
    name = None
    model = None
    make = None

    def __init__(self , o_name, o_model, o_make):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def start_engine(self):
        print("Starting a car with name" + self.name)
        print("Starting a car with model" + self.model)
        print("Starting a car with make" + self.make)
    #end of class

lambo = Car("lambo", "V2", "2024")
honda = Car("honda_city", "city", "2022")
lambo.start_engine()
honda.start_engine()
