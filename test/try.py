#%%
import networkx as nx
import networkx.drawing.nx_pydot as pd
import matplotlib as plt
G=nx.DiGraph()
G.add_edge(1,2,type='m')
G.add_edge(1,3,type='m')
G.add_edge(2,4,type='m')
G.add_edge(2,5,type='m')
G.add_edge(2,6,type='m')
G.add_edge(4,7,type='m')
G.add_edge(5,8,type='m')
G.add_edge(6,9,type='m')
G.add_edge(6,10,type='m')
G.add_edge(11,12,type='m')
G.add_edge(11,13,type='m')
G.add_edge(20,2,type='f')
G.add_edge(20,3,type='f')
nx.draw_spring(G,with_labels=True)
pd.write_dot(G,r"C:\Temp\Test.dot")