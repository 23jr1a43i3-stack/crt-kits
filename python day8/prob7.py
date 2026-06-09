class Ride:
    def fare(self):
        print("Fare: ₹100")

class LuxuryRide(Ride):
    def fare(self):
        print("Fare: ₹300")

ride = LuxuryRide()
ride.fare()