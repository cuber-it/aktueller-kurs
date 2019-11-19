import sys
#import thesaurus as theo

#daten = theo.read_data("openthesaurus.txt")
#t = theo.build_thesaurus(daten)
#theo.suche_worte(t)

#from thesaurus import read_data
from thesaurus import *

daten = read_data("openthesaurus.txt")
t = build_thesaurus(daten)
suche_worte(t)
