class Shotgun():
    dv = 0
    acc = 0
    def __init__(self, Acc, Dv):
        self.dv = Dv
        self.acc = Acc
    def getstats(self):
        return self.dv, self.acc
    def setstats(self, Acc, Dv):
        self.dv = Dv
        self.acc = Acc