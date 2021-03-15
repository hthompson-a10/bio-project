import avl
import nodes
import sys


def _create_annotation_node(line):
    parsed_line = line.split('\t')
    chromosome = parsed_line[0]
    start = int(parsed_line[3])
    end = int(parsed_line[4])
    gene_name = parsed_line[-2].split(';')[4].split(' ')[2]
    anno_node = nodes.AnnotationNode(chromosome, start, end, gene_name)
    return anno_node


def build_forest_map(gtf_filepath):
    forest_map = {}
    with open(gtf_filepath, 'r') as f:
        lines = f.readlines()
        anno_node = _create_annotation_node(lines[0])
        gene_block = avl.GeneTreeNode(anno_node.start, anno_node.gene_name)
        gene_block.annotations.append(anno_node)

        for i in range(1, len(lines)):
            anno_node = _create_annotation_node(lines[i])
            if anno_node.gene_name != gene_block.gene_name: # New block has been reached
                # Set the end coordinate of the gene block. Insert gene block into
                # an AVL tree based on chromosome
                gene_block.end = gene_block.annotations[-1].end
                chromosome = gene_block.annotations[-1].chromosome
                if not forest_map.get(chromosome):
                    forest_map[chromosome] = gene_block
                else:
                    root = forest_map[chromosome]
                    forest_map[chromosome] = avl.AVLGeneTree().insert(root, gene_block)
                # Setup a new gene block and overwrite the previous gene name
                gene_block = avl.GeneTreeNode(anno_node.start, anno_node.gene_name)
            gene_block.annotations.append(anno_node)
    return forest_map

def search_coordinate(tab_filepath, forest_map):
    with open(tab_filepath, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            parsed_line = lines[i].split('\t')
            root_node = forest_map.get(parsed_line[0])
            if root_node:
                coordinate = int(parsed_line[1][:-1])
                gene_block = avl.AVLGeneTree().search(root_node, coordinate)
                lines[i] = lines[i].replace('\n', '') + f" \t{gene_block.gene_name}\n"
            else:
                lines[i] = lines[i].replace('\n', '') + ' \t\t"UNKNOWN"\n'
        f.seek(0)
        f.writelines(lines)

def main():
    tab_filepath = sys.argv[1]
    gtf_filepath = sys.argv[2]
    forest_map = build_forest_map(gtf_filepath)
    search_coordinate(tab_filepath, forest_map)

if __name__ == "__main__":
    main()