from max import max_of 

t = (4, 7, 5.6, 2, 3.14, 1)
s ='string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다. ') #튜플의 최댓값 찾기
print(f'{s}의 최댓값은 {max_of(s)}입니다.')  #문자열의 최댓값 찾기 
print(f'{a}의 최댓값은 {max_of(a)}입니다. ') # 리스트의 최댓값 찾기
