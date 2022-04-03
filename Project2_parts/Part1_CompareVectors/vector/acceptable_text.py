import re

#   iii, aaa, ??, ?, ... not acceptable
#   charbel?    acceptable

def acceptable_text(text):

    if len(text)==0:
        return False

    special_characters=['[','@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','}','{','~',':',']','a','i','\\']
    Flags = []
    #regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]ai')
    for char in text:
        if char in special_characters:
            Flags.append(False)
        else:
            Flags.append(True)

    #print(Flags)
    if True in Flags:
        return True
    else:
        return False    