import random

with open("output.txt", "r") as infile:
    xor_text, flag = infile.readlines()

xor_text = xor_text.split("is: ")[-1].strip()
flag = flag.split("is: ")[-1].strip()

seed = 5985

random.seed(seed)

num_of_swaps = random.randint(10, 100)
num_of_xor_swaps = random.randint(10, 100)

swap_indices = []
xor_indices = [[] for _ in range(num_of_swaps)]

for i, _ in enumerate(range(num_of_swaps)):
    swap_indexA = random.randint(0, len(flag) - 1)
    swap_indexB = random.randint(0, len(flag) - 1)

    swap_indices.append((swap_indexA, swap_indexB))

    for _ in range(num_of_xor_swaps):
        xor_indexA = random.randrange(0, len(flag) - 1, 2)
        xor_indexB = random.randrange(0, len(flag) - 1, 2)

        xor_indices[i].append((xor_indexA, xor_indexB))
        
swap_indices = swap_indices[::-1]
xor_indices = [x[::-1] for x in xor_indices][::-1]

flag = list(flag)
xor_text = list(xor_text)

for i, (swap_indexA, swap_indexB) in enumerate(swap_indices):
    for xor_indexA, xor_indexB in xor_indices[i]:
        
        xor_text[xor_indexA] = chr(ord(flag[xor_indexB]) ^ ord(xor_text[xor_indexA]))
        flag[xor_indexB] = chr(ord(flag[xor_indexB]) ^ ord(xor_text[xor_indexA]))
        
    flag[swap_indexA], flag[swap_indexB] = flag[swap_indexB], flag[swap_indexA]


print("flag is: " + "".join(flag))
print("Original xor text is: " + "".join(xor_text))