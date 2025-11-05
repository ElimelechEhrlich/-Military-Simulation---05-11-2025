from unit import *
from strikeoption import *

class Army:
    total_attacks = 0
    def __init__(self, units:list[Unit]):
        self.units = units
        
    def attack_all(self):
        for unit in self.units:
            print (unit.attack())
            Army.total_attacks += 1

strike1 = Tank('Tank', 20, 'madium')
strike2 = Rifle('rifle', 20, 'short')
strike3 = SniperRifle('sniper rifle', 25, 'long')
hshiryon = TankUnit('Hshiryon', strike1 , s1 , soldiers)
golani = Infantry('Golani', strike2 , s1 , soldiers)
golani_sniper = Sniper('Golani', strike2 , s1 , soldiers)

print (Army.total_attacks)
units = [hshiryon, golani, golani_sniper]
attack_all_units = Army(units)
attack_all_units.attack_all()
print (Army.total_attacks)
