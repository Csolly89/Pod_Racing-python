# object classes for a basic Podracer with max_speed, condition(perfect,trashed, repaired, price)
# define a repair method that will update condition to repaired
# AnakinsPod that inherits Podracer also contains special method called boost... mulitply max_speed by 2
# SebulbasPod inherits PodRacer as well but also has a special method flame_jet, update the condition of another podracer to trashed

class PodRacer:
    def __init__(self,max_speed,condition,price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price 

    def repair(self):
        self.condition = "Like it was brand new"
