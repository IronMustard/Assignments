print("Hello\n")
AA_masses_dict = {'A' : 71.03711360, 'C' : 103.0091854, 'D' : 115.0269428,
'E' : 129.0425928, 'F' : 147.0684136, 'G' : 57.02146360, 'H' : 137.0589116,
'I' : 113.0840636, 'K' : 128.0949626, 'L' : 113.0840636, 'M' : 131.0404854,
'N' : 114.0429272, 'P': 97.05276360, 'Q' : 128.0585772, 'R' : 156.1011106,
'S' : 87.03202820, 'T' : 101.0476782, 'V' : 99.06841360, 'W' : 186.0793126,
'Y' : 163.0633282}

h2o = 18.010564684
allprotein=list()
badprotein=list()
goodprotein=list()
AAsum = 0

list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]

AA_alphabet = list(AA_masses_dict.keys())

for idx in list_of_protein_dicts:
    for k in idx:
        if k == 'seq':
            #print (k, idx[k])
            b = list()
            if idx[k] not in b:
                b.append(idx[k].upper())
                y = "".join(b)
                allprotein.append(y)
                for char in y:
                    if char not in AA_alphabet:
                        print("Invalid protein:",y,"contains",char)
                        badprotein.append(y)
# print('\n')
# print('badprotein:',badprotein)
# print("\n")
for protein in allprotein:
    if protein not in badprotein:
        goodprotein.append(protein)
        # print("Valid protein:",protein)
# print("\n")
# print('goodprotein:',goodprotein)
# print("\n")

aa_charge_goodprotein = dict()
for i in list_of_protein_dicts:
    if i['seq'].upper() in goodprotein:
        aa_charge_goodprotein[i['seq'].upper()] = i['ch']
# print('aa_charge_goodprotein:',aa_charge_goodprotein)

print('')
for i in goodprotein:
    for letter in i:
        if letter in AA_masses_dict:
            AAsum = AAsum + AA_masses_dict[letter]
            AA_total_mass = AAsum + h2o
            mass2charge = AA_total_mass/aa_charge_goodprotein[i]
    print("Valid protein:",i,"m/z =",mass2charge)
    AAsum = 0
