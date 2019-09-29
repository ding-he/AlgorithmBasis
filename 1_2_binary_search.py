'''
二分查找(升序)
返回查找位置
'''
def binary_search(array, key):
    # low, high指针指向两头
    low = 0
    high = len(array) - 1
    while low <= high:
        # 计算中间的参与比较
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            # key出现在(mid, high]之间
            # 调整low 
            low = mid + 1
        else:
            # key出现在[low, mid)之间
            # 调整high
            high = mid - 1
    
    # 找不到返回None
    return None

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(array)
print(binary_search(array, 8))
print(binary_search(array, 2))
print(binary_search(array, 12))
