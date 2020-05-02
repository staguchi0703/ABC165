def resolve():
    '''
    code here
    '''


    N, M, Q = [int(item) for item in input().split()]
    a_list = [[int(item) for item in input().split()] for _ in range(Q)]


    res = 0    
    for item in comb:
        temp_res = 0

        print(item)
        for j in a_list:
            a = j[0]-1
            b = j[1]-1
            c = j[2]
            d = j[3]

            if item[b] -item[a] == c:
                temp_res += d
                print(item[b] , item[a])
                print(b,a)
                print(c,d, '---')

        res = max(res, temp_res)

    print(res)

if __name__ == "__main__":
    resolve()
