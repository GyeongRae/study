from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """함수 어노테이션 직관적으로 함수의 매개변수 사용방안을 알 수 있음"""
    maximum = a[0]
    for i in range(1, len(a)): #배열의 최댓값을 구하는 반복문
         if a[i] > maximum: 
            maximum = a[i]
    return maximum

if __name__ == '__main__': ##모듈 객체로 name은 모듈 객체의 이름 변수
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')