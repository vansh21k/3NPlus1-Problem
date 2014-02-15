'''Solution to 3n+1 problem posted here: http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110101&format=html '''
def getCycles(n):
    ''' returns cycle length for integer n'''
    if n == 1:
        return 1
    elif n%2 == 1:
        return 1 + getCycles(3 * n + 1)
    else:
        return 1 + getCycles(n/2)
        
inp = raw_input("Enter 2 numbers seperated by space\n")
a,b = inp.strip().split(' ')
a = int(a)
b = int(b)
if (a > b):
    a,b = b,a #Swaps integers, a should be lesser than b
max_cycle, cur_cycle = 0, 0 #max_cycle to keep state of current max, cur_cycle to keep state of current
for i in range(a,b+1):
    cur_cycle = getCycles(i)
    if cur_cycle > max_cycle:
        max_cycle = cur_cycle
print max_cycle
