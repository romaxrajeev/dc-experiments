import threading

def upper(s):
    print("Upper:",s.upper())

def lower(s):
    print("Lower:",s.lower())

def printStr(s):
    print("String:",s)

n = input("Enter a string: ")
t1 = threading.Thread(target=printStr, args=(n,))
t2 = threading.Thread(target=lower, args=(n,))
t3 = threading.Thread(target=upper, args=(n,))

#Starting all threads
t1.start()
t2.start()
t3.start()

#Wait till each thread executes
t1.join()
t2.join()
t3.join()

print("Done!")