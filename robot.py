class Robot:
    # 1. Constructor: sets up the robot's initial name and battery level
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    # 2. Method 1: introduces the robot and shows its current battery
    def introduce_and_status(self):
        print(f"Hello! My name is {self.name}, and I belong to Bob.")
        print(f"My current battery level is {self.battery_level}%.")

    # 3. Method 2: charges the robot safely without going over 100%
    def charge_safely(self, amount):
        if amount <= 0:
            print(f"{self.name}: Please enter a positive charge amount.")
            return

        print(f"Charging {self.name} by {amount}%...")
        self.battery_level += amount

        # Safety check to prevent overcharging
        if self.battery_level > 100:
            self.battery_level = 100
            print(f"Safety stop! {self.name} is fully charged at 100%.")
        else:
            print(f"{self.name}'s battery is now at {self.battery_level}%.")


# 4. Creating the two robot objects
timmy = Robot("Timmy", 45)
tom = Robot("Tom", 80)

# Testing the methods
timmy.introduce_and_status()
timmy.charge_safely(30)

print("---")

tom.introduce_and_status()
tom.charge_safely(40)  # This will trigger the 100% safety limit