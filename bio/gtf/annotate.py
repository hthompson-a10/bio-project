import sys

from bio.gtf import avl
from bio.gtf import nodes


def _create_annotation_node(line):
    parsed_line = line.split('\t')
    chromosome = parsed_line[0]
    start = int(parsed_line[3])
    end = int(parsed_line[4])
    gene_name = parsed_line[-2].split(';')[4].split(' ')[2].replace('\"', "")
    anno_node = nodes.AnnotationNode(chromosome, start, end, gene_name)
    return anno_node


def _insert_into_map(tree_map, chromosome, gene_block):
    if not tree_map.get(chromosome):
        tree_map[chromosome] = gene_block
    else:
        root = tree_map[chromosome]
        tree_map[chromosome] = avl.AVLGeneTree().insert(root, gene_block)
    return tree_map


def build_tree_map(gtf_filepath):
    tree_map = {}
    lines = []
    with open(gtf_filepath, 'r') as f:
        lines = f.readlines()
        if len(lines) == 0:
            return tree_map

    anno_node = _create_annotation_node(lines[0])
    gene_block = avl.GeneTreeNode(anno_node.start, anno_node.end, anno_node.gene_name)
    gene_block.annotations.append(anno_node)

    for i in range(1, len(lines)):
        anno_node = _create_annotation_node(lines[i])
        if anno_node.start != gene_block.annotations[-1].end:
            # Set the end coordinate of the gene block. Insert gene block into
            # an AVL tree based on chromosome
            gene_block.end = gene_block.annotations[-1].end
            chromosome = gene_block.annotations[-1].chromosome
            tree_map = _insert_into_map(tree_map, chromosome, gene_block)
            # Setup a new gene block
            gene_block = avl.GeneTreeNode(anno_node.start, anno_node.end, anno_node.gene_name)
        gene_block.annotations.append(anno_node)

    # Last line has been reached. Insert block into tree
    gene_block.end = gene_block.annotations[-1].end
    chromosome = gene_block.annotations[-1].chromosome
    tree_map = _insert_into_map(tree_map, chromosome, gene_block)

    return tree_map


def annotate_file(tab_filepath, tree_map):
    with open(tab_filepath, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            parsed_line = lines[i].split('\t')
            root_node = tree_map.get(parsed_line[0])
            if root_node:
                coordinate = int(parsed_line[1][:-1])
                gene_block = avl.AVLGeneTree().search(root_node, coordinate)
                lines[i] = lines[i].replace('\n', '') + f" \t{gene_block.gene_name}\n"
            else:
                lines[i] = lines[i].replace('\n', '') + ' \t\tUNKNOWN\n'
        f.seek(0)
        f.writelines(lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: gtf_annotate <file_to_annotate> "
              "<gtf_file_with_annotations>")

    tab_filepath = sys.argv[1]
    gtf_filepath = sys.argv[2]
    tree_map = build_tree_map(gtf_filepath)
    annotate_file(tab_filepath, tree_map)


if __name__ == "__main__":
    main()
