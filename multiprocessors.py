import time
import multiprocessing

processes = [] # leave this empty
processorNum = 10 # number of running multiprocessors
 
def func(): # your function
    print(True)
    
# multiprocessors
for processorID in range(processorNum):
    p = multiprocessing.Process(target = , args = []) # input your function (without "()") and arguments
    if __name__ == '__main__':
        p.start() # starts the multiprocessor
        processes.append(p) # appends to processes list
for p in processes:
    p.join() # joins each multiprocessor in list to stop code from moving forward unless all are done

print(f"Finished running after : {time.perf_counter}")

