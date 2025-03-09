import matplotlib.pyplot as plt
from searchProblem import Arc, Search_problem_from_explicit_graph

problem1 = Search_problem_from_explicit_graph(
    'Problem 1',
    {'A', 'B', 'C', 'D', 'G', 'X', 'L'},
    [
        Arc('A', 'B', 3),
        Arc('A', 'C', 1),
        Arc('B', 'D', 1),
        Arc('B', 'G', 3),
        Arc('C', 'B', 1),
        Arc('C', 'D', 3),
        Arc('D', 'G', 1),
    ],
    start='A',
    goals={'G'},
    positions={
        'A': (0, 1),
        'B': (0.5, 0.5),
        'C': (0, 0.5),
        'D': (0.5, 0),
        'G': (1, 0)
    }
)
problem1.show()
plt.show()

# Aggiungi le righe di codice per testare il Searcher
if __name__ == "__main__":
    from searchGeneric import Searcher
    # Crea un'istanza del searcher per il problema 1
    searcher1 = Searcher(problem1)
    # Trova la prima soluzione
    searcher1.search()
    # Trova la prossima soluzione (ripeti fino a quando non ci sono più soluzioni)
    searcher1.search()

# problem2 = Search_problem_from_explicit_graph(
#     'Problem 2',
#     {'A', 'B', 'C', 'D', 'E', 'G', 'H', 'J'},
#     [
#         Arc('A', 'B', 1),
#         Arc('B', 'C', 3),
#         Arc('B', 'D', 1),
#         Arc('D', 'E', 3),
#         Arc('D', 'G', 1),
#         Arc('A', 'H', 3),
#         Arc('H', 'J', 1),
#     ],
#     start='A',
#     goals={'G'},
#     positions={
#         'A': (0, 1),
#         'B': (0, 3 / 4),
#         'C': (0, 0),
#         'D': (1 / 4, 3 / 4),
#         'E': (1 / 4, 0),
#         'G': (2 / 4, 3 / 4),
#         'H': (3 / 4, 1),
#         'J': (3 / 4, 3 / 4)
#     }
# )
# problem2.show()

# problem3 = Search_problem_from_explicit_graph(
#     'Problem 3',
#     {'a', 'b', 'c', 'd', 'e', 'g', 'h', 'j'},
#     [],
#     start='g',
#     goals={'k', 'g'}
# )
# problem3.show()

# simp_delivery_graph = Search_problem_from_explicit_graph(
#     "Acyclic Delivery Graph",
#     {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'},
#     [
#         Arc('A', 'B', 2),
#         Arc('A', 'C', 3),
#         Arc('A', 'D', 4),
#         Arc('B', 'E', 2),
#         Arc('B', 'F', 3),
#         Arc('C', 'J', 7),
#         Arc('D', 'H', 4),
#         Arc('F', 'D', 2),
#         Arc('H', 'G', 3),
#         Arc('J', 'G', 4),
#     ],
#     start='A',
#     goals={'G'},
#     hmap={
#         'A': 7,
#         'B': 5,
#         'C': 9,
#         'D': 6,
#         'E': 3,
#         'F': 5,
#         'G': 0,
#         'H': 3,
#         'J': 4,
#     },
#     positions={
#         'A': (0.4, 0.1),
#         'B': (0.4, 0.4),
#         'C': (0.1, 0.1),
#         'D': (0.7, 0.1),
#         'E': (0.6, 0.7),
#         'F': (0.7, 0.4),
#         'G': (0.7, 0.9),
#         'H': (0.9, 0.6),
#         'J': (0.3, 0.9),
#     }
# )
# simp_delivery_graph.show()

