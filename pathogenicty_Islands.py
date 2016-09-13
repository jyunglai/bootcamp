import os


def calculate_GC_Content(seq):
    """Returns the GC content from the sequence"""
    #Error Handling
    if len(seq) == 0:
        RuntimeError("Empty sequence")

    seqUpper = seq.upper()
    numberOfGC = seqUpper.count('G') + seqUpper.count('C')

    return numberOfGC / len(seq)

def gc_blocks(seq, block_size):

    if block_size <= 0:
        RuntimeError("Block size cannot be less than 0")

    #Initialize list for GC Values of each block
    gcValue = []

    tracker = 0
    blockSeq = ''
    for i, base in enumerate(seq):
        print(base)
        if tracker < block_size:
            blockSeq += base
            tracker += 1
            tempBase = base
        else:
            #Reset tracker
            print(blockSeq)
            gcValue.append(calculate_GC_Content(blockSeq))
            tracker = 0
            blockSeq = tempBase

    return tuple(gcValue)
