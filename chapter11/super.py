class vehicle:
    def __init__(self,vehicle_type):
        print("I am a vehicle")
        self.veicle_type="Car"

class car(vehicle):

    def __init__(self,vehicle_type,brand):
        super().__init__(vehicle_type)
        print("I am a car")
        self.brand=brand

class model(car):
    def __init__(self,vehivle_type,brand,model):
        super().__init__(vehivle_type,brand)
        print("I am a model")
        self.model=model

    def get_details(self):
        print(f"Vehicle Type: {self.veicle_type}, Brand: {self.brand}, Model: {self.model}")

honda=model("Car","Honda","Civic")
honda.get_details()