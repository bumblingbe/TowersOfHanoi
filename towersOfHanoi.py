def hanoi(n,start,end):
    if n == 1:
        print(f'move top block from {start} to {end}')
        return
    else:
        #declare 'middle' rod option
        rodOptions = [1,2,3]
        rodOptions.remove(start)
        rodOptions.remove(end)
        middle = rodOptions[0]
        
        #move all-but-base to middle
        hanoi(n-1,start,middle)

        #move base to end
        print(f'move top block from {start} to {end}')

        #move all-but-base to end
        hanoi(n-1,middle,end)
