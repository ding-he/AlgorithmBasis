def quick_sort(array):
    # 基线条件, 0个或1个不需要排序
    if len(array) < 2:
        return array
    # 递归条件
    else:
        # 基准值
        pivot = array[0]
        # 小部分子数组
        less = [i for i in array[1:] if i <= pivot]
        # 大部分子数组
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2, 4, 1, 4, 7, 2, 1, 5, 9, 8, 5]))
