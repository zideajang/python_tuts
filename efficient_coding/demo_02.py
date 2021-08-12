import time

a_list = []

tic = time.perf_counter()
if not a_list:
    pass
toc = time.perf_counter()
print(toc - tic)

# 1.948000000001615e-06
# 1.39600000000073e-06
# 8.599999999983621e-07