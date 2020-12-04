import sys

import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000)

# This forms a 2d array of the map, in the format of
# [
#    ['.','.','.','#','.','.','.','#'],
#    ['#','#','.','.','#','#','.','#'],
#     ...
# ]

def getData(fname):
    return map(lambda x : [c for c in x[:-1]], list(open(fname)))

def traverse(map2d):
    # Number of steps we take
    slopes = [

        # Part 1:
        # Right 3, down 1. (This is the slope you already checked.)
        [3, 1],

        # Part 2: the above, multiplied by 
        # Right 1, down 1.
        # Right 5, down 1.
        # Right 7, down 1.
        # Right 1, down 2.
        [1, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    # result
    slopeTrees = [];
    mapBackup = map2d

    # Iterate over all the slopes
    for (right, down) in slopes:
        map2d = mapBackup
        trees = 0

        # Iterate over the map using the given steps
        for row in range(0, len(map2d), down):
            nextRow = row+1;

            # if the next step is the end of the map - record the result
            if (row+down >= len(map2d)):
                slopeTrees.append(trees)

            # shift the map to the right for set number of steps
            map2d = map(lambda x: x[right:] + x[:right], map2d)

            # shift the map to the down for set number of steps
            map2d = map2d[down:] + map2d[:down]

            # Mark a tree! 
            if (map2d[0][0] == '#'):
                trees += 1

    # Multiply the result
    return reduce(lambda a, b: a*b, slopeTrees)

print(traverse(getData('demo.txt' if len(sys.argv) > 1 and sys.argv[1] == '-d' else 'input.txt')))


