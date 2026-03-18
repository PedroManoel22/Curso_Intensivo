class Restaurant:
    number_total = 0

    def __init__(
        self,
        restaurant_name: str,
        cuisine_type: str,
        number_served: int = 0,
        open: bool = False,
    ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self._number_served = number_served
        self.open = open
        self.number_total += number_served

    @property
    def number_served(self) -> int:
        return self._number_served

    @number_served.setter
    def number_served(self, new: int) -> None:
        self._number_served = new

    def describe_restaurant(self):
        print(f"\nName: {self.restaurant_name}\ntype: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"\n\033[1;32mThe restaurant {self.restaurant_name} is open!\033[m")
        self.open = True

    def set_number_served(self, new_number: int):
        if self.open:
            self._number_served = new_number
            print(f"Updated list of served clients: {self._number_served}")

        else:
            print("\n\033[1;31mThe retaurant is closed!\033[m\n")
            print("It cannot serve any more customers\n")

    def increment_number_served(self):
        self.number_total += self.number_served
        print(f"\n{self.number_total} customers served today!")


if __name__ == "__main__":
    restaurant = Restaurant("Pedro`s bar", "Comida nordestina", 15)
    restaurant.open_restaurant()
    print(restaurant.number_served)
    restaurant.set_number_served(2)
    print(restaurant.number_served)
    restaurant.increment_number_served()
