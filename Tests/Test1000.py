import unittest
import time

from classes.GraphAlgo import GraphAlgo


class Test1000(unittest.TestCase):

    def test_shortestPath(self):
        g = GraphAlgo()
        g.load_from_json("1000Nodes.json")
        start = time.time_ns()
        self.assertEquals(g.shortest_path(31, 999),
                          (549.4918018351897, {0: 31, 1: 407, 2: 894, 3: 692, 4: 674, 5: 870, 6: 683, 7: 940, 8: 999}))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"shortestPath: {t} ms")

    def test_CenterPoint(self):
        g = GraphAlgo()
        g.load_from_json("1000Nodes.json")
        start = time.time_ns()
        self.assertEquals(g.centerPoint(), (362, 1185.9594924690523))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"CenterPoint: {t} ms")

    def test_TSP(self):
        g = GraphAlgo()
        g.load_from_json("1000Nodes.json")
        l = [2, 1, 4]
        start = time.time_ns()
        res = g.TSP(l)
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"TSP: {t} ms")
        list = res[0]
        start = time.time_ns()
        self.assertEquals(len(list), 21)

    def test_save_to_json(self):
        g = GraphAlgo()
        g.load_from_json("1000Nodes.json")
        start = time.time_ns()
        self.assertTrue(g.save_to_json("output.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"save_to_json: {t} ms")

    def test_load_from_json(self):
        start = time.time_ns()
        g = GraphAlgo()
        self.assertTrue(g.load_from_json("1000Nodes.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"load_from_json: {t} ms")
