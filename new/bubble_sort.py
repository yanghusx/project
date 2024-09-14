def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(0, len(ls) - i -1):
            if ls[j]<ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls
# a =bubble_sort([3,7,2,5])

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merger_list = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l]< right[r]:
            merger_list.append(left[l])
            l += 1
        else:
            merger_list.append(right[r])
            r += 1
    merger_list.extend(left[l:])
    merger_list.extend(right[r:])
    return merger_list





if __name__ == '__main__':
    a =merge_sort([3,7,2])
    print(a)