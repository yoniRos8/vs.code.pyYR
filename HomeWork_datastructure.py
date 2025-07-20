#1
def get_value(dictionary,key):
    if(key in dictionary):
        print(key)
    else:
        print("Error!")

my_dict={"name":"yoni","age":17,"id":"33156784"}
get_value(my_dict,"yo")

#2
def union_sets(set1,set2):
    set1=set(set1)
    set2=set(set2)
    return set1.union(set2)

set1={2,1,5,7,"y"}
set2={2,3,6,1}
print(union_sets(set1,set2))

#3
def count_value_in_tuples(tuple_list):
 
    count_dict={}
    for tup in tuple_list:
        for val in tup:
            if(val in count_dict):
                count_dict[val]+=1
            else:
                count_dict[val]=1
            
    return count_dict


list1=[("a","b"),("a","c"),("d","b"),("e","f"),("a","b")]
print(count_value_in_tuples(list1))


       

