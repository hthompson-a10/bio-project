from setuptools import setup

setup(name='bio_project',
      version='0.1',
      description='Bio Project',
      url='https://github.com/hthompson-a10/bio-project',
      author='Hunter Thompson',
      author_email='thompson.grey.hunter@gmail.com',
      license='MIT',
      packages=['bio'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'fastq_percentage = bio.fastq.percentages:main',
              'fasta_frequency = bio.fasta.frequency:main',
              'gtf_annotate = bio.gtf.annotate:main'
          ],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ])
