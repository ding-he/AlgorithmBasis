'''
问题:
	假设你是个小偷，背着一个可装 4磅东西的背包. 可以盗窃5件商品
		1. 音响 3000元 4磅
		2. 笔记本电脑 2000元 3磅
		3. 吉他 1500元 1磅
		4. iPhone 2000元 1磅
		5. MP3 1000元 1磅
偷到的钱最高?
'''


def init_steal():
    product['guitar'] = {}
    product['guitar']['value'] = 1500
    product['guitar']['weight'] = 1

    product['sound'] = {}
    product['sound']['value'] = 3000
    product['sound']['weight'] = 4

    product['PC'] = {}
    product['PC']['value'] = 2000
    product['PC']['weight'] = 3

    product['iPhone'] = {}
    product['iPhone']['value'] = 2000
    product['iPhone']['weight'] = 1

    product['MP3'] = {}
    product['MP3']['value'] = 1000
    product['MP3']['weight'] = 1

    space = totalWeight
    for p in product:
        if product[p]['weight'] < space:
            space = product[p]['weight']

    for i in range(space, totalWeight, space):
        weight.append(i)
    weight.append(totalWeight)

    for i in range(len(product)):
        map.append([])
        for j in range(len(weight)):
            map[i].append({})
            map[i][j]['value'] = 0
            map[i][j]['product'] = set()


def max_value():
    indexi = 0
    indexj = 0
    value = 0
    for i, p in enumerate(product):
        # 对每一行进行更新
        for j, w in enumerate(weight):
            # 更新每一列
            # 先计算上一个留下来的值
            last_product = set()
            if i == 0:
                last_value = 0
            else:
                last_value = map[i - 1][j]['value']
                last_product |= map[i - 1][j]['product']

            # 计算本次的值
            current_value = 0
            current_product = set()
            if w >= product[p]['weight']:
                current_value = product[p]['value']
                current_product.add(p)
                remain_weight = w - product[p]['weight']
                if remain_weight > 0:
                    if i != 0 and j != 0:
                        current_value += map[i - 1][remain_weight - 1]['value']
                        current_product |= map[i - 1][remain_weight - 1]['product']

            if last_value >= current_value:
                map[i][j]['value'] = last_value
                map[i][j]['product'] = last_product
            else:
                map[i][j]['value'] = current_value
                map[i][j]['product'] = current_product

            # 记录最大值
            if value < map[i][j]['value']:
                value = map[i][j]['value']
                indexi = i
                indexj = j

    return map[indexi][indexj]['product'], map[indexi][indexj]['value']


totalWeight = 4
product = {}
weight = []
map = []
init_steal()
category, value = max_value()
print(category)
print(value)
