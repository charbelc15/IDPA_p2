def position(root, node):
    counter = -1
    for i in root.getiterator():
        counter+=1
        if(i==node):
            return counter