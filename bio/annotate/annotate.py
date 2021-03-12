import sys
import avl

def _create_annotation_node(self, parsed_line):
    chromosome = parsed_line[0]
    start = int(parsed_line[3])
    end = int(parsed_line[4])
    gene_name = parsed_line[-2].split(';')[4].split(' ')[1]
    anno_node = AnnotationNode(start, end, gene_name, lines[i])
    return anno_node


def build_forest_map(gtf_filepath):
    forest_map = {}
    with open(gtf_filepath, 'r') as f:
        gene_block = None
        lines = f.readlines()
        for i in range(0, len(lines)):
            parsed_line = lines[i].split('\t')
            anno_node = self._create_annotation_node(parsed_line)
            if anno_node.gene_name != gene_block.gene_name: # New block has been reached
                if gene_block != None:
                    # Set the end coordinate of the gene block. Insert gene block into
                    # an AVL tree based on chromosome
                    gene_block.end = gene_block.annotations[-1].end
                    if not forest_map.get(chromosome):
                        forest_map[chromosome] = new avl.AVLGeneTree()
                    forest_map[chromosome].insert(gene_block)
                # Setup a new gene block and overwrite the previous gene name
                gene_block = avl.GeneTreeNode(start, gene_name)
                prev_name = gene_name
            gene_block.annotations.append(anno_node)
    return forest_map

def search_coordinate(tab_filepath):
    pass

def main():
    tab_filepath = sys.argv[1]
    gtf_filepath = sys.argv[2]
    forest_map = build_forest_map(gtf_filepath)

    #annotation = root.binary_search(0, len(root.annotations)-1, coordinate)

if __name__ == "__main__":
    main()