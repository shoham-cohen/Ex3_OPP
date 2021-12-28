
class EdgeData:
    src = 0
    w = 0.0
    des = 0

    def __init__(self, src, w, des):
        self.src = src
        self.w = w
        self.des = des

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.des


    def getWeight(self):
        return self.w
