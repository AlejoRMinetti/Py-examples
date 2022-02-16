import time

print("Seconds counter")

for i in range(5):
    time.sleep(1) # sleep for 1s
    print(i)

# execution speed
start_time = time.time()
# your code
elapsed_time = time.time() - start_time
print("time for execution of non code: ",elapsed_time,"s")