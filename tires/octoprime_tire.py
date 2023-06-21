from tires import Tire

class OctoprimeTires(Tire):
    def __init__(self, tires):
        self.tires = tires
    
    def needs_service(self):
        sum = 0
        for tire in self.tires:
            sum += tire
            
        if sum >= 3:
            return True
        return False

