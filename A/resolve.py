def resolve():
    '''
    code here
    '''
    K = int(input())
    A, B = [int(item) for item in input().split()]

    for i in range(A, B+1):
        if i % K == 0:
            print('OK')
            break
    else:
        print('NG')

if __name__ == "__main__":
    resolve()
