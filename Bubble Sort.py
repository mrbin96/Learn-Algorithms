#思路：
    #1、每次拿第一个数据往后比较，如果大于后面的数值，就进行更换，交换下来最后一个元素最大
    #2、接着拿第一个元素往后比较，因为上一轮已经交换出最大的数，只需要交换到倒数第二个数
    #其实从上两步就可以看出，涉及到两个循环，包括每轮筛选出最大的数放在最后和跑n-1轮

def BubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    a = [12,24,36,25,16]
    b = BubbleSort(a)
    print("排序之前的顺序为：")
    for i in a:
        print(i,end = '\n')
    print("排序之后的顺序为:")
    for i in b:
        print(i,end = '\n')
