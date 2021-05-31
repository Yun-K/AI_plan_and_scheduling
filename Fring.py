class Fringe:
    def __init__(self, node1, node2, savingCost):
        self.node1 = node1
        self.node2 = node2
        self.savingCost = savingCost

    def __str__(self):
        return "Fringe(SavingCost_priority={p}, node1={n1},node2={n2})".format(p=self.savingCost, n1=self.node1, n2=self.node2)

    def __lt__(self, other):
        """__lt__ define the comparison, compare is based on the saving Cost, the bigger saving Cost got higher priority

        Args:
            other (Fringe): other Fringe object to be compared

        Returns:
            [type]: [description]
        """
        return self.savingCost > other.savingCost
