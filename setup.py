from setuptools import setup

setup(name='bio_project',
      version='0.1',
      description='Bio Project',
      url='https://github.com/hthompson-a10/bio_project',
      author='Hunter Thompson',
      author_email='thompson.grey.hunter@gmail.com',
      license='MIT',
      packages=['bio'],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'fastq_percentage = bio.fastq.percentages:main',
            'fasta_frequency = bio.fasta.frequency:main',
            'annotate = bio.annotate.annotate:main'
        ],
      }   
 )
