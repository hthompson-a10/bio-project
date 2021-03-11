class AnnotationNode(object):
    
    def __init__(self, start, end, gene_name, annotation=None):
        self.start = start
        self.end = end
        self.gene_name = gene_name
        self.annotation = annotation


class GeneBlock(object):
    
    def __init__(self, start):
        self.start = start
        self.annotations = []
    
    def binary_search(self, left, right, coordinate):
        if right >= left:
            mid = left + (right - left) // 2
            if self.annotations[mid].start <= coordinate and self.annotations[mid].end >= coordinate:
                return self.annotations[mid]
            elif self.annotations[mid].start > coordinate:
                return binary_search(self.annotations, left, mid-1, coordinate)
            else:
                return binary_search(self.annotations, mid+1, right, coordinate)

    def __eq__(self, other):
        if type(other) == int:
            return self.start == other
        else:
            return self.start == other.start

    def __ne__(self, other):
        if type(other) == int:
            return self.start != other
        else:
            return self.start != other.start

    def __lt__(self, other):
        if type(other) == int:
            return self.start < other
        else:
            return self.start < other.start

    def __gt__(self, other):
        if type(other) == int:
            return self.start > other
        else:
            return self.start > other.start

    def __le__(self, other):
        if type(other) == int:
            return self.start <= other
        else:
            return self.start <= other.start

    def __ge__(self, other):
        if type(other) == int:
            return self.start >= other
        else:
            return self.start >= other.start