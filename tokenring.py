import random
import time

#Token Ring Algorithm

#Ask user how many processes are there
processes = int(input("Enter the number of processes: "))

#Maintain queues of CS processes
ring = [0] * processes
completed = []

#Give token to process 0
token = 0

#Get a random process to do CS, which is not completed
ring[random.choice([x for x in range(processes)])] = 1

#Printing initial status
print("\nToken with", token)
print("Process",ring.index(1),"wants to enter CS")

#Loop around
while len(completed) < processes:

    #Check if the process with token wants to enter CS
    if ring[token] == 1:
        print("\nProcess",token,"has token and wants to enter Critical Section.\nExecuting...")
        
        #Wait for 3 seconds to show execution
        time.sleep(3.00)
        
        #Pass token to next process
        print("Process",token,"has completed execution and token passed to",(token + 1) % processes)

        #Add completed process to completed
        ring[token] = 0
        completed.append(token)

        #Check if any process is remaining or not
        rem = [x for x in range(processes) if x not in completed]
        if len(rem) > 0:
            #Choose a random process which is not completed for CS
            ring[random.choice(rem)] = 1
    else:

        #Pass token
        print("\nProcess",token,"has the token but doesn't want to execute in Critical Section.\nHence passing over to next",(token + 1) % processes)

    #Print the current status
    print("Token with", token)
    if len(completed) < processes:
        print("Process",ring.index(1),"wants to enter CS")
    print("Completed processes:",completed)

    #Actually passing token here, since this line is common in both if and else, hence written here
    token = (token + 1) % processes

#Print the completed sequence
print("All processes are completed.")
print("Sequence:",completed)