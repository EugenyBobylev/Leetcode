from typing import List

def checkIfExist(arr: List[int]) -> bool:
    res = [n for n in arr if (n + n) in arr]
    if len(res) > 0 and 0 in res:
        res.remove(0)
    print(res)
    return len(res) > 0

if __name__ == '__main__':
    data_1 = [10,2,5,3]
    data_2 = [3,1,7,11]
    data_3 = [-2,0,10,-19,4,6,-8]
    data_4 = [0, 0]
    res = checkIfExist(data_4)
    print(res)
