# -*- coding: utf-8 -*-

import networkx as nx
from math import prod

G = nx.Graph()

with open('i25.txt') as f:
    for line in f:
        left, right = line.strip().split(': ')
        G.add_edges_from(((left, node) for node in right.split(' ')))

G.remove_edges_from(nx.minimum_edge_cut(G))

print(prod(map(len, nx.connected_components(G))))

# 551196