class SeqNode(object):

    def __init__(self, name, seq):
        self.name = name
        self.seq = seq
        self.cnt = 1

    def __eq__(self, other):
        return self.cnt == other.cnt

    def __ne__(self, other):
        return self.cnt != other.cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __gt__(self, other):
        return self.cnt > other.cnt

    def __le__(self, other):
        return self.cnt <= other.cnt

    def __ge__(self, other):
        return self.cnt >= other.cnt