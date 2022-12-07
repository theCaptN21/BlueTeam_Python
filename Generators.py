#Test out this example of using a generator with a range:
def gen_range(stop, start=1, step=1):
    num = start
    while num<= stop:
        yield num
        num += step
#Type python3.7 -i <filename>.py in your terminal, and it should run

#Create a generator with a list:
generator = gen_range(10)
list(generator)
Output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Create a generator using the Fibonacci sequence:
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
#Run the generator: 
fib = gen_fib()
next(fib)
Output = 1
next(fib)
Ouptut = 1
next(fib)
Output = 2
next(fib)
Output = 3
next(fib)
Output = 5
next(fib)
Output = 8
#Create a giant list using the Fibonacci sequence:
fib = gen_fib()
[next(fib) for _ in range(50)][-1]
Output = 12586269025



