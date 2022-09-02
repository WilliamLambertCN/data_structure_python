import time

# print('time cost',time_end-time_start,'s')

def nChooseK(n, k):
    # return 0 #change the code here
    if k > n / 2:
        return nChooseK(n, n - k)
    res = 1
    for i in range(k):
        res = res * (n - k + 1 + i) // (i + 1)
    return res

# print(nChooseK(6,4))

# time_start=time.time()
# rs1 = nChooseK(6,4)
# time_end=time.time()


def nChooseK_recursive(n, k):
    # if k>n/2:
    #     return nChooseK_recursive(n,n-k)
    if k == 0 or n == k:
        return 1
    return nChooseK_recursive(n - 1, k) + nChooseK_recursive(n - 1, k - 1)

# print(nChooseK_recursive(32,16))

import sys

sys.setrecursionlimit(5000000)
print(sys.getrecursionlimit())

time_start = time.time()
i = 20
# while True:
#     time_start = time.time()
#     rs1 = nChooseK_recursive(i, i // 2)
#     time_end = time.time()
#     timecost = time_end - time_start
#     print("nChooseK_recursive({n:d},{k:d}) , within {times:<5.3f} seconds".format(
#             n=i, k=i // 2, times=timecost))
#     if timecost >= 60:
#         break
#     i += 1
# print("nChooseK_recursive({n:d},{k:d}) is {rs:<10.6E}, within {times:<5.2f} seconds".format(
#         n=i, k=i // 2, rs=rs1, times=timecost))
print("nChooseK({n:d},{k:d}) is {rs:<10.6E}".format(
        n=30, k=15, rs=nChooseK(30, 15)))
