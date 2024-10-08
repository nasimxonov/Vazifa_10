class Order:

    def __init__(self, order_id):

        self.order_id = order_id

    def show_order(self):
        
        print(f"Buyurtma ID: {self.order_id}")


class FoodOrder(Order):


    def __init__(self, order_id, food_name, quantity):

        super().__init__(order_id)
        self.food_name = food_name
        self.quantity = quantity

    def show_food_order(self):

        print(f"Buyurtma ID: {self.order_id}, Taom: {self.food_name}, Miqdori: {self.quantity}")


class DrinkOrder(Order):

    def __init__(self, order_id, drink_name, volume):
        super().__init__(order_id)
        self.drink_name = drink_name
        self.volume = volume

    def show_drink_order(self):

        print(f"Buyurtma ID: {self.order_id}, Ichimlik: {self.drink_name}, Hajmi: {self.volume} ml")


food_order = FoodOrder(1, "Lag'mon", 2)
food_order.show_order()
food_order.show_food_order()

drink_order = DrinkOrder(2, "Choy", 500)
drink_order.show_order()
drink_order.show_drink_order()
