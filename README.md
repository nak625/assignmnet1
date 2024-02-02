# Python Project README

## Overview
This Python project consists of two main files, `fib.py` and `echo.py`, each serving distinct purposes related to Fibonacci calculations and simulating an echo effect.

### 1. `fib.py`
- Calculates Fibonacci numbers using recursion and memoization.
- Measures the execution time of each calculation.
- Plots the results using Matplotlib.
- Screenshot of my code, there is an issue 75% of the way through the sequence. Assumed to be a hardware issue.
![fib](https://github.com/nak625/assignmnet1/assets/123668402/cf073dba-2eee-4fc1-90c6-4ee1b90a52e6)


   ```bash
   Sample Output:
   Finished in 0.00000000s : f(2) -> 2
   Finished in 0.00000000s : f(1) -> 1   
   Finished in 0.00000000s : f(3) -> 3   
   Finished in 0.00000000s : f(4) -> 5   
   Finished in 0.00049973s : f(5) -> 8   
   Finished in 0.00049973s : f(6) -> 13  
   Finished in 0.00049973s : f(7) -> 21  
   Finished in 0.00049973s : f(8) -> 34  
   Finished in 0.00049973s : f(9) -> 55  
   .....
   Finished in 0.00500417s : f(74) -> 2111485077978050
   Finished in 0.00500417s : f(75) -> 3416454622906707
   Finished in 0.00500417s : f(76) -> 5527939700884757
   Finished in 0.01501298s : f(77) -> 8944394323791464
   Finished in 0.01551294s : f(78) -> 14472334024676221
   Finished in 0.01551294s : f(79) -> 23416728348467685
   Finished in 0.01551294s : f(80) -> 37889062373143906
   .....
   Finished in 0.01701450s : f(98) -> 218922995834555169026
   Finished in 0.01701450s : f(99) -> 354224848179261915075
   Finished in 0.01701450s : f(100) -> 573147844013817084101
   
-The graph x is Fib(number) y is time it finished in.

![Figure_1](https://github.com/nak625/assignmnet1/assets/123668402/1867062a-742f-4124-a72d-e04e2d8eae3c)

### 2. `echo.py`
- Implements a function `echo` to simulate a real-world echo effect.
- Limited to 3 repetitions.
-Here is the screenshot of the code as well as sample output.
![echo](https://github.com/nak625/assignmnet1/assets/123668402/dc2fef8a-70b6-4803-912e-13cc904384d1)

## Usage
1. Run the scripts using a Python interpreter.
   ```bash
   python fib.py
   python echo.py
