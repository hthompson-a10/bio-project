import glob
import math
import os
import sys


def sequence_gen(lines):
    idx = 1
    while idx < len(lines) - 4:
        yield lines[idx]
        idx += 4


def truncate(value, decimal_pos):
    return value - value % (10 ** decimal_pos)


def collect_percents(fastq_iter):
    percents = {}
    for fastq_file in fastq_iter:
        total_seq_cnt = 0
        seq_over_30 = 0
        with open(fastq_file, 'r') as f:
            lines = f.readlines()
            for seq in sequence_gen(lines):
                if len(seq) > 30:
                    seq_over_30 += 1
                total_seq_cnt += 1
        percents[fastq_file] = (seq_over_30 / total_seq_cnt) * 100
    return percents


def build_output_message(root_dir, percents, percision):
    subdir_msg_dict = {}
    for k, v in percents.items():
        filename = k.split('/')[-1]
        subdir = k.replace(root_dir, '').replace(filename, '')
        msg = f"{filename}: {v:.{percision}f}% of sequences have greater than 30 nucleotides"
        if not subdir_msg_dict.get(subdir):
            subdir_msg_dict[subdir] = []
        subdir_msg_dict[subdir].append(msg)

    output_msg = ""
    for k in subdir_msg_dict.keys():
        dirpath = os.path.join(root_dir, k)
        output_msg += f"{dirpath}:\n"
        for msg in subdir_msg_dict[k]:
            output_msg += f"\t{msg}\n"

    return output_msg


def main():
    root_dir = sys.argv[1]
    percision = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    fastq_iter = glob.iglob(os.path.join(root_dir, '**/*.fastq'),
                            recursive=True)
    percentages = collect_percents(fastq_iter)
    print(build_output_message(root_dir, percentages, percision))


if __name__ == "__main__":
    main()