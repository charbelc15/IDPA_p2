# Hanndle multiple nested levels of tags.
# Does Not delete while forward iterating --> Doesnt l break if multiple xml tags are deleted in the same level one-after-another.
def delete(root, node, nested=False):
    if(root==node):
        root.clear()
    for child in (root.iter()):
        if nested:
            if len(child) >= 1:
                delete(child,node)
        if child==node:  
            child.getparent().remove(child)
  