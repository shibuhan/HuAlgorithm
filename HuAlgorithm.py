import GEXFManager

import math


def HU(graph):
    setLabels(graph)
    a = calcA(graph)

    for j in range(1, len(graph)+1):
        U = getU(graph)
        S = getS(U, a)
        schedule(S, j)

        if len(S) == 0:
            break

        print("Time " + str(j), end=' ')
        for node in S:
            print(node.id, end=' ')
        print()


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
    graph = GEXFManager.init()
    HU(graph)
    GEXFManager.write(graph)


if __name__ == "__main__":
    main()