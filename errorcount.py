#This scripts counts the no f error codes and print.
def findErrorMsg(logfile):
    count = 0
    with open(logfile,'r') as f:
        for line in f:
            if "ERROR" in line:
                # print(line.strip())
                count+=1
    print(f"Number of ERROR codes in the log file are {count}")
    
findErrorMsg("error_log.txt")