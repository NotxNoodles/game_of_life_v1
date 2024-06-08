import os
import time

arr_1 = [[0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,1,1,1,0,0,0,0],
         [0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         ]
arr_2 = [[0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         ]

#Checks the neighbours and updates the original array with the updated values 
def updateArray(arr, arr2):
    neighbors = 0
    #check the condition to either kill, keep, generate
        #if 1 or 0 neighbor: KILL (underpopulation)
        #if >=4 neighbor: KILL (overpopulation)
        #if 2 or 3 neighbors: KEEP
        #if on cell border: KILL
        #if cell == 0 and neighbors == 3: GENERATE
    
    #Counting the neighbours
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            neighbors = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            #Adding and deleting cells in the second array
            if  arr[i][j] == 0:
                if neighbors == 3:
                    arr2[i][j] = 1
            else:
                if neighbors <= 1 or neighbors >= 4:
                    arr2[i][j] = 0
                else:
                    arr2[i][j] = 1
            neighbors = 0
    
    #Copying everything from array 2 to array 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = arr2[i][j]



    
    #Clearing the end rows
    for i in range(len(arr[0])):
        arr[0][i] = 0
        arr[len(arr)-1][i] = 0


    #Clearing the end columns
    for i in range(len(arr)):
        arr[i][0] = 0
        arr[i][len(arr[0])-1] = 0

    
    #Resetting array 2
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr2[i][j] = 0

#Printing out the new array

for j in range(30):
    updateArray(arr_1,arr_2)
    for i in range(len(arr_1)):
        print(arr_1[i],"\n")
    time.sleep(.5)
    print('\x1Bc')
    