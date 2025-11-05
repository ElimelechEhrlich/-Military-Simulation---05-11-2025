from abc import ABC, abstractmethod

class StrikeOption(ABC):
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
    @abstractmethod
    def strike(self):
        pass

class Tank(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: Shell firing'
        else:
            return 'Out of ammo'
    
class Rifle(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: shooting with rifle'
        else:
            return 'Out of ammo'
    
class SniperRifle(StrikeOption):
    def strike(self):
        if self.ammo < 0:
            self.ammo -= 1
            return f'strike: shooting with sniper rifle'
        else:
            return 'Out of ammo'


