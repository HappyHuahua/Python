arr = input("Input:\n")
kk = [int(n)for n in arr.split()] #这行代表将input进来的数据转为整型数组
num = len(kk)
print(kk)

for i in range(1,num):
    for j in range(i,0,-1):
        if kk[j-1] > kk[j]:
            kk[j-1], kk[j] = kk[j], kk[j-1]
        else:
            break


print(f"Output: \n{kk}")

print(sorted(kk,reverse=True))