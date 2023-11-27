import statistics

def display_main_menu():
    print("Enter some numbers separated by spaces (e.g. 5 67 32)")  # Changed commas to spaces for input format

def calc_average(numlist):
    total = 0.0
    for x in numlist:
        total += x
    average = total / len(numlist)
    return average

def calc_average_temperature(numlist):  # New function to calculate average temperature
    return statistics.mean(numlist)

def get_user_input():
    templist = input()
    splitlist = templist.split()  # Changed split delimiter to spaces
    floatlist = [float(x) for x in splitlist]
    return floatlist

def find_min_max(numlist):
    x = ["Minimum value = " + str(min(numlist)), "Maximum value = " + str(max(numlist))]
    return x

def calc_min_max_temperature(numlist):  # New function to calculate min and max temperature
    return [min(numlist), max(numlist)]

def sort_temperature(numlist):
    numlist.sort()
    return numlist

def calc_median_temperature(numlist):
    median = statistics.median(numlist)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    print("List of numbers: " + str(numlist))
    average = calc_average(numlist)
    print("Average value: " + str(average))
    minmax = find_min_max(numlist)
    print(minmax)
    tempsort = sort_temperature(numlist)
    print("Sorted values: " + str(tempsort))
    mediantemp = calc_median_temperature(numlist)
    print("Median Value: " + str(mediantemp))

if __name__ == "__main__":
    main()
