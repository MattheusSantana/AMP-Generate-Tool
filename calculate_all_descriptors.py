from modlamp.descriptors import GlobalDescriptor
#apd_sequences_file = open('apd_sequences.txt','r')
#apd_sequences = list(apd_sequences_file.readlines())

helix_apd_sequences_file = open('helix_apd_sequences.txt','r')
helix_sequences = list(helix_apd_sequences_file.readlines())

#descriptor = GlobalDescriptor(apd_sequences)
descriptor = GlobalDescriptor(helix_sequences)
descriptor.calculate_all(amide=True)
print(descriptor.featurenames)
descriptor.save_descriptor('helix_sequences_all_descriptors.csv')