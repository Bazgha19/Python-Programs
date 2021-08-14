# Binary Search

'''
def binary_search(list,item):
    low=0
    high=len(list)-1
    
    while low<=high:
        mid=(low+high)
        guess=list[mid]
        if guess==item:
            return mid
        if guess >item:
            high=mid-1
        else:
            low=mid+1
    return None

l=[1,3,5,7,9]
print(binary_search(l,3))
print(binary_search(l,-1))

'''

'''
def binary_search(list,item):
    low=0
    high=len(list)-1
    
    while low<=high:
        mid=(low+high)//2
        if list[mid]==item:
           return "Found at index", mid
            
        elif list[mid]<item:
            low=mid+1
            "Found at index", low
        else:
            high=mid-1
            "Found at index",high
    return "Element Not Found"
    
    
    
list=[1,2,23,4,52,67,3,5]
list.sort()
item=int(input())
print(binary_search(list,item))


'''


























