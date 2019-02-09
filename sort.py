def mergesort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        l = alist[:mid]
        r = alsit[mid:]
        mergesort(l)
        mergesort(r)

        i = j = k = 0
        # compare and merge 2 sorted list
        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                alist[k] = l[i] # extra buffer list
                i+=1
            else:
                alsit[k] = r[j]
                j+=1
            k+=1
        while i<len(l):
            alist[k] = l[i]
            i+=1
        while j<len(r):
            alist[k] = r[j]
            j+=1

    return alist # return anyway
