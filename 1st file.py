from maths_module import *

#from difflib import get_close_matches as gcm

def response():
    lists = []
    inputs = input('Enter your maths question\n').lower()
    for i in inputs.split():
        try:
            lists.append(float(i))
        except:
            pass
    num1, num2 = float(lists[0]), float(lists[1] if len(lists) == 2 else 0)

    if ("add" in inputs) or ("sum" in inputs) or ("addition" in inputs)  or ("+" in inputs):    
        print(add(num1, num2))
    elif ("subtract" in inputs) or ("minus" in inputs) or ("-" in inputs):
        print(sub(num1, num2))
    elif ("multiply" in inputs) or ("times" in inputs) or ("multipication" in inputs) or ("*" in inputs):    
        print(mul(num1, num2))
    elif "divide" in inputs or ("/" in inputs):
        print(div(num1, num2))
    elif "hcf" in inputs:
        print(hcf(num1, num2))
    elif "lcm" in inputs:
        print(lcm(num1, num2))
    else:
        print('Sorry its beyond my ability')
    


while True:    
    try:
        response()
    except:
        print('Something is wrong!')
        