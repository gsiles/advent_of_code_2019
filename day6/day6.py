import re

def read_puzzle_input():
    input_file = open("puzzle_input.txt")
    puzzle_input = input_file.read()
    input_file.close()
    return puzzle_input.strip().split("\n")

def parent_child(data):
    array = []
    for element in data:
        array.append(element.split(")"))
    return array

def get_childs(parent):
    # return array with childs
    indices = [i for i, x in enumerate(data) if x[0] == parent ]
    childs = []
    for i in indices:
        childs.append(data[i][1])
    return childs

def get_tree(root):
    tree = [[root]]           #each position is a level
    childs = get_childs(root)
    if childs:
        tree.append(childs)
        end = False
        while (not end):
            level = []
            for element in childs:
                level.extend(get_childs(element))
            if level:
                childs = level
                tree.append(level)
            else:
                end = True
    return tree


data1 = read_puzzle_input()
data = parent_child(data1)
tree = get_tree("COM")

#Part1
suma = 0
for i in range(len(tree)):
    suma = suma + i*len(tree[i])
print(suma)



#Part2
def get_parents(node):
    parents = []
    while(not node == "COM"):
        aux = [x for x in data if x[1] == node ]
        node = aux[0][0]
        parents.append(node)
    return parents

you_path = get_parents("YOU")
san_path = get_parents("SAN")
while(you_path[-1] == san_path[-1]):
    del you_path[-1]
    del san_path[-1]
print(len(you_path)+len(san_path))
