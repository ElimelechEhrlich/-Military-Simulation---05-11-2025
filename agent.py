from unit import *
from soulder import *

class Agent:
    total_agents = 0
    def __init__(self, code_name:str, clearance_level:int):
        self.code_name = code_name
        self.clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        return f'Agent: {self.code_name}. Clearance Level: {self.clearance_level}'


class Mission:
    def __init__(self, mission_name:str, target:str,unit:Unit, assigned_agent:Agent):
        self.mission_name = mission_name
        self.target = target
        self.unit = unit
        self.assigned_agent = assigned_agent
    
    def execute(self):
        return Unit.attack()

    def brief(self):
        return f'Mission: {self.mission_name}, Target: {self.target}, Agent: {self.assigned_agent.code_name}'
    
class MissionManager:
    missions = []
    def __init__(self):
        pass
    @classmethod
    def add_mission(cls:Mission):
        MissionManager.missions.append(cls.brief())



class ReconMission(Mission):
    def __init__(self, target, unit:Unit, assigned_agent:Soldier):
        super().__init__(mission_name, target, unit, assigned_agent)
        mission_name = 'strike'


class StrikeMission(Mission):
    def __init__(self, target, unit:Unit, assigned_agent:Soldier):
        super().__init__(mission_name, target, unit, assigned_agent)
        mission_name = 'Recon'
    
class RescueMission(Mission):
    def __init__(self, target, unit:Unit, assigned_agent:Soldier):
        super().__init__(mission_name, target, unit, assigned_agent)
        mission_name = 'Rescue'
    
