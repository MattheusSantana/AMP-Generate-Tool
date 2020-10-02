#This script just calculate and plot aminoacid distribution from all PAMs sequences in APD
# and helicoidal sequences from APD.  

from modlamp.plot import plot_aa_distr 
apd_sequences = open('apd_sequences.txt','r')
helix_sequences = open('helix_apd_sequences.txt', 'r')
all_apd_sequences = list(apd_sequences.readlines())
helix_apd_sequences = list(helix_sequences.readlines())

plot_aa_distr(all_apd_sequences,color='#83AF9B', filename='apd_sequences')
plot_aa_distr(helix_apd_sequences,color='#83AF9B', filename='helix_apd_sequences')
