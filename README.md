# Ex4_OPP

* Written by Shoham Cohen and Yehonatan Baruchson.
## position
Object that stores 3 values:
* double x
* double y
* double z
The constructor recives a String and splits him to the 3 values.

## EdgeData
EdgeData is an object that stores 3 values:
* int src
* int des
* double w

### Methods
* getSrc: return the id of the source NodeData of the edge.
* getDes: return the id of the destination NodeData of the edge.
* getWeight: return the weight of the edge.

## NodeData

Nodedata is an object that stores 3 values:
* nodedata ID.
* nodedata position.
* nodedata Dict of all the edges that related to this node.

### Methods
* GetKey: returns the ID of the Node
* GetLocation: returns the positon of the Node
* SetLocation: changes the position of thr Node to the inputted position

## DiGraph

DiGraph is an object that stores 3 values:
* Dict of NodeDatas.
* int NumOfEdges: number of the edges in the graph.
* int MC: parameter that helps us to track changes in the graph.

### Methods
* v_size: returns the number of nodes on the graph.
* e_size: returns the number of Edges in the graph.
* get_all_v: returns a Dict with all the nodes in the graph.
* all_in_edges_of_node: return a Dict of all the nodes who has an edge that her dest is the inputted node.
* all_out_edges_of_node: return a Dict of all the nodes who has an edge that her source is the inputted node.
* get_mc: returns the MC.
* add_edge: addind the inputted edge, returns True if added succesfully.
* add_node: addind the inputted node, returns True if added succesfully.
* remove_node: delete the Node and all of his Edges from the graph, returns True if added succesfully.
* remove_edge: delete the specific inputted Edge, returns True if added succesfully.

## GraphAlgo

GraphAlgo is an object who stores only one value:
* GraphAlgo - DiGraph.

### Methods

* dikjestra: dikjestra algorithem
* shortestPath: does the dijkstra's algorithm, we will follow the values that stores in the prev array, we will start from prev[des] and see what value there is.
we will continue doing that while also we store every value in our way until we get to the prev[src]. we will return that list and the distance of the path.
* centerPoint: checks the node that has the smallest largest distance to other node in the graph.
we will again do the dijkstra's algorithm but now we will do it to every node. for each node we will take the biggest value in his distance array,
at the end the node with the smallest chosen value is the center node.
* TSP: returns the shortest path that go through all the inputted nodes, for each node in the list we will find the shortest path to the node the comes after him and we will close a circle.
* save_to_json: saves the graph to a new json file.
* load_from_json: load a new graph from a json file.
* plot_graph: The GUI, drawing the nodes and edges by their position. The GUI include option the see the center Node, TSP of inputted nodes id's and the shortest path between two inputted nodes.
