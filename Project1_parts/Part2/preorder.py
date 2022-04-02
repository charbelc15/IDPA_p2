import xml.etree.ElementTree as ET

def preorder(root):

    if root is None:
        return [] 
    ans = [root] #We can add .tag to root but it WILL BECOME A STRINGS array
    for x in root:
        ans += preorder(x)        
    return ans