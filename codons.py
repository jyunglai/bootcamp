#Taking input from the command line
codon = input('Input your codon:')

codonList = ['UAA', 'UAG', 'UGA']

#Sample Switch statement using if and elif
if codon == "AUG":
    print('This codon is the start codon.')
elif codon in codonList:
    print('This codon is not the start codon.')
else:
    print('None of the above')
