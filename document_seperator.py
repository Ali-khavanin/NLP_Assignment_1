import re
import pickle
import json


def load_var(load_path):
    file = open(load_path, 'rb')
    variable = pickle.load(file)
    file.close()
    return variable


def save_var(save_path, variable):
    print("saving vars ...")
    file = open(save_path, 'wb')
    pickle.dump(variable, file)
    print("variable saved.")
    file.close()


lst_document = []
line = ''
document = ''
with open('hamshahri_2000.txt', 'r') as input_file:
    while True:
        line = input_file.readline()
        document += line
        if line is "":
            break
        if re.findall('\n', line):
            lst_document.append(document)
            document = ''

save_var('all_documents_seperated', lst_document)
#
# dd = load_var('all_documents_seperated')
#
# print(dd[0])
