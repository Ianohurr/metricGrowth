import random
import time
import csv
"""
Create fake values for db files. I didn't have access to more than 3 db files when I started writing this
so i decided to make my own. This function will go through each machine in the db. It will give the machine
a 1/2 change of gaining megabytes or 1/2 chance to lose some. After that it will gain/lose between 1-5 percent
which will be chosen randomly.
"""
def changeValues(list):
    for x in range(len(list)):
        percentChange=2
        gain=1
        if(len(list[x])>1):
            currentValue=list[x][1].replace(')','').strip()
        if(gain==1):
            currentValue=float(currentValue)+(float(currentValue)*float(".0"+str(percentChange)))
            currentValue=round(currentValue,2)
        else:
            currentValue=float(currentValue)-(float(currentValue)*float(".0"+str(percentChange)))
            currentValue=round(currentValue,2)
        if(len(list[x])>1):
            list[x][1]=") "+str(currentValue)


"""
This function will create a certain amount of csv files as i need to analyze x amount of days from the db
"""
def createTimeFrame(days):
    with open ("dbsizes07262017.csv") as f:
        fields=[]
        for line in f:
            line=line.split(',')
            fields.append(line)



    #x=x.replace(')','').strip()
    for x in range(days):
        changeValues(fields)
        date=time.strftime("%m%d%Y")
        fileName=("dbsizes"+str(x)+".csv")
        with open(fileName, 'w+',newline='') as csvfile:
            db=csv.writer(csvfile,delimiter=',')
            for line in fields:
                db.writerow(line)

def createCurrentDay():
    with open ("dbsizes07262017.csv") as f:
        fields=[]
        for line in f:
            line=line.split(',')
            fields.append(line)



    #x=x.replace(')','').strip()
        changeValues(fields)
        date=time.strftime("%m%d%Y")
        fileName=("dbsizes"+date+".csv")
        with open(fileName, 'w+',newline='') as csvfile:
            db=csv.writer(csvfile,delimiter=',')
            for line in fields:
                db.writerow(line)


def main():
    createCurrentDay()

if __name__ == '__main__':
    main()
