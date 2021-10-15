from pyvis.network import Network
import networkx as nx
import instaloader
import CB_Functions as cbfunc
import CB_Formatting as cbform


class LayeredNodeGroup:
    def __init__(self, IL, layerName, depth):
        self.IL = IL
        self.layerName = layerName
        self.depth = depth

        self.nodeList = []

    def generateNodeGroup(self, nodes):
        for node in nodes: