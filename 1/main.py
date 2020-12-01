import time

def getData(fname):
    return map(lambda x : int(x[:-1]), list(open(fname)))


def pairs_optimized(data):
    for k, x in enumerate(data, start=0):
        for y in data[k:]:
                if x + y == 2020:
                    print(x * y)

def triplets_optimized(data):
    for k, x in enumerate(data, start=0):
        for j, y in enumerate(data[k:], start=0):
            for z in data[j:]:
                if x + y + z == 2020:
                    print(x * y * z)

def pairs_lame(data):
    for x in data:
        for y in data:
                if x + y == 2020:
                    print(x * y)

def triplets_lame(data):
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    print(x * y * z)

def pairs_best(data):
    for k, x in enumerate(data, 0):
        y = 2020 - x
        if y in data[k:]:
            print(x * y)

def triplets_best(data):
    for k, x in enumerate(data, start=0):
        for j, y in enumerate(data[k:], start=k):
            z = 2020-x-y;
            if z in data[j:]:
                print(x * y * z)


print("------")
start_time = time.time()
print("O(n^2) / O(n^3)")
pairs_lame(getData('input.txt'));
triplets_lame(getData('input.txt'));
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("O(n^2) / O(n^3) with adjusted starting indexes")
pairs_optimized(getData('input.txt'));
triplets_optimized(getData('input.txt'));
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print("O(n) / O(n^2) with adjusted starting indexes")
pairs_best(getData('input.txt'))
triplets_best(getData('input.txt'))
print("--- %s seconds ---" % (time.time() - start_time))
