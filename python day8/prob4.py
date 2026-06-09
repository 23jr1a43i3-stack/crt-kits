class Customer:

    def delivery_charge(self):
        print("Delivery Charge: ₹50")

class PrimeCustomer(Customer):

    def delivery_charge(self):
        print("Delivery Charge: ₹20")
if __name__ == "__main__":
    prime_user = PrimeCustomer()
    prime_user.delivery_charge()