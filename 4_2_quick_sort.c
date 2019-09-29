#include <stdio.h>

void quickSort(int *array, int low, int high)
{
	int lowIndex = low;
	int highIndex = high;
	int key = array[low];
	
	// 基线条件
	if(low >= high)
	{
		return;
	}
	
	while(low < high)
	{
		// 先找到右边第一个不满足的
		while(low < high && key <= array[high])
			high--;
		
		// 与左边数组交换
		if(key > array[high])
		{
			array[low] = array[high];
			low++;
		}
		
		// 找到左边第一个不满足的
		while(low < high && key >= array[low])
			low++;
		
		// 与右边数组交换
		if(key < array[low])
		{
			array[high] = array[low];
			high--;
		}
	}
	
	// 将基数插回数组中
	array[low] = key;
	quickSort(array, lowIndex, low - 1);
	quickSort(array, low + 1, highIndex);
}


int main()
{
	int array[] = {2, 4, 1, 6, 7, 8, 0, 5, 3, 9};
	int len = sizeof(array) / sizeof(int);
	int i;
	
	for(i = 0; i < len; i++)
		printf("%d ", array[i]);
	printf("\n");
	
	quickSort(array, 0, len - 1);
	
	for(i = 0; i < len; i++)
		printf("%d ", array[i]);
	printf("\n");
}
