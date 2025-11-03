class Agent:
    def __init__(self, code_name:str, clearance_lavel:int):
        self.code_name = code_name
        self.clearance_lavel = clearance_lavel

    def report(self):
        print (f"Agent: {self.code_name} reporting. clearance Lavel: {self.clearance_lavel}")

agent1 = Agent("ben", 1)

class Mission:
    def __init__(self, mission_name:str, target_loction:str, assigned_agent:Agent):
        self.mission_name = mission_name
        self.target_loction = target_loction
        self.assigned_agent = assigned_agent

    def assigned_agent(self, assigned_agent):
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"missiom: {self.mission_name}, Target_loction: {self.target_loction}, Agent: {self.assigned_agent.code_name}")

mission1 = Mission("cath", "london")
mission1.breif()
