class Bike:
    def __init__(self, bike_id, model, available=True):
        self.bike_id = bike_id
        self.model = model
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Rented"
        return f"ID: {self.bike_id}, Model: {self.model}, Status: {status}"

class BikeRentalSystem:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike_id, model):
        self.bikes.append(Bike(bike_id, model))
        print("✅ Bike added successfully!")

    def display_bikes(self):
        if not self.bikes:
            print("⚠️ No bikes in the system.")
            return
        print("\n🚲 List of Bikes:")
        for bike in self.bikes:
            print(bike)

    def rent_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id and bike.available:
                bike.available = False
                print("✅ Bike rented successfully!")
                return
        print("❌ Bike not available or does not exist.")

    def return_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id and not bike.available:
                bike.available = True
                print("✅ Bike returned successfully!")
                return
        print("❌ Bike not found or was not rented.")

# -------- Main Program --------
def main():
    system = BikeRentalSystem()

    while True:
        print("\n====== Bike Rental System ======")
        print("1. Add Bike")
        print("2. View Bikes")
        print("3. Rent Bike")
        print("4. Return Bike")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            bike_id = input("Enter bike ID: ")
            model = input("Enter bike model: ")
            system.add_bike(bike_id, model)
        elif choice == '2':
            system.display_bikes()
        elif choice == '3':
            bike_id = input("Enter bike ID to rent: ")
            system.rent_bike(bike_id)
        elif choice == '4':
            bike_id = input("Enter bike ID to return: ")
            system.return_bike(bike_id)
        elif choice == '5':
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
