import re
import numpy as np
"""
This Algorithm will take an input string (e.g: "Hello World") and creates a Binary Tree which
encrypts string using this Tree. First output contains Binary Code for every character we have,
Second (optional) output contains the Decryption of binary input and decrypts it (e.g: 101 = hi).
"""

# String will be converted into lowercase, spaces and non alphabetical characters will be removed.
s = input("Enter the string for Encryption: ").lower().replace(" ", "")
s = re.sub(r'[^a-z]', '', s)

class Huffman:

    def __init__(self, encryption_string):
        self.encryption_string = encryption_string

    def CharactersCount(self, encryption_string):
        """
        This function counts every character (e.g: a) and stores it.
        """
        total = {}
        for i in encryption_string:
            total[i] = encryption_string.count(i)
        print("\nNumber of repeats = " + str(total))
        return total

    def BuildTree(self, encryption_string):
        """
        This function creates a tree-like matrix which
        contains the binary tree from bottom to top.
        First row of matrix declares connection between vertices.
        """

        total_number = self.CharactersCount(encryption_string)
        total = total_number
        codes = total_number
        codes = dict.fromkeys(codes, '')
        tree = np.zeros(shape=(len(total), 3), dtype=np)
        tree[0, 0] = 'None'
        tree[0, 1] = '0'
        tree[0, 2] = '1'

        print("\nThe binary tree is = ")
        for i in range(1, len(total)):

            minimum_key1 = min(total, key=total.get)
            minimum_value1 = min(total.values())
            total.pop(minimum_key1)
            tree[i, 1] = minimum_key1 + "=" + str(minimum_value1)

            minimum_key2 = min(total, key=total.get)
            minimum_value2 = min(total.values())
            total.pop(minimum_key2)
            tree[i, 2] = minimum_key2 + "=" + str(minimum_value2)

            tree[i, 0] = minimum_key1 + minimum_key2 + "=" + str(minimum_value1 + minimum_value2)
            total[minimum_key1 + minimum_key2] = minimum_value1 + minimum_value2

            print(tree[i, 0] + " , " + tree[i, 1] + " , " + tree[i, 2])

        for ch in codes.keys():
            for i in range(len(codes)-1, 0, -1):
                if ch in tree[i, 1]:
                    codes[ch] = codes[ch] + '0'
                elif ch in tree[i, 2]:
                    codes[ch] = codes[ch] + '1'
        print("\nCodes for each character are = ", codes)

        return codes

    def Decryption(self, codes):
        """
        This function decrypts based on codes that achived previously
        """
        main_var = input("\nEnter the code for decryption = ")
        key_list = list(codes.keys())
        value_list = list(codes.values())

        answer = ''
        var = main_var
        for i in range(len(main_var)-1):
            for c in value_list:
                position = value_list.index(c)
                if var.startswith(c):
                    answer = answer + key_list[position]
                    var = var[len(c):]
        print("\nDecrypted code is equal to = ", answer)


# Call The Class
obj = Huffman(s)
codes = obj.BuildTree(s)

while (True):
    d = input("\nEnter '1' for decryption or '0' for terminating the program : ")
    if d == '1':
        obj.Decryption(codes)
    elif d == '0':
        break
    else:
        print("\nJust enter 1 or 0 !!!")
