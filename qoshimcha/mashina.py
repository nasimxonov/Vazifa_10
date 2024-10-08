class Car:


    def __init__(self, model):

        self.model = model

    def drive(self):

        print(f"{self.model} harakatlanmoqda.")

    def stop(self):
        
        print(f"{self.model} to'xtadi.")


class SportsCar(Car):


    def __init__(self, model, max_speed):

        super().__init__(model)
        self.max_speed = max_speed

    def accelerate(self):

        print(f"{self.model} tezlashmoqda. Max tezlik: {self.max_speed} km/soat")


class Truck(Car):


    def __init__(self, model, cargo_capacity):

        super().__init__(model)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, cargo_weight):

        if cargo_weight > self.cargo_capacity:
            print(f"{self.model} yuk oshib ketdi max sigadi: {self.cargo_capacity} kg")
        else:
            print(f"{self.model} yuk {cargo_weight} kg tashiyapti")

ferrari = SportsCar("Ferrari", 350)
ferrari.drive()
ferrari.accelerate()
ferrari.stop()

volvo_truck = Truck("Volvo", 10000)
volvo_truck.drive()
volvo_truck.load_cargo(8000)
volvo_truck.stop()

