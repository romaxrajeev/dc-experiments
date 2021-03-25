#Lamport clock for two processes

#Inputs
e1,e2 = map(int,input("Enter the number of events in process1 and process2: ").split())

print("If e1 happens before e2, keep value as 1.\nIf e1 happens after e2, keep value as -1.\nElse, keep value as 0.")
print("Enter the dependency matrix:")

dependency = [list(map(int,input().split(" "))) for _ in range(e1)]

#Initializing clocks to 1
event1 = [1]*e1
event2 = [1]*e2

#Cycle throught the list
for x in range(e1):
    for y in range(e2):
        if dependency[x][y] == 1:
           #Check which is maximum and update
            event2[y] = max(event1[x]+1,event2[y])
        if dependency[x][y] == -1:
            #Check which is maximum and update
            event1[x] = max(event2[y]+1,event1[x])
        else:
            #In case of any updations, just increment the next value by 1
            for k in range(y,e2-1):
                event2[k+1] = event2[k] + 1
            for k in range(x,e1-1):
                event1[k+1] = event1[k] + 1

#Print output
print("Process 1:",event1,"\nProcess 2:",event2)