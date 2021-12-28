from Ex3.position import position
from Ex3.EdgeData import EdgeData


class NodeData:

    def __init__(self, pos: position, id: int, edges: dict):
        if pos is None:
            self.pos = position("0.0,0.0,0.0")
            if edges is None:
                self.edges = dict()
                self.id = id
            else:
                self.edges = edges
                self.id = id
        else:
            self.pos = pos
            self.id = id
            if edges is None:
                self.edges = dict()
            else:
                self.edges = edges


    def getKey(self):
        return self.id

    def getLocation(self):
        return self.pos

    def setLocation(self, p):
        self.pos.x = p.x
        self.pos.y = p.y
        self.pos.z = p.z
