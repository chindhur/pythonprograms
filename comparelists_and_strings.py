#to compre 2 lists and return true if atleast one is matching
def compare_lists(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
                return result

#to compare 2 lists and return matching elements
def comparelists(list1,list2):
    matching=[]
    for x in list1:
        if(x in list2):
            matching.append(x)
    return matching

#to compare 2 strings and return the matching elements
def compare_strings(string1,string2):
    matching_char=[]
    for char in string1:
        if char in string2:
            matching_char.append(char)
    return matching_char

print(compare_lists([6,8,9,3],[7,9,2,1]))
print(compare_lists([8,9,7,6],[1,2,3,4]))

match_result=comparelists([78,98,54],[98,54])
print(match_result)

result=compare_strings("hello","world")
print(result)

