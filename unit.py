from abc import ABC, abstractmethod
from strikeoption import StrikeOption, SniperRifle
from soulder import Soldier
from weapon import Weapon
from agent import *

class Unit(ABC):
    def __init__(self, unit_name:str, StrikeOption:StrikeOption ,commander:Soldier, soldiers:list[Soldier]):
        self.unit_name = unit_name
        self.StrikeOption = StrikeOption
        self.commander = commander
        self.soldiers = soldiers
    @abstractmethod
    def attack():
        pass

    def briefing(self):
        return f'unit name: {self.unit_name}, Strike Option: {self.StrikeOption.name}, commander details: {self.commander.report()}'      
    
class TankUnit(Unit):
    def attack(self):
        return 'Shell firing'

class Infantry(Unit):
    def attack(self):
        return 'Get in and start shooting.'
        
class Sniper(Unit):
    def attack(self, target, unit:Unit, assigned_agent:Soldier):
        return 'Identify the target with binoculars and take accurate shots'


w1 = Weapon('TAR-21', 10)
w2 = Weapon('TAR-22', 15)
s1 = Soldier('meir', 'seren', w1)
s2 = Soldier('avi', 'turay', w2)
s3 = Soldier('eli', 'turay', w2)
s4 = Soldier('beni', 'turay', w1)
soldiers = [s2, s3, s4]

a = Weapon('M24', 30)
b = Soldier('Eli', 'seren', a)
c = SniperRifle('shoot', 20)
d = Sniper('eee', c , b , soldiers)

print (d.attack())

