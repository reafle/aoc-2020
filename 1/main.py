def getData(fname):
    return map(lambda x : int(x[:-1]), list(open(fname)))

def pairs(data):
    for k, x in enumerate(data, 0):
        y = 2020 - x
        if y in data[k:]:
            print(x * y)

def triplets(data):
    for k, x in enumerate(data, start=0):
        for j, y in enumerate(data[k:], start=k):
            z = 2020-x-y;
            if z in data[j:]:
                print(x * y * z)

pairs(getData('input.txt'))
triplets(getData('input.txt'))
