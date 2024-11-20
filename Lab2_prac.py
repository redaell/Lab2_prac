print ("ET7035 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    inputstr = input()
    print ("original input = ", inputstr)

    inputsplit = inputstr.split(",") #split it using comma
    print ("after splitting = ", inputsplit)

    floatlist = []
    for x in inputsplit: # go through each number in the original list
        floatnum = float(x) # float each of the numbers
        floatlist.append(floatnum) # add each flaoted number into the list 
    return floatlist

def calc_average(inputlist):
    print("calc_average")
    total = sum(inputlist)
    average = total/len(inputlist)
    print ("average = ",average)
    return average

def find_median(sortedlist):
    print("calc_median_temperature")
    sortedlist.sort()
    cnt = len(sortedlist)

    if cnt % 2 == 1:
        median = sortedlist[(cnt-1)//2]

    else:
        median = (sortedlist[cnt//2] + sortedlist[cnt//2]-1)//2
    print("Median = ", median)  
    return median


def calc_min_max_temperature(inputlist):
    print("find min max")
    inputlist.sort()
    resultlist = [inputlist[0], inputlist[-1]] #return the results of the first and last 
    print ("min and max list = ", resultlist)
    return resultlist

def main():
    display_main_menu()
    floatlist = get_user_input() # to capture and store the output of get user input to floatlist
    calc_average(floatlist)
    calc_min_max_temperature(floatlist)
    find_median(floatlist)

if __name__ == "__main__":
    main()



