collection = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def find(letter):
    len_col = len(collection)
    for i in range(len_col):
        if (letter == collection[i]):
            return i;    
    return -1

def put_letter(index):
    letter = collection[index]
    return letter

main_script = input("Enter script: ")
main_key = input("Enter key: ")

main_script = main_script.upper()
main_key = main_key.upper()

length_script = len(main_script)
length_key  = len(main_key)

decoded = []   

if (main_key != None or main_key.rstrip() != "" or main_key != " "):
    j = 0
    for i in range(length_script):
        main_src_index = find(main_script[i])
        if (main_src_index != -1):
            if (j == length_key):
                j = 0
            main_key_index = find(main_key[j])
            j += 1
            main_src_index -= main_key_index
            if (main_src_index < 0):
                main_src_index += 26
            main_letter = put_letter(main_src_index)
        else:
            main_letter = main_script[i]
        decoded.append(main_letter)          
else:
    print("Error! Key is empty")

for i in range(len(decoded)):
    print(decoded[i], end="")
