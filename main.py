import random
import math
import numpy as np
total_waiting_time_in_system = 0 # initial value for the total waiting time
total_waiting_time_in_queue = 0 #initial number of the customer who wait
customer_count = 1 #customer count to display customer number in the table
car_number = 0 #inital car number to follow car count in for loop
road = ""
first_road = 0
second_road = 0
third_road = 0

lambda1 = int(input("Please enter a value for the lambda1: "))
lambda2 = int(input("Please enter a value for the lambda2: "))
lambda3 = int(input("Please enter a value for the lambda3: "))
mu = int(input("Please enter a value for the mu: "))

debugger_input = input("Do you want to run in this code in debugger mode?\n") #asks user if s/he wants to start code in a debug mode
if debugger_input.casefold() == "yes": #if the answer is yes
    print("Perfect! You are in the debugger mode!\n" #display following guides to control debug mode
          "Please use:\n"
          "**************************************\n"
          "n - to execute next line of the code\n"
          "c - complete all code\n"
          "p - print\n"
          "s - step into a function\n"
          "**************************************\n")
    import pdb;

    pdb.set_trace() #if the answer is yes, code starts to run with the debug mode
elif debugger_input.casefold() == "no": #if the answer is no code just run without debug mode
    print("You are not running this code in debugger mode.")
else:
    print("You typed invalid input!")

