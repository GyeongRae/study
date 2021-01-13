def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환')
    
    while True:
        while True:
            n = int(input('변환 할 값으로 음이 아닌 정수 입력'))
            if n > 0:
                break
                
                
        while True:
            con = int(input('어떤 징수로 변환?'))
            if 2<= con <= 36:
                break
    
        print(f'{con}진수로는 {card_conv(n, con)}입니다')
    
        retry = input('한번 더 변환? (y = 예/ n = 아니오): ')
        if retry in {'N', 'n'}:
                break