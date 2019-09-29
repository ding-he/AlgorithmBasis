def divide_land(height, width):
    # 大者为width, 小者为height
    if height > width:
        temp = height
        height = width
        width = temp
    
    if width % height == 0:
        # 基线条件, 可以完整的分成正方形
        return height
    else:
        # 递归条件, 分而治之
        return divide_land(width % height, height)

def sum_array(array):
    # 基线条件
    if len(array) == 0:
        return 0
    # 递归条件
    else:
        return array[0] + sum_array(array[1:])

print(divide_land(640, 1680))
print(sum_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
