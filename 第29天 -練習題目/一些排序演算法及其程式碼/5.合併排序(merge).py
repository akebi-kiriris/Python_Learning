def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 合併兩個有序數組
    def merge(l, r):
        merged = []
        i = j = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                merged.append(l[i])
                i += 1
            else:
                merged.append(r[j])
                j += 1
        merged.extend(l[i:])
        merged.extend(r[j:])
        return merged
    
    return merge(left, right)