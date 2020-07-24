import Node as n
import networkx as nx

readFile = "./testdata.gexf"
resultFile = "./result.gexf"


def read():
    testdata = nx.read_gexf(readFile)

    node_objects = []
    for node_gexf in testdata.nodes:
        predecessors_gexf = list(testdata.predecessors(node_gexf))
        if len(predecessors_gexf) == 0:
            continue

        node_object = n.Node(str(node_gexf), None, [])
        node_objects.append(node_object)

    for node_object in node_objects:
        predecessors_gexf = list(testdata.predecessors(node_object.id))
        predecessor_objects = []
        for predecessor_gexf in predecessors_gexf:
            predecessor_object = next(filter(lambda node: node.id == str(predecessor_gexf), node_objects), None)
            if predecessor_object is not None:
                predecessor_objects.append(predecessor_object)

        successors_gexf = list(testdata.successors(node_object.id))
        successor_gexf = successors_gexf[0] if len(successors_gexf) != 0 else None
        successor_object = None
        if successor_gexf is not None:
            successor_object = next(filter(lambda node: node.id == successor_gexf, node_objects), None)

        node_object.predecessors = predecessor_objects
        node_object.successor = successor_object

    return node_objects


NOP_TOP = "NOP_TOP"


def write(graph):
    G = nx.DiGraph()
    G.add_node(NOP_TOP, time=0)
    for node in graph:
        G.add_node(node.id, time=node.time)

        if len(node.predecessors) == 0:
            G.add_edge(NOP_TOP, node.id)

        if node.successor is not None:
            G.add_edge(node.id, node.successor.id)

    # G.nodes[NOP_TOP]['viz'] = {'size': 100, 'color': {'a': 0, 'r': 255, 'g': 255, 'b': 255}, 'position': {'x': 0, 'y': 0, 'z': 0}}

    nx.write_gexf(G, resultFile)