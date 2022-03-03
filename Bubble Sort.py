#思路：
    #1、每次拿第一个数据往后比较，如果大于后面的数值，就进行更换，交换下来最后一个元素最大
    #2、接着拿第一个元素往后比较，因为上一轮已经交换出最大的数，只需要交换到倒数第二个数

def BubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
a = [12,24,36,25,16]
b = BubbleSort(a)
print(b)
