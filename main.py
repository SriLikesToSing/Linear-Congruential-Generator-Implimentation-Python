#LCG algorithm implimentation


#how do you compress numbers?

def generate(m, a, c, X0, length):
    list = [X0]
    length+=1
    for x in range(1, length):
        list.append((a*list[x-1])%m)

    return list





list = generate(2**32, 1664525, 1013904223, 1,  5)

for x in list:
    print(x)

#ti-84
    '''
        - given range of values to be generated in
            - gives a number using an algorithm
            -  Save that number as the next X0
                - next time that program is run it should know somehow that X0 == the previous value
            - evvery time enter is pressed new value should be given enstead of ending the program
    '''




