# Simple numbers
# That application determines simple numbers
# from a line integer numbers, and than you
# can get sum or multiplication of a simple numbers.

my_list = []
my_list_simple = [2]
sam = 0
multi = 1
a = int(input('Enter the beginning of a line: '))
b = int(input('Enter the end of a line: '))
def ferma(a, n):
    '''Ferm's test
    That function testing integer numbers of a line
    and determines simple numbers. And than add simple
    numbers to a list'''
    if (a ** (n - 1)) % n == 1:
        my_list_simple.append(n)
def ferma_list():
    '''Ferm's test
    That function testing integer numbers of a line
    from 'a' to 'b' and defines simple numbers.
    And than add simple numbers to a list'''
    if a > 2:
        del my_list_simple[0]
    for i in range(a, b + 1):
        ferma(i - 2, i)
def sam_add():
    """Calculating simple numbers
    That function summarizes or multiply simple
    numbers from a list simple numbers """
    global sam
    global multi
    for x in my_list_simple:
        sam += x
        multi *= x

ferma_list()
sam_add()
print(my_list_simple)
print(len(my_list_simple))
while True:
    print('''
    1. Sum of all simple numbers of the line
    2. Addition of all simple numbers of the line
    3. Quit''')
    inp = int(input('Enter your choice: \n> '))
    if inp == 1:
        print(sam)
    elif inp == 2:
        print(multi)
    elif inp == 3:
        break
    else:
        print('Incorrect input')

