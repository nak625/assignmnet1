#fib.py
#3980 SP24
#nknosp
#Assignment1 Python refresher

import time 
from functools import lru_cache
import matplotlib.pyplot as plt

# Global 2D array to store results [n, result, execution_time]
result_array = []

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        runtime = (t2-t1) 
        print(f"Finished in {(runtime):.8f}s : f({args[0]}) -> {result}")
        result_array.append([args[0], (runtime)])  # Append values to the global array
        return result
    return wrap_func

@lru_cache
@timer
def fib(n: int) -> int:
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)
    
if __name__ == "__main__":
    fib(100)
    
    '''Creates a plot of the results that pops up when plt.show runs'''
    x_values = [entry[0] for entry in result_array]
    y_values = [entry[1] for entry in result_array]

    plt.plot(x_values, y_values, marker='o')
    plt.title('Fibonacci sequence')
    plt.xlabel('Fibonacci Number')
    plt.ylabel('Time')
    plt.show()