import datetime

user_input=input("enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")
# creating variables #
goal = input_list[0]
deadline = input_list[1]

# converting python predefine string for all element to date format.converting string into datetime#
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
# calculate how many days from now till deadline #
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
# print(deadline_date - today_date) #
# print(type(datetime.datetime.strptime(daedline, "%d.%m.%Y")))#
print(f"Dear User ! Time remaining for your goal: {goal} is {time_till.days}.days")