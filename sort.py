def mergesort(alist):
    # base case
    if len(alist) <= 1:
        return alist
    mid = len(alist)//2
    l = mergesort(alist[:mid])
    r = mergesort(alsit[mid:])
    return merge(left,right) # follow base case format

def merge(left,right): # both left, right are sorted list
    temp = []
    while left and right:
        if left[0] < right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    temp += left + right # in case any sublist has value not been merged
    return temp

    # interative way to merge 2 sublists:
    #
    #     i = j = k = 0
    #     while i<len(l) and j<len(r):
    #         if l[i]>r[j]:
    #             alist[k] = l[i]
    #             i+=1
    #         else:
    #             alsit[k] = r[j]
    #             j+=1
    #         k+=1
    #     while i<len(l):
    #         alist[k] = l[i]
    #         i+=1
    #     while j<len(r):
    #         alist[k] = r[j]
    #         j+=1
    #
    # return alist
