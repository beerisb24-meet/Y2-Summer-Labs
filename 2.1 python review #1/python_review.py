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
tempOrder=[highest_temp,lowest_temp]
lastHighTemp=highest_temp
lowestHighTemp=26
for temp in range(len(temperatures)):
	if temperatures[temp]>=highest_temp:
		if lastHighTemp<highest_temp:
			lowestHighTemp=lastHighTemp
		lastHighTemp=highest_temp
		highest_temp=temperatures[temp]
		tempOrder.insert(tempOrder.index(lastHighTemp)+1,highest_temp)
		highest_temp_day=days_of_the_week[temp]
	elif temperatures[temp]<=lowest_temp:
		lastLowTemp=lowest_temp
		lowest_temp=temperatures[temp]
		lowest_temp_day=days_of_the_week[temp]
		tempOrder.insert(tempOrder.index(lastLowTemp)-1,lowest_temp)
	elif lowest_temp<temperatures[temp]<highest_temp:
		tempOrder.insert(tempOrder.index(lowestHighTemp)-1,temperatures[temp])
tempOrder.remove(26)
tempOrder.remove(41)



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
print("good days for Shelly are: "+str(good_days))
print(str(highest_temp)+", the highest temperature, was on "+highest_temp_day)
print(str(lowest_temp)+", the lowest temperature, was on "+lowest_temp_day)
print("The avg temp is: "+str(average_temp))
print("days with above avg temps are: "+str(above_avg_days))
print("The order of the temps(lowest to highest) is: "+str(tempOrder))
#I know that this bonus doesn't work completely, but I couldn't figure out how to solve it.