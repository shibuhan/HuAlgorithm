import GEXFManager

import math


def HU(graph):
    setLabels(graph)
    a = calcA(graph)
    # If I followed the textbook, this "a" should have been passed as an argument to this "HU" function,
    # like HU(graph, a), but I needed a labeled Node to calculate "a", so I calculated it here.

    l = 1
    while len(list(filter(lambda node: not node.scheduled, graph))) != 0:
        U = getU(graph)
        S = getS(U, a)
        schedule(S, l)
        l = l + 1

        # DEBUG
        # print("Time " + str(l-1), end=' ')
        # for node in S:
        #     print(node.id, end=' ')
        # print()


def setLabels(graph):
    for node in graph:
        node.setLabel()


def calcA(graph):
    alpha = max(graph, key=lambda node: node.label).label
    ramda = alpha
    candidates = []

    for y in range(1, alpha+1+1):
        result = sigmaP(graph, y, alpha) / (y + ramda - alpha)
        candidates.append(result)

    a = math.ceil(max(candidates))
    return a


def sigmaP(graph, y, alpha):
    sumP = 0
    for j in range(1, y+1):
        p = list(filter(lambda node: node.label == (alpha + 1 - j), graph))
        sumP = sumP + len(p)

    return sumP


def getU(graph):
    return list(filter(lambda node: node.isTargetNode(), graph))


def getS(U, a):
    S = []
    for i in range(a):
        if len(U) == 0:
            break

        target = max(U, key=lambda node: node.label)
        U.remove(target)
        S.append(target)

    return S


def schedule(S, time):
    for node in S:
        node.scheduled = True
        node.time = time


def main():
    graph = GEXFManager.read()
    HU(graph)
    GEXFManager.write(graph)


if __name__ == "__main__":
    main()