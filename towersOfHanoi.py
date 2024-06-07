# define function for n blocks, starting on rod 'start' and ending on rod 'end'.
# assumptions: n is positive, three rods (numbered 1, 2 and 3).
def hanoi(n,start,end):
    '''
    Prints step-by-step instructions for solving Towers of Hanoi problem 
    for n number of blocks, moving between 'start' rod and 'end' rod. 
    The 'start' and 'end' rod arguments must be positive integers.
    Assumes 'n' is positive and there are 3 rods (rod 1, rod 2 and rod 3).
    '''

    # validate parameters
    def checkPosInt(n,start,end):
        for arg in [n,start,end]:
            if arg%1 != 0 or arg<=0:
                return 'invalid'
    if checkPosInt(n,start,end)== 'invalid':
        print("Error: all arguments must be positive whole numbers greater than zero.")
        return

    if start == end:
        print("'start' must be different to 'end'")
        return

    for pos in [start, end]:
        if pos not in [1,2,3]:
            print("'start' and 'end' must be 1, 2, or 3.")
            return            

    # print instructions themselves
    if n == 1:
        # base case: only 1 block
        print(f'move top block from {start} to {end}')
        return
    else:
        # declare 'middle' rod variable
        rodOptions = [1,2,3]
        rodOptions.remove(start)
        rodOptions.remove(end)
        middle = rodOptions[0]
        
        # move all-but-base to middle
        hanoi(n-1,start,middle)

        # move base to end
        print(f'move top block from {start} to {end}')

        # move all-but-base to end
        hanoi(n-1,middle,end)
