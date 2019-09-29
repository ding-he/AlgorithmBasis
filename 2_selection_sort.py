'''
选择法排序
'''
def selection_sort(array):
    new_array = array
    # 每次找出最小值作为第一个数, 总共N次
    for i in range(len(new_array) - 1):
        index = i
        change = False
        # 每次向后寻找N个数
        for j in range(i + 1, len(new_array)):
            if new_array[index] > new_array[j]:
                index = j
                change = True

        # 优化, 交换了才做
        if change:
            new_array[i], new_array[index] = new_array[index], new_array[i]
    
    return new_array


print(selection_sort([2, 4, 1, 0, 7, 3, 5, 9, 2]))
