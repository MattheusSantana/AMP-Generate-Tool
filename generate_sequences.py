from modlamp.sequences import Helices
from modlamp.plot import helical_wheel

h = Helices(5,7,21)
h.generate_sequences()

for sequence in h.sequences:
	print(sequence)
	helical_wheel(sequence , colorcoding='charge')