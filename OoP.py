# object classes for a basic Podracer with max_speed, condition(perfect,trashed, repaired, price)
# define a repair method that will update condition to repaired
# AnakinsPod that inherits Podracer also contains special method called boost... mulitply max_speed by 2
# SebulbasPod inherits PodRacer as well but also has a special method flame_jet, update the condition of another podracer to trashed / wasted

# main parent class to which the children will inherit
class PodRacer:
    def __init__(self,max_speed,condition,price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price 

    def repair(self):
        self.condition = "Like it was brand new"

# Anakin is lame name.. we all know he is and always shall be Lord Vader
class VadersPod:
    # dont remember what the none does here on 19... just gonna leave it
    def __init__(self,max_speed,condition,price) -> None:
        # super init brings down the settings of self.max_speed = max_speed etc etc
        super.init(max_speed,condition,price)

    def boost(self):
        self.max_speed *= 2
        print("Use the force Lord Vader")

# Sebulba also inherits from Podracer 
class SebulbasPod:
    def __init__(self,max_speed,condition,price) -> None:
        # super init brings down the settings of self.max_speed = max_speed etc etc
        super.init(max_speed,condition,price)

    def flame_jet(self):
        PodRacer.shared_condition = "Wasted"
        print("I have the highground Anakin")
