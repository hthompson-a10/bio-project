import k_heap as heap
import node
import sys

def convert_to_list(seq_dict):
    seq_list = []
    for v in seq_dict.values():
        seq_list.append(v)
    return seq_list


def build_sequence_dict(fasta_filepath):
    seq_dict = {}
    with open(fasta_filepath, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)-1):
            seq_name = lines[i]
            if seq_dict.get(seq_name):
                seq_dict[seq_name].cnt += 1
            else:
                seq = lines[i+1]
                seq_dict[seq_name] = node.SeqNode(seq_name, seq)
    return seq_dict


def main():
    fasta_filepath = sys.argv[1]
    seq_dict = build_sequence_dict(fasta_filepath)
    seq_list = convert_to_list(seq_dict)

    k_heap = heap.KHeap()
    k_heap.build_heap(seq_list, len(seq_list), 9)
    for i in range(0, 9):
        top_node = k_heap.extract_max(seq_list, len(seq_list), 9)
        print(top_node.name)
        print(top_node.seq)
        print(top_node.cnt)

if __name__ == "__main__":
    main()