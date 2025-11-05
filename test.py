from abc import ABC, abstractmethod

class  Weapon:
    total_weapons = 0
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1
    def __str__(self):
        return str({f'name: {self.name}, ammo: {self.ammo}'})

class Soldier:
    def __init__(self, name:str, rank:str,  weapon:Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def __str__(self):
        return f'name: {self.name}, rank: {self.rank}, weapon: {self.weapon}'

    def report(self):
        return {Soldier.__str__(self)}

class StrikeOption(ABC):
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
    @abstractmethod
    def strike(self):
        pass

class Tank(StrikeOption):
    def strike(self):
        return f'strike: Shell firing'
    
class Drone(StrikeOption):
    def strike(self):
        return f'strike: Stray Weapon'
    
class Unit:
    def __init__(self, unit_name:str, StrikeOption:StrikeOption ,commander:Soldier, soldiers:list[Soldier]):
        self.unit_name = unit_name
        self.StrikeOption = StrikeOption
        self.commander = commander
        self.soldiers = soldiers

    def briefing(self):
        return f'unit name: {self.unit_name}, Strike Option: {self.StrikeOption.name}, commander details: {self.commander.report()}'      
    

    

w1 = Weapon('TAR-21', 10)
w2 = Weapon('TAR-22', 15)

s1 = Soldier('meir', 'seren', w1)
s2 = Soldier('avi', 'turay', w2)
s3 = Soldier('eli', 'turay', w2)
s4 = Soldier('beni', 'turay', w1)
soldiers = [s2, s3, s4]

strike1 = Tank('Tank', 20)
strike2 = Drone('Drone', 20)

hshiryon = Unit('hshiryon', strike1 , s1 , soldiers)
unit888 = Unit('888', strike2 , s1 , soldiers)

units = [hshiryon, unit888]
for unit in units:
    print (unit.briefing())



        

        