# cyclic_simp_delivery_graph = Search_problem_from_explicit_graph(
#     "Cyclic Delivery Graph",
#     {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'},
#     [
#         Arc('A', 'B', 2),
#         Arc('A', 'C', 3),
#         Arc('A', 'D', 4),
#         Arc('B', 'E', 2),
#         Arc('B', 'F', 3),
#         Arc('C', 'A', 3),
#         Arc('C', 'J', 6),
#         Arc('D', 'A', 4),
#         Arc('D', 'H', 4),
#         Arc('F', 'B', 3),
#         Arc('F', 'D', 2),
#         Arc('G', 'H', 3),
#         Arc('G', 'J', 4),
#         Arc('H', 'D', 4),
#         Arc('H', 'G', 3),
#         Arc('J', 'C', 6),
#         Arc('J', 'G', 4),
#     ],
#     start='A',
#     goals={'G'},
#     hmap={
#         'A': 7,
#         'B': 5,
#         'C': 9,
#         'D': 6,
#         'E': 3,
#         'F': 5,
#         'G': 0,
#         'H': 3,
#         'J': 4,
#     },
#     positions={
#         'A': (0.4, 0.1),
#         'B': (0.4, 0.4),
#         'C': (0.1, 0.1),
#         'D': (0.7, 0.1),
#         'E': (0.6, 0.7),
#         'F': (0.7, 0.4),
#         'G': (0.7, 0.9),
#         'H': (0.9, 0.6),
#         'J': (0.3, 0.9),
#     }
# )
# cyclic_simp_delivery_graph.show()

# tree_graph = Search_problem_from_explicit_graph(
#     "Tree Graph",
#     {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#      'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK'},
#     [
#         Arc('A', 'B', 1),
#         Arc('A', 'C', 1),
#         Arc('B', 'D', 1),
#         Arc('B', 'E', 1),
#         Arc('C', 'F', 1),
#         Arc('C', 'G', 1),
#         Arc('D', 'H', 1),
#         Arc('D', 'I', 1),
#         Arc('E', 'J', 1),
#         Arc('E', 'K', 1),
#         Arc('F', 'L', 1),
#         Arc('G', 'M', 1),
#         Arc('G', 'N', 1),
#         Arc('H', 'O', 1),
#         Arc('H', 'P', 1),
#         Arc('J', 'Q', 1),
#         Arc('J', 'R', 1),
#         Arc('L', 'S', 1),
#         Arc('L', 'T', 1),
#         Arc('N', 'U', 1),
#         Arc('N', 'V', 1),
#         Arc('O', 'W', 1),
#         Arc('P', 'X', 1),
#         Arc('P', 'Y', 1),
#         Arc('R', 'Z', 1),
#         Arc('R', 'AA', 1),
#         Arc('T', 'BB', 1),
#         Arc('T', 'CC', 1),
#         Arc('V', 'DD', 1),
#         Arc('V', 'EE', 1),
#         Arc('W', 'FF', 1),
#         Arc('X', 'GG', 1),
#         Arc('Y', 'HH', 1),
#         Arc('AA', 'II', 1),
#         Arc('CC', 'JJ', 1),
#         Arc('CC', 'KK', 1),
#     ],
#     start='A',
#     goals={'K', 'M', 'T', 'X', 'Z', 'HH'},
#     positions={
#         'A': (0.5, 0.95),
#         'B': (0.25, 0.85),
#         'C': (0.75, 0.85),
#         'D': (0.1, 0.75),
#         'E': (0.4, 0.75),
#         'F': (0.6, 0.75),
#         'G': (0.9, 0.75),
#         'H': (0.1, 0.56),
#         'I': (0.25, 0.56),
#         'J': (0.4, 0.56),
#         'K': (0.5, 0.56),
#         'L': (0.6, 0.56),
#         'M': (0.75, 0.56),
#         'N': (0.9, 0.56),
#         'O': (0, 0.37),
#         'P': (0.1, 0.37),
#         'Q': (0.25, 0.37),
#         'R': (0.4, 0.37),
#         'S': (0.5, 0.37),
#         'T': (0.6, 0.37),
#         'U': (0.75, 0.37),
#         'V': (0.9, 0.37),
#         'W': (0, 0.18),
#         'X': (0.1, 0.18),
#         'Y': (0.25, 0.18),
#         'Z': (0.4, 0.18),
#         'AA': (0.5, 0.18),
#         'BB': (0.6, 0.18),
#         'CC': (0.75, 0.18),
#         'DD': (0.9, 0.18),
#         'EE': (1, 0.18),
#         'FF': (0, 0),
#         'GG': (0.1, 0),
#         'HH': (0.25, 0),
#         'II': (0.5, 0),
#         'JJ': (0.75, 0),
#         'KK': (0.9, 0),
#     }
# )
# tree_graph.show(show_costs=False)
# plt.show()
