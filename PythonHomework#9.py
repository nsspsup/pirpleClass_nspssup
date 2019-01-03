import time, sys

class Vehicle:
    def __init__(self, make, model, year, weight,NeedsMaintenance, TripsSinceMaintenance):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance


    def setMake(self, make):
        self.make = make

    def setModel(self,model):
        self.model = model

    def setYear(self,year):
        self.year = year

    def setWeight(self,weight):
        self.weight = weight

class Cars(Vehicle):
    def __init__(self, make, model, year, weight,NeedsMaintenance = False, TripsSinceMaintenance = 0, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight,NeedsMaintenance , TripsSinceMaintenance)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True

    def stop(self):
        if self.isDriving == True:
            self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 5:
            self.NeedsMaintenance = True

        self.isDriving = False

    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return("make: " + self.make +"\n" + \
               "model: " + self.model + "\n" + \
               "year: " + self.year + "\n" + \
               "weight: " + self.weight + "\n" + \
               "needs maintenance: " + str(self.NeedsMaintenance) + "\n" + \
               "trips since maintenance: " + str(self.TripsSinceMaintenance))

class Planes(Vehicle):
    def __init__(self,make, model, year, weight,NeedsMaintenance = False, TripsSinceMaintenance = 0,isFlying = False):
        Vehicle.__init__(self, make, model, year, weight,NeedsMaintenance , TripsSinceMaintenance)
        self.isFlying = isFlying

    def fly(self):
        if self.NeedsMaintenance == False:
            self.isFlying = True
        else:
            print("no flights possible until repaired!!")
            return False

    def land(self):
        if self.isFlying == True:
            self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 5:
            self.NeedsMaintenance = True


    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return("make: " + self.make +"\n" + \
               "model: " + self.model + "\n" + \
               "year: " + self.year + "\n" + \
               "weight: " + self.weight + "\n" + \
               "needs maintenance: " + str(self.NeedsMaintenance) + "\n" + \
               "trips since maintenance: " + str(self.TripsSinceMaintenance))


Ford_GT = Cars("Ford","GT","1966","1520")
Shelby_GT350 = Cars("Ford","GT350","1966","1470")
DeLorean = Cars("DMCH","DeLorean","1925","1230")
X_Wing = Planes("X-Wing","T-65B" ,"30 ABY","19700")


def menu1():
    print("""
    
    Select your car
    
        CARS:
    -------------    
    1. Ford GT40
    2. Shelby 
    3. DeLorean
    
    4. X-wing
""")
    choice = int(input(">>>: "))
    if choice == 1:
        selectedCar = "Ford_GT"
    elif choice == 2:
        selectedCar = "Shelby_GT350"
    elif choice == 3:
        selectedCar = "DeLorean"
    elif choice == 4:
        selectedCar = "X_Wing"
    else:
        print("invalid choice")
        menu1()

    menu2(selectedCar)

def menu2(selectedCar):
    print("""
        ACTIONS:
    -------------    
    5. Drive
    6. Stop
    7. Repair
    8. Car Info
    
    9. Exit Up
""")

    choice = int(input(">>>: "))


    if choice == 5:
        if selectedCar == "X_Wing":
            eval(selectedCar).fly()
            menu2(selectedCar)
        else:
            eval(selectedCar).drive()
            menu2(selectedCar)
    elif choice == 6:
        if selectedCar == "X_Wing":
            eval(selectedCar).land()
            menu2(selectedCar)
        else:
            eval(selectedCar).stop()
            menu2(selectedCar)
    elif choice == 7:
        eval(selectedCar).repair()
        menu2(selectedCar)
    elif choice == 8:
        print(eval(selectedCar))
        time.sleep(2)
        menu2(selectedCar)
    elif choice == 9:
        menu1()
    else:
        print("invalid choice")
        menu2(selectedCar)
        time.sleep(1)

while True:
    menu1()




