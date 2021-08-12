import time
val = True

tic = time.perf_counter()
if val:
    pass
toc = time.perf_counter()
print(toc - tic)

# 5.075999999999692e-06
# 7.430000000044346e-07
# 6.690000000017515e-07

