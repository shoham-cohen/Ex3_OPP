import random
from classes.EdgeData import EdgeData
import math
from typing import List
from future.moves import tkinter
from future.moves.tkinter import simpledialog, messagebox
from DiGraph import DiGraph
from classes.NodeData import NodeData
from classes.position import position
from GraphAlgoInterface import GraphAlgoInterface
import json
import pygame
from pygame import Color, display, gfxdraw, font
from pygame.constants import RESIZABLE

WIDTH, HEIGHT = 1200, 600
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=15, flags=RESIZABLE)
time = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 15, bold=True)


def scale(point, minS, maxS, minPoint, maxPoint):
    return int(((point - minPoint) / (maxPoint - minPoint)) * (maxS - minS) + minS)


def arr(color, start, end):
    r = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(screen, color, (
        (end[0] + 10 * math.sin(math.radians(r)), end[1] + 10 * math.cos(math.radians(r))),
        (end[0] + 10 * math.sin(math.radians(r - 120)), end[1] + 10 * math.cos(math.radians(r - 120))),
        (end[0] + 10 * math.sin(math.radians(r + 120)), end[1] + 10 * math.cos(math.radians(r + 120)))))


class GraphAlgo(GraphAlgoInterface):
    graph = DiGraph()

    def __init__(self):
        pass

    def setVal(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> DiGraph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as file:

                data = json.load(file)
                nodes = dict()
                for i in data["Nodes"]:
                    pos: position = position(i["pos"])
                    id = i["id"]
                    edge = dict()
                    NodeDatai: NodeData = NodeData(pos, id, edge)
                    nodes[id] = NodeDatai
                counter = 0
                for i in data["Edges"]:
                    counter = counter + 1
                    src = i["src"]
                    w = i["w"]
                    dest = i["dest"]
                    Edge: EdgeData = EdgeData(src, w, dest)
                    stringD = str(src)
                    stringD += ","
                    stringD += str(dest)

                    if src != dest:
                        nodes[src].edges[stringD] = Edge
                        nodes[dest].edges[stringD] = Edge
                    else:
                        nodes[src].edges[stringD] = Edge
                graph: DiGraph = DiGraph()
                graph.setVal(nodes, counter, 0)
                self.graph = graph
        except Exception:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        dic = dict()
        list_of_nodes = list()
        list_of_edge = list()
        counter = 0
        for i in self.graph.nodes:
            for j in self.graph.nodes[i].edges:
                counter = counter + 1
                if int(self.graph.nodes[i].edges[j].src) == i:
                    d = dict()
                    d["src"] = self.graph.nodes[i].edges[j].src
                    d["w"] = self.graph.nodes[i].edges[j].w
                    d["dest"] = self.graph.nodes[i].edges[j].des
                    list_of_edge.append(d)
        for i in self.graph.nodes:
            d = dict()
            position = str(self.graph.nodes[i].pos.x)
            position += ","
            position += str(self.graph.nodes[i].pos.y)
            position += ","
            position += str(self.graph.nodes[i].pos.z)
            d["pos"] = position
            d["id"] = self.graph.nodes[i].id
            list_of_nodes.append(d)
        dic["edge"] = list_of_edge
        dic["nodes"] = list_of_nodes
        try:
            with open(file_name, 'w') as json_file:
                json.dump(dic, json_file)
        except Exception:
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        (d, prev) = self.dikjestra(id1)
        l = {}
        i = id2
        l[0] = id2
        x = 1
        while i != id1:
            if i == -1:
                return None
            l[x] = prev[i]
            i = l[x]
            x += 1
        res = {}
        x -= 1
        index = 0
        while x != -1:
            res[index] = l[x]
            x -= 1
            index += 1

        return d[id2], res

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        resultList = []
        HelperList = []
        temp = {}
        dist = 0
        for i in range(len(node_lst) - 1):
            mod = (i + 1) % len(node_lst)
            dist, temp = self.shortest_path(node_lst[i], node_lst[mod])
            if temp is None:
                return None
            HelperList.append(temp)

        for i in range(len(HelperList[0])):
            resultList.append(HelperList[0][i])
        i = 1
        while i < len(HelperList):
            j = 1
            while j < len(HelperList[i]):
                resultList.append(HelperList[i][j])
                j += 1
            i += 1

        res = 0.0
        for i in range(len(resultList) - 1):
            str1 = str(resultList[i])
            str2 = str(resultList[i + 1])
            str3 = ","
            strr = str1 + str3 + str2
            res += self.graph.nodes.get(resultList[i]).edges.get(strr).w

        return resultList, res


    def centerPoint(self) -> (int, float):
        resMax = float('inf')
        resId = -1
        for i in self.graph.nodes:
            (dist, path) = self.dikjestra(i)
            distances = dist.values()
            temp = max(distances)
            if temp < resMax:
                resId = i
                resMax = temp
        return resId, resMax

    def plot_graph(self) -> None:
        minx = 100000.0
        maxx = 0.0
        miny = 100000.0
        maxy = 0.0
        edges = {}
        for i in self.graph.nodes:
            if self.graph.nodes[i].pos.x == 0 and self.graph.nodes[i].pos.y == 0:
                p_x = random.uniform(35.18, 35.213)
                p_y = random.uniform(32.101, 32.108)
                st1 = str(p_x)
                st2 = str(p_y)
                st3 = ","
                st4 = "0.0"
                p = position(st1+st2+st3+st4)
                self.graph.nodes[i].setLocation(p)
            for j in self.graph.nodes.get(i).edges:
                if j not in edges:
                    edges[j] = self.graph.nodes.get(i).edges.get(j)
        for i in self.graph.nodes:
            if float(self.graph.nodes.get(i).pos.x) < minx:
                minx = float(self.graph.nodes.get(i).pos.x)
            if float(self.graph.nodes.get(i).pos.x) > maxx:
                maxx = float(self.graph.nodes.get(i).pos.x)
            if float(self.graph.nodes.get(i).pos.y) < miny:
                miny = float(self.graph.nodes.get(i).pos.y)
            if float(self.graph.nodes.get(i).pos.y) > maxy:
                maxy = float(self.graph.nodes.get(i).pos.y)
        flag = True
        tsp = []
        center = []
        while flag:
            clk = False
            screen.fill(Color(110, 150, 150))
            donex = {}
            doney = {}
            for i in self.graph.nodes:
                x = scale(float(self.graph.nodes.get(i).pos.x), 60, screen.get_width() - 60, minx, maxx)
                y = scale(float(self.graph.nodes.get(i).pos.y), 60, screen.get_height() - 60, miny, maxy)
                donex[i] = x
                doney[i] = y
                gfxdraw.filled_circle(screen, x, y, 10, Color(255, 255, 255))
                if center == i:
                    gfxdraw.filled_circle(screen, x, y, 10, Color(150, 0, 0))
                if len(tsp) != 0 and i in tsp:
                    gfxdraw.filled_circle(screen, x, y, 10, Color(0, 255, 0))
                j = FONT.render(str(i), True, pygame.Color(0, 0, 0))
                k = j.get_rect(center=(x, y))
                screen.blit(j, k)
            for i in edges:
                sX = scale(float(self.graph.nodes[edges[i].src].pos.x), 60, screen.get_width() - 60, minx, maxx)
                sY = scale(float(self.graph.nodes[edges[i].src].pos.y), 60, screen.get_height() - 60, miny, maxy)
                dX = scale(float(self.graph.nodes[edges[i].des].pos.x), 60, screen.get_width() - 60, minx, maxx)
                dY = scale(float(self.graph.nodes[edges[i].des].pos.y), 60, screen.get_height() - 60, miny, maxy)
                pygame.draw.line(screen, Color(255, 255, 0), (sX, sY), (dX, dY), width=2)
                arr("red", [sX, sY], [(sX + dX) / 2, (sY + dY) / 2])
            for i in range(len(tsp) - 1):
                sX = scale(float(self.graph.nodes[tsp[i]].pos.x), 60, screen.get_width() - 60, minx, maxx)
                sY = scale(float(self.graph.nodes[tsp[i]].pos.y), 60, screen.get_height() - 60, miny, maxy)
                dX = scale(float(self.graph.nodes[tsp[i + 1]].pos.x), 60, screen.get_width() - 60, minx, maxx)
                dY = scale(float(self.graph.nodes[tsp[i + 1]].pos.y), 60, screen.get_height() - 60, miny, maxy)
                pygame.draw.line(screen, Color(0, 0, 255), (sX, sY), (dX, dY), width=2)
                arr("white", [sX, sY], [(sX + dX) / 2, (sY + dY) / 2])

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    flag = False
                elif e.type == pygame.MOUSEBUTTONUP:
                    clk = True
                    print(pygame.mouse.get_pos())
                    for i in range(len(doney)):
                        if (doney[i] + 10 > pygame.mouse.get_pos()[1] > doney[i] - 10) and \
                                (donex[i] + 10 > pygame.mouse.get_pos()[0] > donex[i] - 10):
                            print()

            b1 = pygame.Rect(0, 0, 60, 30)
            pygame.draw.rect(screen, (250, 250, 210), b1, border_radius=10)
            font1 = pygame.font.SysFont("Ariel", 15)
            screen.blit((font1.render('refresh', True, (0, 0, 0))), (10, 10))
            b2 = pygame.Rect(65, 0, 60, 30)
            pygame.draw.rect(screen, (250, 250, 210), b2, border_radius=10)
            screen.blit((font1.render('TSP', True, (0, 0, 0))), (85, 10))
            b3 = pygame.Rect(130, 0, 80, 30)
            pygame.draw.rect(screen, (250, 250, 210), b3, border_radius=10)
            screen.blit((font1.render('shortest path', True, (0, 0, 0))), (135, 10))
            b4 = pygame.Rect(215, 0, 60, 30)
            pygame.draw.rect(screen, (250, 250, 210), b4, border_radius=10)
            screen.blit((font1.render('center', True, (0, 0, 0))), (225, 10))

            if clk:
                clkpos = pygame.mouse.get_pos()
                if b1.collidepoint(clkpos):
                    center = []
                    tsp = []
                elif b2.collidepoint(clkpos):
                    root = tkinter.Tk()
                    root.withdraw()
                    list = simpledialog.askstring(title="TSP",
                                                  prompt="enter the nodes id's (enter space between each id)")
                    list = list.split()
                    for i in range(len(list)):
                        list[i] = int(list[i])
                    tsp = self.TSP(list)
                    tkinter.messagebox.showinfo("length", tsp[1])
                    tsp = tsp[0]
                elif b3.collidepoint(clkpos):
                    root = tkinter.Tk()
                    root.withdraw()
                    src = simpledialog.askstring(title="path",
                                                 prompt="source node id:")
                    dest = simpledialog.askstring(title="path",
                                                  prompt="destination node id:")
                    tsp = self.shortest_path(int(src), int(dest))
                    print(tsp)
                    tkinter.messagebox.showinfo("length", tsp[0])
                    tsp = tsp[1]
                elif b4.collidepoint(clkpos):
                    c = self.centerPoint()
                    center = c[0]
            display.update()
            time.tick(60)

    def dikjestra(self, src: int) -> (list, list):
        finishedNodes = 0
        INFINITY = 1000000
        prev = {}
        distance = {}
        visited = {}
        for i in self.graph.nodes:
            prev[i] = -1
            distance[i] = INFINITY
            visited[i] = False

        distance[src] = 0
        prev[src] = 0
        for i in self.graph.nodes.get(src).edges:
            if self.graph.nodes.get(src).edges.get(i).src == src:
                if self.graph.nodes.get(src).edges.get(i).w < distance[self.graph.nodes.get(src).edges.get(i).des]:
                    distance[self.graph.nodes.get(src).edges.get(i).des] = self.graph.nodes.get(src).edges.get(i).w
                    prev[self.graph.nodes.get(src).edges.get(i).des] = self.graph.nodes.get(src).edges.get(i).src

        visited[src] = True
        finishedNodes += 1
        while finishedNodes != self.graph.v_size():
            min = INFINITY
            result = 0
            for i in self.graph.nodes:
                if distance[i] < min and visited[i] == False:
                    min = distance[i]
                    result = i

            for i in self.graph.nodes.get(result).edges:
                if self.graph.nodes.get(result).edges.get(i).src == result:
                    if distance[self.graph.nodes.get(result).edges.get(i).src] + self.graph.nodes.get(result).edges.get(
                            i).w < distance[self.graph.nodes.get(result).edges.get(i).des]:
                        distance[self.graph.nodes.get(result).edges.get(i).des] = distance[self.graph.nodes.get(
                            result).edges.get(i).src] + self.graph.nodes.get(result).edges.get(i).w
                        prev[self.graph.nodes.get(result).edges.get(i).des] = self.graph.nodes.get(result).edges.get(
                            i).src

            visited[result] = True
            finishedNodes += 1

        return distance, prev
