def resolve():
    '''
    code here

    NがBより多きいとき0からBの間の差の最大値が解
    じゃあ、N＜Bの時の第二項は？　→　0となる
    第一項だけ考えればよい
    第一項は単調増加の関数だからNの時かB-1のときに最大となる
    ※Bの時だと一周して0に戻ってしまう

    '''
    A,B,N = [int(item) for item in input().split()]

    def func(x):
        first = int(A * x / B)
        second = A * int(x/B)
        return first - second

    if N >= B:
        print(func(B-1))
    else:
        print(func(N))
        

if __name__ == "__main__":
    resolve()
