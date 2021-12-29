import random

from classes.EdgeData import EdgeData
from classes.NodeData import NodeData
from classes.position import position


class DiGraph:

    nodes = dict()
    NumOfEdges = 0
    MC = 0

    def __init__(self):
        pass

    def setVal(self, nodes: dict, NumOfEdges: int, MC: int):
        self.nodes = nodes
        self.NumOfEdges = NumOfEdges
        self.MC = MC

    def v_size(self) -> int:
        res = len(self.nodes)
        return res

    def e_size(self) -> int:
        return self.NumOfEdges

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        outedges = dict()
        for i in self.nodes.get(id1).edges:
            if self.nodes.get(id1).edges.get(i).des == id1:
                outedges[self.nodes.get(id1).edges.get(i).src] = self.nodes.get(id1).edges.get(i).w

        return outedges

    def all_out_edges_of_node(self, id1: int) -> dict:
        inedges = dict()
        for i in self.nodes.get(id1).edges:
            if self.nodes.get(id1).edges.get(i).src == id1:
                inedges[self.nodes.get(id1).edges.get(i).des] = self.nodes.get(id1).edges.get(i).w

        return inedges

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes and weight >= 0 and id1 != id2:
            edge = EdgeData(id1, weight, id2)
            str1 = str(id1)
            str2 = str(id2)
            str3 = ","
            stri = str1+str3+str2
            self.nodes.get(id1).edges[stri] = edge
            self.nodes.get(id2).edges[stri] = edge
            self.NumOfEdges = self.NumOfEdges + 1
            self.MC = self.MC + 1
            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            edges = dict()

            node = NodeData(None, node_id, edges)
            self.nodes[node_id] = node
            self.MC = self.MC + 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for i in self.nodes:
                j = 0
                while j < self.nodes[i].edges:
                    if self.nodes[i].edges[j].des == node_id or self.nodes[i].edges[j].src == node_id:
                        self.nodes[i].edges.pop(j)
                        self.NumOfEdges = self.NumOfEdges - 2
            self.nodes.pop(node_id)
            self.MC = self.MC + 1
            return True

        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes and node_id2 in self.nodes:
            for i in self.nodes.get(node_id1).edges:
                if self.nodes.get(node_id1).edges.get(i).des == node_id2:
                    self.nodes.get(node_id1).edges.pop(i)
                    break

            for i in self.nodes.get(node_id2).edges:
                if self.nodes.get(node_id2).edges.get(i).des == node_id1:
                    self.nodes.get(node_id2).edges.pop(i)
                    break
            return True

        return False
