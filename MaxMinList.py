def find_max_min(lst):
    max_v = lst[0]        # assume first element is max
    min_v = lst[0]        # assume first element is min
    
    for n in lst:         # go through each number
        if n > max_v:      # check for bigger number
            max_v = n
        if n < min_v:      # check for smaller number
            min_v = n
    
    return max_v,min_v      # return both

print(find_max_min([3,4,9,0,1,99]))     # (99,0)
    
    


  
# output using f-strings or print() with text.    
    
def find_max_min(lst):
    max_v = lst[4]        # assume first element is max
    min_v = lst[4]        # assume first element is min
    
    for n in lst:         # go through each number
        if n > max_v:      # check for bigger number
            max_v = n
        if n < min_v:      # check for smaller number
            min_v = n
    
    return max_v,min_v   

number = [89,34,2,3,77,599]
max_v,min_v = find_max_min(number)

print(f"Max value is {max_v}")
print(f"Min value is {min_v}")



def find_max_min(list):
    return max(list), min(list)

print(find_max_min([29,89,69,79]))