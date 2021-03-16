import sys

from bio.fasta import d_heap
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
        while i < len(lines):
            seq = lines[i].strip('\n')
            if seq_dict.get(seq):
                seq_dict[seq].cnt += 1
            else:
                seq_dict[seq] = nodes.SeqNode(seq)
            i += 2
    return seq_dict


def build_output_message(seq_list):
    """
    This function leverages a heap to partially sort the data. Only the top 10
    sequences are of concern, so the rest of the data can be ignored. A
    4-ary heap is used as it tends to perform better than a binary heap 
    when working with large datasets due to caching behavior.
    """
    heap = d_heap.DHeap()
    heap.build_heap(seq_list, len(seq_list), 4)

    output_msg = ""
    for i in range(0, min(10, len(seq_list))):
        seq_node = heap.extract_max(seq_list, len(seq_list), 4)
        #output_msg += f"Sequence: {seq_node.seq}\n"
        #output_msg += f"Sequence Frequency Count: {seq_node.cnt}\n\n"
    return output_msg


def main():
    fasta_filepath = sys.argv[1]
    seq_dict = build_sequence_dict(fasta_filepath)
    seq_list = convert_to_list(seq_dict)

    import timeit
    starttime = timeit.default_timer()
    #seq_list = seq_list.sort(key=lambda x: x.cnt)
    build_output_message(seq_list)
    print("The time difference is :", timeit.default_timer() - starttime)

    
    #print(output_msg)


if __name__ == "__main__":
    main()