for i in range(100000):
    car_number += 1 #increment car number by 1 for every step
    random_number_service = random.uniform(0, 1) #created a number between 0 and 1 and assign it to the random_number_service to calculate service time
    service_time = (-(1 / mu) * math.log((1 - random_number_service), math.e)) #as the service time is common among cars and we have 1 service time, we assign a service time first

    if car_number == 1: #checks if the car number is 1
        #interarrival_time = 0
        interarrival_time = 0  # initial interarrival time
        time_service_begins = 0 #if the car number is 1 we assume our service starts with the first reach of the car so time service begins at 0
        waiting_time_in_queue = 0 #if the car number is 1 we assume our service starts with the first reach of the car so waiting time in queue is 0
        arrival_time = 0 #if the car number is 1 we assume our service starts with the first reach of the car so arrival time is 0
        idle_time = 0 #if the car number is 1 we assume our service starts with the first reach of the car so idle time is also 0

        random_number1 = random.uniform(0, 1)  # generates random number betweem 0 and 1 to use in interarrival time 1
        random_number2 = random.uniform(0, 1)  # generates random number betweem 0 and 1 to use in interarrival time 2
        random_number3 = random.uniform(0, 1)  # generates random number betweem 0 and 1 to use in interarrival time 3


        time_customer_in_system = service_time + waiting_time_in_queue # calculates the time customer in system
        time_service_ends = service_time + time_service_begins # calculates the end time of the system
    else:
        random_number1 = random.uniform(0, 1) #generates random number betweem 0 and 1 to use in interarrival time 1
        random_number2 = random.uniform(0, 1) #generates random number betweem 0 and 1 to use in interarrival time 2
        random_number3 = random.uniform(0, 1) #generates random number betweem 0 and 1 to use in interarrival time 3


        if lambda1 == 0 and lambda2 == 0:
            interarrival_time3 = (-(1 / lambda3) * math.log((1 - random_number3), math.e))
            arrival_time3 = interarrival_time3 + arrival_time  # takes arrival time for the interarrival time 3
            min_arrival_time = arrival_time3
            arrival_time1 = 0
            arrival_time2 = 0
            #calculates exponential random variables for each interarrival time, using random_number and lambda
        elif lambda1 == 0 and lambda3 == 0:
            interarrival_time2 = (-(1 / lambda2) * math.log((1 - random_number2), math.e))
            arrival_time2 = interarrival_time2 + arrival_time  # takes arrival time for the interarrival time 3
            min_arrival_time = arrival_time2
            arrival_time1 = 0
            arrival_time3 = 0
        elif lambda2 == 0 and lambda3 == 0:
            interarrival_time1 = (-(1 / lambda1) * math.log((1 - random_number1), math.e))
            arrival_time1 = interarrival_time1 + arrival_time  # takes arrival time for the interarrival time 1
            min_arrival_time = arrival_time1
            arrival_time2 = 0
            arrival_time3 = 0
        elif lambda1 == 0:
            interarrival_time2 = (-(1 / lambda2) * math.log((1 - random_number2), math.e))
            interarrival_time3 = (-(1 / lambda3) * math.log((1 - random_number3), math.e))
            arrival_time2 = interarrival_time2 + arrival_time  # takes arrival time for the interarrival time 2
            arrival_time3 = interarrival_time3 + arrival_time  # takes arrival time for the interarrival time 3
            min_arrival_time = min(arrival_time2, arrival_time3)
            arrival_time1 = 0
        elif lambda2 == 0:
            interarrival_time1 = (-(1 / lambda1) * math.log((1 - random_number1), math.e))
            interarrival_time3 = (-(1 / lambda3) * math.log((1 - random_number3), math.e))
            arrival_time1 = interarrival_time1 + arrival_time  # takes arrival time for the interarrival time 1
            arrival_time3 = interarrival_time3 + arrival_time  # takes arrival time for the interarrival time 3
            min_arrival_time = min(arrival_time1, arrival_time3)
            arrival_time2 = 0
        elif lambda3 == 0:
            interarrival_time1 = (-(1 / lambda1) * math.log((1 - random_number1), math.e))
            interarrival_time2 = (-(1 / lambda2) * math.log((1 - random_number2), math.e))
            arrival_time1 = interarrival_time1 + arrival_time  # takes arrival time for the interarrival time 1
            arrival_time2 = interarrival_time2 + arrival_time  # takes arrival time for the interarrival time 2
            min_arrival_time = min(arrival_time1, arrival_time2)
            arrival_time3 = 0
        else:
            interarrival_time1 = (-(1 / lambda1) * math.log((1 - random_number1), math.e))
            interarrival_time2 = (-(1 / lambda2) * math.log((1 - random_number2), math.e))
            interarrival_time3 = (-(1 / lambda3) * math.log((1 - random_number3), math.e))
            arrival_time1 = interarrival_time1 + arrival_time #takes arrival time for the interarrival time 1
            arrival_time2 = interarrival_time2 + arrival_time #takes arrival time for the interarrival time 2
            arrival_time3 = interarrival_time3 + arrival_time #takes arrival time for the interarrival time 3
            min_arrival_time = min(arrival_time1, arrival_time2, arrival_time3) #compare 3 arrival time to decide which one is going to be the next one

        if min_arrival_time == arrival_time1: #checks if the minimum arrival
            interarrival_time = interarrival_time1 #if minimum arrival time equals to interarrival time 1, it equals the interarrival to interarrival1
            road = "road1"
            first_road += 1
        elif min_arrival_time == arrival_time2:
            interarrival_time = interarrival_time2 #if minimum arrival time equals to interarrival time 2, it equals the interarrival to interarrival2
            road = "road2"
            second_road += 1
        elif min_arrival_time == arrival_time3:
            interarrival_time = interarrival_time3 #if minimum arrival time equals to interarrival time 3, it equals the interarrival to interarrival3
            road = "road3"
            third_road += 1


        arrival_time = interarrival_time + arrival_time #arrival time calcuation with previous arrival time and interarrival time
        time_service_begins = max(time_service_ends, arrival_time) #calculates begin time by comparing and getting max of previous end time and arrival time
        waiting_time_in_queue = time_service_begins - arrival_time #calculates waiting time in queue with previous begin time and current arrival time
        time_customer_in_system = service_time + waiting_time_in_queue #calculates customer's system time with service time and waiting time in queue
        #idle_time = time_service_ends - time_service_begins
        if time_service_begins - time_service_ends < 0: #to calculate idle time it takes the difference between previous time service ends and time service begins and checks if the it is less than 0
            idle_time = 0 #if the difference is less than 0 it assign the idle time 0 because it means system was not idle at these time duration
        else:
            idle_time = time_service_begins - time_service_ends # if the difference is greater than or equal to 0 performs operation
        time_service_ends = service_time + time_service_begins #calculates time service ends by the current service time and time service begins

    total_waiting_time_in_system += time_customer_in_system #calculate the total waiting time in system
    total_waiting_time_in_queue += waiting_time_in_queue #calculates the total waiting queue time

    if debugger_input == "yes" and customer_count <= 10:#if the debugger mode is selected it creates a table for the user and displays only 10 of the iterations
        d = {customer_count: [interarrival_time, arrival_time, service_time, time_service_begins, waiting_time_in_queue, #it is a dictionary that has a key of customer count and array as a value of other parameters
                              time_service_ends, time_customer_in_system, idle_time, road],
             }
        if customer_count == 1: #if the customer count is 1 it creates the title of the columns for table, it prevents creating table for every customer count
            print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25}".format('Customer - ',
                                                                                          'Interarrival Time - ',
                                                                                          'Arrival Time - ',
                                                                                          'Service Time - ',
                                                                                          "Time Service Begins - ",
                                                                                          "Waiting Time In Queue - ",
                                                                                          "Time Service Ends - ",
                                                                                          "Time Customer In System - ",
                                                                                          "Idle Time", "Road"))
        #to reach the values of the dictionary it assigns parameters to v value and then print it in the following format
        for k, v in d.items():
            my_interarrival_time, my_arrival_time, my_service_time, my_time_service_begins, my_waiting_time_in_queue, my_time_service_ends, \
            my_time_customer_in_system, my_idle_time, my_road = v
            print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25} {:<30} {:<30}".format(k, my_interarrival_time,
                                                                                         my_arrival_time,
                                                                                         my_service_time,
                                                                                         my_time_service_begins,
                                                                                         my_waiting_time_in_queue,
                                                                                         my_time_service_ends,
                                                                                         my_time_customer_in_system,
                                                                                         my_idle_time,my_road))
        customer_count += 1 #increments customer count for output customer number
print("**************************")
average_waiting_time_in_system = total_waiting_time_in_system / car_number #it calculates the total average time
print("The average waiting time of the cars in the system: ", average_waiting_time_in_system)

wait_in_queue = total_waiting_time_in_queue / car_number
print("The average waiting time of the cars in the queue: ", wait_in_queue) #it calculates the total waiting queue time

if debugger_input.casefold() == "no": #gives information to the user to see table if s/he is not in the debugger mode
    print("Please run this code in debugger mode to see the results in the table.")

print("Road 1:", first_road/car_number)
print("Road 2:", second_road/car_number)
print("Road 3:", third_road/car_number)