import unittest
import time

from classes.GraphAlgo import GraphAlgo


class Test10000(unittest.TestCase):

    def test_shortestPath(self):
        g = GraphAlgo()
        g.load_from_json("100000Nodes.json")
        start = time.time_ns()
        self.assertEquals(g.shortest_path(31, 999),
                          (512.7494720292688, {0: 31, 1: 12202, 2: 26150, 3: 37537, 4: 19166, 5: 91635, 6: 5103, 7: 54018, 8: 11208, 9: 999}))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"shortestPath: {t} ms")

    def test_TSP(self):
        g = GraphAlgo()
        g.load_from_json("100000Nodes.json")
        l = [2, 1, 4]
        start = time.time_ns()
        res = g.TSP(l)
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"TSP: {t} ms")
        list = res[0]
        self.assertEquals(len(list), 23)

    def test_save_to_json(self):
        g = GraphAlgo()
        g.load_from_json("100000Nodes.json")
        start = time.time_ns()
        self.assertTrue(g.save_to_json("output.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"save_to_json: {t} ms")

    def test_load_from_json(self):
        start = time.time_ns()
        g = GraphAlgo()
        self.assertTrue(g.load_from_json("100000Nodes.json"))
        stop = time.time_ns()
        t = (stop - start) / 1e+6
        print(f"load_from_json: {t} ms")



