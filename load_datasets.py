#This script just load AMPs sequences from UniProt and plot helicals wheels.

from modlamp.datasets import load_AMPvsUniProt
from modlamp.plot import helical_wheel

data = load_AMPvsUniProt()

def print_sequences():
	for sequence in data.sequences[:10]:
		print(sequence, len(sequence))
		helical_wheel(sequence, colorcoding='charge')

def print_targets():
	for target in data.target:
		print(target)
print_sequences()
print_targets()

