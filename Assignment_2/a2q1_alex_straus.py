from datetime import datetime
from functools import reduce
print("Hello\n")
fname = input('Enter file name\n') # should enter 'cleaned_GPMDB_table.tsv'
if len(fname) < 1:
    fname = 'cleaned_GPMDB_mini.tsv' # smaller version of 'cleaned_GPMDB_table.tsv'
try:
    fhand = open(fname)
except:
    print("Error, could not find",fname)
    quit()

headers = fhand.readline().split()
key1 = headers[1] # = 'date'
key2 = headers[22] # = 'taxon'
# print(key1, key2)
nested_list = []
for row in fhand:
    split_row = row.rstrip().split('\t')
    nested_list.append(split_row)

def dictify(lst):
    dcts_in_a_lst = []
    dicts1 = {}
    dateify = datetime.strptime(lst[1],'%Y:%m:%d:%H:%M:%S')
    if len(lst[22].split(',')) > 1:
        species = lst[22].split(',')
        for animal in species:
            dicts2 = {}
            dicts2[key1] = dateify
            dicts2[key2] = animal
            dcts_in_a_lst.append(dicts2)
    else:
        dicts1[key1] = dateify
        dicts1[key2] = lst[22]
        dcts_in_a_lst.append(dicts1)
    return dcts_in_a_lst

nested_iterator = iter(nested_list)
double_wraplst_of_dicts = list(map(dictify, nested_iterator))
lst_of_dicts = [val for sublist in double_wraplst_of_dicts for val in sublist]
# print(lst_of_dicts)
# print(len(lst_of_dicts))

def filterdates(dctslist):
    low_date = datetime(2010, 6, 1, 0, 0, 0)
    high_date = datetime(2010, 10, 1, 0, 0, 0)
    if dctslist['date'] > low_date and dctslist['date'] < high_date:
        return True
    return False

fltr_iterator = iter(lst_of_dicts)
lst_of_filter_dates_dicts = (list(filter(filterdates, fltr_iterator)))
# print(lst_of_filter_dates_dicts)
# print(len(lst_of_filter_dates_dicts))

def count_taxons(collector, dictto_merge):
    species = dictto_merge['taxon']
    if species not in collector:
        collector[species] = 1
    else:
        collector[species] = collector[species] + 1
    return collector

taxon_count_dict = dict(reduce(count_taxons,lst_of_filter_dates_dicts,{}))
# print(taxon_count_dict)
# print(len(taxon_count_dict))

inverse = [(value, key) for key, value in taxon_count_dict.items()]
print('Most frequent taxon:',max(inverse))
#
fhand.close()
print('\nfile closed!')