import sys

from bio.fasta import k_heap as heap
from bio.fasta import nodes


def convert_to_list(seq_dict):
    seq_list = []
    for v in seq_dict.values():
        seq_list.append(v)
    return seq_list


def build_sequence_dict(fasta_filepath):
    seq_dict = {}
    with open(fasta_filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        while i < len(lines) - 1:
            seq = lines[i]
            if seq_dict.get(seq):
                seq_dict[seq].cnt += 1
            else:
                seq_dict[seq] = nodes.SeqNode(seq)
            i += 2
    return seq_dict


def build_output_message(seq_list):
    # Use a k-ary heap to do a quick partial sort in O(n) time
    # We use 9-ary as this sets the node as the max the next 9 children as the other most
    # frequent
    k_heap = heap.KHeap()
    k_heap.build_heap(seq_list, len(seq_list), 9)

    output_msg = ""
    for i in range(0, 10):
        seq_node = k_heap.extract_max(seq_list, len(seq_list), 9)
        output_msg += f"Sequence: {seq_node.seq}"
        output_msg += f"Sequence Frequency Count: {seq_node.cnt}\n\n"

    return output_msg


def main():
    fasta_filepath = sys.argv[1]
    seq_dict = build_sequence_dict(fasta_filepath)
    seq_list = convert_to_list(seq_dict)
    output_msg = build_output_message(seq_list)
    print(output_msg)


if __name__ == "__main__":
    main()