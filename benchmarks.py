import timeit
import numpy as np
import networkx as nx
import sys

def printres(exname, r):
    a = np.array(r)
    print("{:20s} mean {:8.3f} (sd{:8.3f})".format(exname, a.mean(),a.std()))

print("""
python version {:s}
numpy version {:s}
networkx version {:s}
""".format(sys.version.replace('\n', ""), np.version.version, nx.__version__))


npsetup = """
import numpy as np

dim = 5000
A = np.random.random((dim,dim))
"""

nptimer = timeit.Timer("A = np.dot(A,A)", setup=npsetup)
npres = [nptimer.timeit(1) for x in range(5)]

printres("np dot", npres)


nxtimer = timeit.Timer('nx.algorithms.betweenness_centrality(g)', setup="""
import networkx as nx
N = 500
g = nx.barabasi_albert_graph(N, 10)
""")

nxres = [nxtimer.timeit(1) for x in range(5)]

printres("nx betweenness", nxres)
