BRACKETS = {'{' : '}', '(' : ')', '[' : ']'}

def checkio(expression):
    brackets_list = []
    for char in expression:
        if char in BRACKETS.keys():
            brackets_list.append(char)
        elif char in BRACKETS.values():
            if len(brackets_list) and (brackets_list[len(brackets_list) - 1] == BRACKETS.keys()[BRACKETS.values().index(char)]):
                brackets_list.pop()
            else:
                return False
    if brackets_list:
        return False
    else:
        return True
            
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
