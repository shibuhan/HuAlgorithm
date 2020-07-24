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

    def hasPredecessors(self):
        return len(self.predecessors) != 0

    def allPredecessorsIsScheduled(self):
        return all(predecessor.scheduled for predecessor in self.predecessors)

    def isTargetNode(self):
        if not self.scheduled:
            return not self.hasPredecessors() or self.allPredecessorsIsScheduled()
        else:
            return False

    def setLabel(self):
        self.label = self.getDistance(self, self.label)

    def getDistance(self, node, distance):
        successor = node.successor

        if successor is None:
            return distance
        else:
            distance = distance + 1
            return node.getDistance(successor, distance)