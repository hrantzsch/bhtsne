import matplotlib.pyplot as plt
import sys

with open(sys.argv[1], 'r') as f:
    x, y = zip(*[line.split() for line in f])

print("Plotting {} samples".format(len(x)))
plt.scatter(x, y)
out = sys.argv[2] if len(sys.argv) == 3 else 'plot.png'
plt.savefig(out)
