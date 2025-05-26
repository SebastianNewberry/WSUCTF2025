import random
from secret import flag

xor_text = "Wayne State offers excellence in Detroit!"

seed = 5985

random.seed(seed)

num_of_swaps = random.randint(10, 100)
num_of_xor_swaps = random.randint(10, 100)

flag = list(flag)
xor_text = list(xor_text)

swap_indices = []
xor_indices = []

for _ in range(num_of_swaps):
    indexA = random.randint(0, len(flag) - 1)
    indexB = random.randint(0, len(flag) - 1)

    flag[indexA], flag[indexB] = flag[indexB], flag[indexA]

    for _ in range(num_of_xor_swaps):
        indexA = random.randrange(0, len(flag) - 1, 2)
        indexB = random.randrange(0, len(flag) - 1, 2)

        flag[indexB] = chr(ord(flag[indexB]) ^ ord(xor_text[indexA]))
        xor_text[indexA] = chr(ord(flag[indexB]) ^ ord(xor_text[indexA]))
            

with open("output.txt", "w+") as outfile:
    outfile.write("xor text is: " + "".join(xor_text) + "\n")
    outfile.write("output flag is: " + "".join(flag))