import matplotlib.pyplot as plt

shortest_route = [(2, 8), (2, 8), (1, 3), (0, 2), (0, 0), (6, 1), (9, 3), (8, 4), (7, 4), (6, 4), (2, 8)]

plt.plot(*zip(*shortest_route), '-o')
plt.show()