from heapq import heappop, heappush
from collections import Counter


class HuffmanTreeNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __add__(self, other):
        return HuffmanTreeNode(self.freq+other.freq, left=self, right=other)
    
    @property
    def is_leaf(self):
        return not self.left and not self.right
    


def encode(data):
    tree_root = tree(data)
    mapping_res = mapping(tree_root)

    return "".join(mapping_res[char] for char in data), tree_root


def decode(data, tree_root):
    node = tree_root
    decoded = ""

    i = 0
    while i < len(data):
        while not node.is_leaf:
            node = node.left if data[i] == "0" else node.right
            i += 1
        
        decoded += node.char
        node = tree_root
    
    return decoded


def tree(data):
    nodes = []
    
    for pair in Counter(data).items():
        heappush(nodes, HuffmanTreeNode(*reversed(pair)))
    
    while len(nodes) > 1:
        left = heappop(nodes)
        right = heappop(nodes)
        heappush(nodes, left+right)
    
    return nodes[0]


def mapping(node):
   return _mapping(node, {}, "")


def _mapping(node, res, bits):
    try:
        _mapping(node.left, res, bits+"0")
        _mapping(node.right, res, bits+"1")
    except AttributeError:
        pass
    
    res[node.char] = bits
    return res
