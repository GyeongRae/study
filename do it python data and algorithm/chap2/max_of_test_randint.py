import random  #난수를 사용하기 위한 모듈 import

from max import max_of

print('난수의 최댓값을 구합니다. ')
num = int(input('난수의 개수를 입력하세요'))
mi = int(input('난수의 최솟값을 입력하세요.: '))
ma = int(input('난수의 최댓값을 입력하세요.: '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(mi, ma)

print(f'{(x)}')
print(f'이 가운데 최댓값음 {max_of(x)}입니다.')
