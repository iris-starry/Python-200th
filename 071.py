def getPrime(x):
    if x%2 == 0:
        return

    for i in range(3, int(x/2),2):
        if x%i==0:
            break

    else:
        return x

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime, listdata)
print(list(ret))   #[11113,11119]가 출력
