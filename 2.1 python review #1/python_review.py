import random
temperatures= []
for i in range(7):
	temperatures.append(random.randint(26,41))
days_of_the_week=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
good_days_count=0
good_days=[]
for temp in range(len(temperatures)):
	if temperatures[temp]%2 == 0:
 		good_days_count+=1
 		good_days.append(days_of_the_week[temp])
 		print(days_of_the_week[temp]+" has even temperatures")

highest_temp=26
lowest_temp=41
print(lowest_temp)
for temp in range(len(temperatures)):
	if temperatures[temp]>highest_temp:
		highest_temp=temperatures[temp]
		highest_temp_day=days_of_the_week[temp]
	if temperatures[temp]<lowest_temp:
		lowest_temp=temperatures[temp]
		lowest_temp_day=days_of_the_week[temp]



average_temp=0
for temp in temperatures:
	average_temp+=temp
average_temp=average_temp/7
above_avg=[]
above_avg_days=[]
for temp in range(len(temperatures)):
	if temperatures[temp]>average_temp:
		above_avg.append(temperatures[temp])
		above_avg_days.append(days_of_the_week[temp])



print("the temps for the week are: "+str(temperatures))
print("good days for Shelly are: "+good_days)
print(str(highest_temp)+", the highest temperature, was on "+highest_temp_day)
print(str(lowest_temp)+", the lowest temperature, was on "+lowest_temp_day)
print("The avg temp is: "+str(average_temp))
print("days with above avg temps are: "+above_avg_days)