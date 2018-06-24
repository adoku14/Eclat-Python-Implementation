
from sys import argv
import sys
from itertools import chain, combinations
kot = 0
FreqItems = dict()
support = dict()
def eclat(prefix, items, dict_id):
    while items:
        i,itids = items.pop()
        isupp = len(itids)
        if isupp >= minsup:

            FreqItems[frozenset(prefix + [i])] = isupp
            suffix = []
            for j, ojtids in items:
                jtids = itids & ojtids
                if len(jtids) >= minsup:
                    suffix.append((j,jtids))

            dict_id += 1
            eclat(prefix+[i], sorted(suffix, key=lambda item: len(item[1]), reverse=True), dict_id)

def rules(FreqItems, confidence):
    Rules = []
    cnt = 0

    for items, support in FreqItems.items():
        if(len(items) > 1):
            lst = list(items)
            antecedent = lst[:len(lst) - 1]
            consequent = lst[-1:]
            
            conf = float(FreqItems[frozenset(items)]/FreqItems[frozenset(antecedent)])
            if (conf >= confidence):
                cnt += 1
                Rules.append((antecedent, consequent, support, conf))

    print('Found %d Rules ' % (cnt))
    return Rules

def print_Frequent_Itemsets(output_freqitems,FreqItems):
    file = open(output_freqitems, 'w+')
    for item, support in FreqItems.items():
        file.write(" {} : {} \n".format(list(item), round(support,4)))




def print_Rules(output_file,Rules):
    file = open(output_file, 'w+')
    for a, b,supp, conf in sorted(Rules):
        file.write("Rule: {} ==> {} : {} : {} \n".format((a), (b), round(supp, 4),round(conf, 4)))
    file.close()

def Read_Data(filename, delimiter=','):
    data = {}
    trans = 0
    f = open(filename, 'r')
    for row in f:
        trans += 1
        for item in row.split(delimiter):
            if item not in data:
                data[item] = set()
            data[item].add(trans)
    f.close()
    return data



if __name__ == "__main__":
    minsup   = int(argv[2])
    confidence = float(argv[3])
    output_FreqItems = argv[4]
    output_Rules = argv[5]
    dict_id = 0
    data = Read_Data(argv[1], ' ') #change the delimiter based on your input file

    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id)
    Rules = rules(FreqItems, confidence)
    print('found %d Frequent items'%len(FreqItems))
    print('Writing Rules .....')
    print_Frequent_Itemsets(output_FreqItems, FreqItems)
    print_Rules(output_Rules, Rules)

