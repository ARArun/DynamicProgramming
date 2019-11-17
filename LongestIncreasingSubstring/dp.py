#! /usr/bin/python3

'''
Finding the longest increasing substring

'''

def lis(LVal):
    Lans = LVal.copy()
    #MINIMUM LONGEST SUBSTRING LENGTH IS ONE
    Lans = [(val*0 + 1) for val in Lans]

    
    for i in range(1, len(LVal)):
        for j in range(0, i):
            # IF THERE IS A VALUE LESS THAN THE I'TH IN PRECEEDING POSITION THEN INCREMENT IF NECESSARY
            if LVal[i] > LVal[j]:
                Lans[i] = max(Lans[i], Lans[j] + 1)
    return(max(Lans))

print(lis([10, 22, 9, 33, 21, 50, 41, 60]))