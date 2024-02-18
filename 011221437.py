# Part 1

adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)]
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0
}



# Part 2

class Node:
    def __init__(self, fName, fParent, fg, fh):
        self.name = fName
        self.parent = fParent
        self.g = fg  # g(n)
        self.h = fh  # h(n)
        self.f = self.h + self.g  # total f(x)



# Part 3

priority_queue = []   # list 

def push_and_sort_priority_queue(node):  # for push and sort  
    priority_queue.append(node)
    priority_queue.sort(key=lambda x: x.f)


NOb = Node('S', None, 0, H['S'])   # source Node 
push_and_sort_priority_queue(NOb)  # insert source


while priority_queue: 
    Nob = priority_queue.pop(0)

    if Nob.name == 'G':
        break

    for i in adjacency_list[Nob.name]:
        new_child = Node(i[0], Nob, Nob.g + i[1], H[i[0]])
        push_and_sort_priority_queue(new_child)



# Part 4

path = []
cost = Nob.g

while Nob.parent is not None:
    path.insert(0, Nob.name)
    Nob = Nob.parent

path.insert(0, Nob.name)

print("Path:", path)
print("Path Cost:", cost)
