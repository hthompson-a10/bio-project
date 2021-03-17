import glob
import os
import sys


def sequence_gen(lines):
    idx = 1
    while idx < len(lines):
        yield lines[idx].strip('\n')
        idx += 4


def build_percentage_map(fastq_iter):
    percent_map = {}
    for fastq_file in fastq_iter:
        total_seq_cnt = 0
        seq_over_30 = 0
        with open(fastq_file, 'r') as f:
            lines = f.readlines()
            for seq in sequence_gen(lines):
                if len(seq) > 30:
                    seq_over_30 += 1
                total_seq_cnt += 1
        percent_map[fastq_file] = (seq_over_30 / total_seq_cnt) * 100
    return percent_map


def write_to_file(root_dir, output_filepath, percent_map, precision):
    subdir_msg_dict = {}
    for k, v in percent_map.items():
        filename = k.split('/')[-1]
        subdir = k.replace(root_dir, '').replace(filename, '')
        msg = f"{filename}: {v:.{precision}f}% of sequences are greater than 30 nucleotides long"
        if not subdir_msg_dict.get(subdir):
            subdir_msg_dict[subdir] = []
        subdir_msg_dict[subdir].append(msg)

    output = []
    for k in subdir_msg_dict.keys():
        dirpath = os.path.join(root_dir, k)
        output_msg = f"{dirpath}:\n"
        for msg in subdir_msg_dict[k]:
            output_msg += f"\t{msg}\n"
        output.append(output_msg)

    fileout = open(output_filepath, 'w')
    fileout.seek(0)
    fileout.writelines(output)


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: fastq_percentage <directory_containing_fastq_files> "
              "<output_file> [precision]")
    root_dir = sys.argv[1]
    output_filepath = sys.argv[2]
    precision = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    fastq_iter = glob.iglob(os.path.join(root_dir, '**/*.fastq'),
                            recursive=True)
    percent_map = build_percentage_map(fastq_iter)
    write_to_file(root_dir, output_filepath, percent_map, precision)


if __name__ == "__main__":
    main()
