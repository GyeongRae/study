from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:

    a = copy.deepcopy(seq) #같은 배열 만들기
    a.append(key) #배열의 끝에 보초 추가

    i = 0
    for i in range(len(a)):
        if (a[i] == key):
            break
        
    return -1 if (i == len(seq)) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하새요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = seq_search(x, ky)

    if (idx == -1):
            print('검색값을 갖는 원소가 존재 x')
    else:
        print(f'검색값은 x[{idx}]')
