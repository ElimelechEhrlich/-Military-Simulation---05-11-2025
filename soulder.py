from weapon import Weapon

class Soldier:
    def __init__(self, name:str, rank:str,  weapon:Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def __str__(self):
        return f'name: {self.name}, rank: {self.rank}, weapon: {self.weapon}'

    def report(self):
        return {Soldier.__str__(self)}
