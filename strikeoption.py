from abc import ABC, abstractmethod

class StrikeOption(ABC):
    def __init__(self, name:str, ammo:int, range:str):
        self.name = name
        self.ammo = ammo
        self.range = range
    @abstractmethod
    def strike(self):
        pass

class Tank(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: Shell firing, range: {self.range}'
        else:
            return 'Out of ammo'
    
class Rifle(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: shooting with rifle, range: {self.range}'
        else:
            return 'Out of ammo'
    
class SniperRifle(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: shooting with sniper rifle, range: {self.range}'
        else:
            return 'Out of ammo'


