class SeqNode(object):

    def __init__(self, seq):
        self.seq = seq
        self.cnt = 1

    def __eq__(self, other):
        if type(other) == int:
            return self.cnt == other
        else:
            return self.cnt == other.cnt

    def __ne__(self, other):
        if type(other) == int:
            return self.cnt != other
        else:
            return self.cnt != other.cnt

    def __lt__(self, other):
        if type(other) == int:
            return self.cnt < other
        else:
            return self.cnt < other.cnt

    def __gt__(self, other):
        if type(other) == int:
            return self.cnt > other
        else:
            return self.cnt > other.cnt

    def __le__(self, other):
        if type(other) == int:
            return self.cnt <= other
        else:
            return self.cnt <= other.cnt

    def __ge__(self, other):
        if type(other) == int:
            return self.cnt >= other
        else:
            return self.cnt >= other.cnt
