def resolve():
    '''
    code here
    '''

    X = int(input())

    is_flag = True
    x = 100
    cnt = 0
    while is_flag:
        cnt += 1
        x *= 1.01
        x = int(x)
        if x >= X:
            is_flag = False

    print(cnt)

if __name__ == "__main__":
    resolve()
