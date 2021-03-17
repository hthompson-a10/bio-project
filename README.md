# Bio

## Installation

Download from github
```
git clone git@github.com:hthompson-a10/bio-project.git
cd bio-project
pip3 install -e .
```

## FASTQ Percentage

### Usage
```
fastq_percentage <directory_containing_fastq_files> <output_file> [precision]
```

### Sample of output file contents

```
$ fastq_percentage bio-project/tests/fixtures/fastq/ out.txt

$ cat out.txt
bio-project/tests/fixtures/fastq/read1/:
        Sample_R1.fastq: 81% of sequences are greater than 30 nucleotides long
bio-project/tests/fixtures/fastq/read2/:
        Sample_R2.fastq: 84% of sequences are greater than 30 nucleotides long
```

With increased precision (10 decimal points)

```
$ fastq_percentage bio-project/tests/fixtures/fastq/ out.txt 10

$ cat out.txt
bio-project/tests/fixtures/fastq/read1/:
        Sample_R1.fastq: 80.6424344886% of sequences are greater than 30 nucleotides long
bio-project/tests/fixtures/fastq/read2/:
        Sample_R2.fastq: 83.6010143702% of sequences are greater than 30 nucleotides long
```

## FASTA Top 10 Sequences

### Usage
```
fasta_frequency <fasta_file> <output_file>
```

### Sample of output file contents

```
$ fasta_frequency bio-project/tests/fixtures/fasta/sample.fasta out.txt

$ cat out.txt
Sequence: CGCGCAGGCTGAAGTAGTTACGCCCCTGTAAAGGAATCTATGGACAATGGAACGAACA
Sequence Count: 28

Sequence: TGTTCTGAGTCAAATGATATTAACTATGCTTATCACATATTATAAAAGACCGTGGACATTCATCTTTAGTGTGTCTCCCTCTTCCTACT
Sequence Count: 27

Sequence: CTCAATCTGCCAAGACCATAGATCCTCTCTTACTGTCAGCTCATCCGGTGAGGCC
Sequence Count: 22
```

## GTF Annotation

### Usage
```
gtf_annotate <file_to_annotate> <gtf_file_with_annotations>
```

### Sample of output file contents

```
$ gtf_annotate bio-project/tests/fixtures/annotate/coordinates_to_annotate.txt bio-project/tests/fixtures/gtf/hg19_annotations.gtf

$ cat coordinates_to_annotate.txt
chr12	20704380 	PDE3A
chr12	20704379 	PDE3A
chr21	9827238 	UNKNOWN
chr5	71146882 	UNKNOWN
chr8	38283717 	FGFR1
chr12	20704371 	PDE3A
chr12	20704377 	PDE3A
```
