from abc import ABC, abstractmethod
import uuid

class  Weapon:
    total_weapons = 0
    def __init__(self, name:str, ammo:int):
        self.name = name
        self.ammo = ammo
        self.serial_number = uuid.uuid4()
        Weapon.total_weapons += 1
    def __str__(self):
        return str({f'name: {self.name}, ammo: {self.ammo}'})
    def  reload(self, amount):  
        self.ammo += amount


