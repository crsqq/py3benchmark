import timeit
import numpy as np
import networkx as nx
import sys

def printres(exname, r):
    a = np.array(r)
    print("{:20s} mean {:8.3f} (sd{:8.3f})".format(exname, a.mean(),a.std()))

def run_benchmark(benchmarkname, stmt, setup, niter):
    t = timeit.Timer(stmt, setup=setup)
    res = [t.timeit(1) for x in range(niter)]
    printres(benchmarkname, res)  

print("""
python version {:s}
numpy version {:s}
networkx version {:s}
""".format(sys.version.replace('\n', ""), np.version.version, nx.__version__))

dim = 4096
n,m = 100,10 # parameter for BA graph

niter = 5


# matrix mult
run_benchmark('np dot',
	"A = np.dot(A,A)",
	"""
import numpy as np
A = np.random.random(({dim},{dim}))
""".format(dim=dim),
niter)


run_benchmark('np svd', "np.linalg.svd(A, full_matrices = False)",
	"""
import numpy as np
A = np.random.random((int({size} / 2), int({size} / 4)))
""".format(size=dim),
niter)


run_benchmark('nx betweenness', 'nx.algorithms.betweenness_centrality(g)',
	"""
import networkx as nx
g = nx.barabasi_albert_graph({n}, {m})
""".format(n=n, m=m),
niter)


