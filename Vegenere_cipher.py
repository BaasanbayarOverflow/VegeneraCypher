import os

def find(letter):
    collection = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lcol = len(collection)
    for i in range(lcol):
        if (letter == collection[i]):
          return(i)
    return -1

def put(index):
    collection = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter = collection[index]
    return letter

main_str = input("Enter word:")
main_key = input("Enter key:")

main_str = main_str.upper()
main_key = main_key.upper()

lstr = len(main_str)
lkey = len(main_key)

trans = []
j = 0
for i in range(lstr):
    ind_m = find(main_str[i])
    if (j == lkey):
        j = 0
    ind_k = find(main_key[j])
    if (ind_m == -1):
        let = main_str[i]
    else :
        j += 1
        s_ind = ind_m + ind_k
        if (s_ind >= 26) :
          s_ind = s_ind - 26
        let = put(s_ind)
    trans.append(let)
    
lll = len(trans)
for i in range(lll):
    print(trans[i], end='')

os.system("PAUSE")
