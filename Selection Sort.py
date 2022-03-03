#思路
    #1、设置一个flag，每次循环选出最小的数据，放在当前循环的第一位
    #2、从下一个数据开始，寻出最小的数据，放在当前循环的第一位(相对第一位)

def SelectionSort(arr):
    for i in range(len(arr)-1):
        flag = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                flag = j
        if i != flag:
            arr[i],arr[flag] = arr[flag],arr[i]
    return arr

if __name__ == '__main__':
    a = [12,24,36,25,16]
    b = SelectionSort(a)
    print("排序之前的顺序为：")
    for i in a:
        print(i,end = '\n')
    print("排序之后的顺序为:")
    for i in b:
        print(i,end = '\n')