# 1st task 
        

with open("./students_record.txt", "r") as f:
    lines = f.readlines()
    grade = []
    
    for line in lines:
        line = line.strip()

        if not line or ',' not in line :
            continue
            
        
        name, grades = line.split(',')
        name = name.strip()
        grades = grades.strip()
        
        try:
            grade.append(float(grades))
        except ValueError:
            print(f"Invalid grade for {name}: '{grades}' — skipping this record.")
    
    if grade:
        avg = sum(grade) / len(grade)
        print(f"Average grades are: {avg:.2f}")
    else:
        print("No valid grades found.")


# Base class
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Vehicle Info: {self.year} {self.make} {self.model}")

#     def start_engine(self):
#         print("Engine started.")


# # Derived class: Car
# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors):
#         super().__init__(make, model, year)
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info()
#         print(f"Number of doors: {self.num_doors}")

#     def accelerate(self):
#         print("Car is accelerating!")


# # Derived class: Truck
# class Truck(Vehicle):
#     def __init__(self, make, model, year, cargo_capacity):
#         super().__init__(make, model, year)
#         self.cargo_capacity = cargo_capacity

#     def display_info(self):
#         super().display_info()
#         print(f"Cargo capacity: {self.cargo_capacity} tons")

#     def load_cargo(self):
#         print("Truck is being loaded with cargo.")

# # Derived class: Motorcycle
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, drive_type):
#         super().__init__(make, model, year)
#         self.drive_type = drive_type

#     def display_info(self):
#         super().display_info()
#         print(f"Drive type: {self.drive_type}")

#     def wheelie(self):
#         print("Motorcycle is performing a wheelie!")


# # Demonstration
# # if __name__ == "__main__":
# car = Car("Toyota", "Corolla", 2022, 4)
# truck = Truck("Volvo", "FH16", 2023, 18)
# bike = Motorcycle("Yamaha", "R15", 2021, "chain drive")

# print("---- Car Details ----")
# car.display_info()
# car.start_engine()
# car.accelerate()

# print("\n---- Truck Details ----")
# truck.display_info()
# truck.start_engine()
# truck.load_cargo()

# print("\n---- Motorcycle Details ----")
# bike.display_info()
# bike.start_engine()
# bike.wheelie()




