class ParkingSystem:
    cap = {}
    now = {}
    def __init__(self, big, medium, small):
        self.cap[3] = small
        self.cap[2] = medium
        self.cap[1] = big
        self.now[1] = 0
        self.now[2] = 0
        self.now[3] = 0
    def addCar(self, carType):
        if self.now[carType] < self.cap[carType]:
            self.now[carType] += 1
            return True
        else:
            return False
