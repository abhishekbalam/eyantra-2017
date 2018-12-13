import astar_test


maze = [[0 for i in range(10)]for i in range(10)]

result = astar_test.astar(maze,(1,1),(6,6))

print result