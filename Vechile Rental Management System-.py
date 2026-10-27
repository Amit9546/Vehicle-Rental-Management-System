###----Vechile Rental Management System----###
class Vehicle:
    def __init__(self,brand,model,rent_per_day):
        self.brand=brand
        self.model=model
        self.rent_per_day=rent_per_day

    def show_details(self):
        print("Brand name = ",self.brand)
        print("Model name = ",self.model)
        print("Per day rent = ",self.rent_per_day)

    def calculate_rent(self,days):
        return self.rent_per_day*days

class Car(Vehicle):
    def __init__(self,brand,model,rent_per_day,seats):
        super().__init__(brand,model,rent_per_day)
        self.seats=seats

    def show_car_details(self):
        print("Seats : ",self.seats)
   
class Bike(Vehicle):
    def __init__(self,brand,model,rent_per_day,engine_cc):
        super().__init__(brand,model,rent_per_day)
        self.engine_cc=engine_cc
    def show_bike_details(self):
        print("Engine power : ",self.engine_cc)

class LuxuryCar(Car):
    def __init__(self,brand,model,rent_per_day,seats,luxury_charge):
        super().__init__(brand,model,rent_per_day,seats)
        self.luxury_charge=luxury_charge
        print("luxury_charage : ",self.luxury_charge)
    def calculate_rent(self, days):
        normal_rent=self.rent_per_day*days
        luxury_rent=self.luxury_charge*days

        return normal_rent+luxury_rent

#car ka object 
car=Car("Toyota","Fortuner",3000,7)
car2=Car("Tata","nano",5200,4)
print("-----CAR DETAILS-----")
car.show_details()
car2.show_details()
car.show_car_details()
car2.show_car_details()
days=3
print("Rental days : ",days)
print("Total rent : ",car.calculate_rent(days))

#bike ka object
bike=Bike("Bullet","classic 350",1000,"500cc")
print("-----BIKE DETAILS-----")
bike.show_details()
bike.show_bike_details()

days=7
print("Rental days : ",days)
print("Total rent : ",bike.calculate_rent(days))

#luxury car ka object
luxury=LuxuryCar("BMW","X5",8000,5,2000)
print("----LUXURY CAR-----")
luxury.show_details()
luxury.show_car_details()

days=2
print("Rental Days : ",days)
print("Total rent : ",luxury.calculate_rent(days))




       











