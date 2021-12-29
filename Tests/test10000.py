import unittest
import time

from Ex3.GraphAlgo import GraphAlgo


class Test10000(unittest.TestCase):

    def test_shortestPath(self):
        g = GraphAlgo()
        g.load_from_json("10000Nodes.json")
        start = time.time_ns()
        self.assertEquals(g.shortest_path(31, 999),
                          (1203.0919651227066, {0: 31, 1: 9646, 2: 7801, 3: 9668, 4: 8818, 5: 8199, 6: 5383, 7: 7253, 8: 9181, 9: 6635, 10: 2815, 11: 1050, 12: 9064, 13: 140, 14: 7235, 15: 999}))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"shortestPath: {t} ms")

    """
    def test_CenterPoint(self):
        g = GraphAlgo()
        g.load_from_json("10000Nodes.json")
        start = time.time_ns()
        self.assertEquals(g.centerPoint(), (3846, 1185.9594924690523))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"CenterPoint: {t} ms")

"""
    def test_TSP(self):
        g = GraphAlgo()
        g.load_from_json("10000Nodes.json")
        l = [2, 1, 4]
        start = time.time_ns()
        res = g.TSP(l)
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"TSP: {t} ms")
        list = res[0]
        self.assertEquals(len(list), 19)

    def test_save_to_json(self):
        g = GraphAlgo()
        g.load_from_json("10000Nodes.json")
        start = time.time_ns()
        self.assertTrue(g.save_to_json("output.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"save_to_json: {t} ms")

    def test_load_from_json(self):
        start = time.time_ns()
        g = GraphAlgo()
        self.assertTrue(g.load_from_json("10000Nodes.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"load_from_json: {t} ms")



