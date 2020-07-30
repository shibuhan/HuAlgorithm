class Node:
    id = ''
    label = 0
    successor = None
    predecessors = []
    time = -1
    scheduled = False

    def __init__(self, id, successor, predecessors):
        self.id = id
        self.successor = successor
        self.predecessors = predecessors

    def setLabel(self):
        self.label = self.__getDistance(self, self.label)

    def isTargetNode(self):
        if not self.scheduled:
            return not self.__hasPredecessors() or self.__allPredecessorsIsScheduled()
        else:
            return False

    def __getDistance(self, node, distance):
        successor = node.successor

        if successor is None:
            return distance
        else:
            distance = distance + 1
            return node.__getDistance(successor, distance)

    def __hasPredecessors(self):
        return len(self.predecessors) != 0

    def __allPredecessorsIsScheduled(self):
        return all(predecessor.scheduled for predecessor in self.predecessors)