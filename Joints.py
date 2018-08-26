class Coord:

    def __init__(self,data):
        self.X = data[0]
        self.Y = data[1]
        self.Z = data[2]

    def getXYZ(self):
        return (self.X,self.Y,self.Z)