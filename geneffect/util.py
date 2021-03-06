from __future__ import absolute_import, division, print_function

import sys
import os
from collections import defaultdict
from datetime import datetime

from Bio.Seq import Seq
from Bio.Alphabet import Alphabet
from Bio.Data import CodonTable


### Project Functions ###

def log(message):
    print('GENEFFECT|PID-%s [%s]: %s' % (os.getpid(), datetime.now(), message))
    sys.stdout.flush()


### General Helper Functions ###

def append_if_not_none(list, element):
    if element is not None:
        list += [element]
        
def get_unique_or_none(collection):
    if len(collection) == 1:
        element, = list(collection)
        return element
    else:
        return None


### Biopython Helper Functions ###

def as_biopython_seq(seq):
    if isinstance(seq, Seq):
        return seq
    elif isinstance(seq, str):
        return Seq(seq, Alphabet())
    else:
        raise Exception('Cannot resolve type %s as Biopython Seq' % type(seq))
    
def codon_to_aa(codon, codon_table = 'Standard'):

    codon_table = CodonTable.unambiguous_dna_by_name[codon_table]

    if codon in codon_table.stop_codons:
        return as_biopython_seq('*')
    else:
        return as_biopython_seq(codon_table.forward_table[codon])
