#Bankers Algorithm

#Some functions
def isFeasible(need,available):
    if sum(1 for x in [available[i] - need[i] for i in range(len(need))] if x < 0) == 0:
        return True
    return False

def addResource(allocation,available):
    return([available[i] + allocation[i] for i in range(len(available))])

#Input for number of process and resources
process, resources = map(int,input("Enter Process and Resources (space separated): ").split())

#Input for allocation matrix and available matrix
print("Enter allocation matrix:")
allocation = [list(map(int,input().split())) for _ in range(process)]
print("Enter maximum matrix:")
maximum = [list(map(int,input().split())) for _ in range(process)]
available = list(map(int,input("Enter available matrix (space separated): ").split()))

#Need matrix = Max - Available
need = [[maximum[i][j] - allocation[i][j] for j in range(resources)] for i in range(process)]

#Safe sequence
safe = []
completed = 0

#If need <= available, add to safe sequence and add allocated to available
current = 0

#Cycles to give some more time for processes to gather resources
cycle = 0
while completed < process and cycle < 5:
    if current == 0:
        cycle += 1
    if isFeasible(need[current],available) and current not in safe:
        print("Let's execute process",current)
        safe.append(current)
        available = addResource(allocation[current],available)
        completed += 1
    else:
        print("Current resources do not permit me to execute process",current)
    current = (current + 1) % process

if completed == process:
    print("Safe state. The safe sequence is:",safe)
else:
    print("Not safe sequence even after 5 cycles.")