import random

processes = [x for x in range(int(input(("Enter the number of processes:"))))]

coordinator = processes[-1]

#Crash the coordinator
crashed = coordinator

#Choose another random process to start the election
coordinator = random.choice(processes[:processes.index(crashed)] + processes[processes.index(crashed)+1:])

print("Current Co-ordinator",crashed,"has crashed.")
print()
print("Choosing a random process to start the election.\n")
sendMes = processes[:processes.index(crashed)] + processes[processes.index(crashed)+1:]

while sendMes != []:

    print("Process",coordinator,'has announced election.')
    #Send to all the processes bigger than current coordinator, if none, stay as the coordinator
    sendMes = processes[processes.index(coordinator)+1:]
    if crashed in sendMes:
        sendMes.pop(sendMes.index(crashed))

    #Print status of the old coordinator
    print("Process",crashed,"has not yet replied.")
    if sendMes == []:
        print("No other process to send message, hence I'll be the co-ordinator.")
    else:
        print("Sending messages to",sendMes)

    #Respond OK for election
    for process in sendMes:
        if process != crashed:
            print("Process",process,"has responded OK for election.")

    #Pass over control to each of OK respondents to carry over the election
    if sendMes != []:
        print("Now",sendMes[0],"will be sending the election message.")
        coordinator = sendMes[0]
        print()