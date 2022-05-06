# %%
import pandas as pd
import numpy as np
import networkx as nx
import networkx.drawing.nx_pydot as pyd
import matplotlib as plt
import csv

# read individual data
individuals = pd.read_csv(r'C:\Python\Graphs\AHRI_Individuals.csv', sep=',', header=0, index_col=0, dtype={
                          'MotherId': int, 'FatherId': int, 'NodeId': int}, parse_dates=['DoB', 'DoD'])
individuals.info()
G = nx.DiGraph()
for row in individuals.itertuples():
    # Add node
    G.add_node(row.Index, sex=row.Sex)
    # Add mother edge
    if row.MotherId != 0:
        G.add_edge(row.MotherId, row.Index, type=2)
    if row.FatherId != 0:
        G.add_edge(row.FatherId, row.Index, type=1)
with open(r'C:\Python\Graphs\network_detail.csv', mode='w') as csv_file:
    fieldnames = ['root', 'nodes', 'parent', 'child', 'type']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for w in nx.weakly_connected_component_subgraphs(G):
        l = nx.topological_sort(w)
        root = next(l)
        if root==740:
            pyd.write_dot(G,r"C:\Python\Graphs\Graph740.dot")
        nodes = w.order()
        for p, c, t in w.edges(data=True):
            writer.writerow({'root': root, 'nodes': nodes,
                             'parent': p, 'child': c, 'type': t['type']})
    csv_file.close()
