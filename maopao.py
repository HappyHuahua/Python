arr = input("Input:\n")
kk = [int(n)for n in arr.split()] #这行代表将input进来的数据转为整型数组
num = len(kk)
print(kk)

for i in range(num):
    state = True
    for j in range(num - i - 1):
        if kk[j] > kk[j+1]:
            kk[j], kk[j+1] = kk[j+1], kk[j]
            state = False
    if state:
        break


print(f"Output: \n{kk}")

print(sorted(kk,reverse=True))