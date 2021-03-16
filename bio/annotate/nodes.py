class AnnotationNode(object):
    
    def __init__(self, chromosome, start, end,
                 gene_name, annotation=None):
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.gene_name = gene_name


class GeneBlock(object):
    
    def __init__(self, start, gene_name):
        self.start = start
        self.end = None
        self.gene_name = gene_name
        self.annotations = []

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