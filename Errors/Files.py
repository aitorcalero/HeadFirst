import os
import pickle

DATAPATH = r'sketch.txt'

man = []
other = []

try:
    data = open(DATAPATH)

    for eachline in data:
        try:
            (role,line_spoken) = eachline.split(":",maxsplit=1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as err:
    print('the datafile is missing or something wrong has happened: '+str(err))

try:
    with open('man_data.txt','wb') as man_data:
        pickle.dump(man,man_data)
    with open('other_data.txt','wb') as other_data:
        pickle.dump(other,other_data)
except pickle.PickleError as perr:
    print('Pickling error: '+ str(perr))