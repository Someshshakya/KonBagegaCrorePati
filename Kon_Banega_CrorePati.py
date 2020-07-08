
print("\t\t\t<<<<<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>>>>>>>>")
print()
print("\t\t\tWecome To KBC (Kon Banega Crorepati)")
print()
print("\t\t\t<<<<<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>>>>>>>")
count=0
question_list=[
			"1. Who was the first President of India?",
			"2. Where is Red fort situated?",
			"3. How many continents are there in the world?",
			"4. Who was the father of nation?",
			]
option_list=[["Jawahar Lal Nehru","Dr.Rajendra Prashad","Mahatma Gandhi","Lal Bhadur Shastri"],
			["Delhi","Agara","Mumbai","Kolkata"],
			["Five","Nine","Seven","Eight"],
			["Moti Lal","Jawahar Lal Nehru"," Bal Ganga Dhar","Mahatma Gandhi"]
			]
life_line=[
		["1. Jawahar Lal Nehru","2. Dr. Rajendra Prashad"],["1. Dehi","2. Agra"],["1. Seven","2. Six"],["1. Moti Lal","2, Mahatama Gandhi"]
		]
answer_list=[2,1,3,4]

solution=[2,1,1,2]
count=0
for i in range(len(question_list)):
	print()
	print(question_list[i])
	print("--------------------------------------------")
	print()
	n=1
	for j in range(len(option_list)):
		print(n,".",option_list[i][j])
		n+=1
	print("Do you want 50 50 life line")
	print("______________________________")
	print()
	a=int(input("\tChoose Your Answer 1. 2. 3. 4.  and  If you want 50 50 Life Line Enter 50 >>>>>>>>>    "))
	if a == 50 and count==1:
		print("You can take 50 50 Life Line only once")
		print("_______________________________________")
		break
	elif a==50:
		for d in range(0,2):
			print(life_line[i][d])
		print()
		print()
		s=int(input("\tChoose Your Answer 1. 2. >>>>>>>>>    "))
		if s==solution[i]:
			print("<<=>>======================<<=>>================<<=>>")
			print("Congratulation ! you have moved to next question !")
			count+=1
		else:
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("      Good Try !!!\n          Better Luck next Time\nNote: You have Entered Wrong Answer\n                                                 made by : Somesh Shakya")
			print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			break
	else:
		if a==answer_list[i]:
			print("<======>>=<<======>")
			print("Congratulation ! ")
			print("<======>>=<<======>")
			continue
		else:
			count+=1
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			print("      Good Try !!!\n          Better Luck next Time\nNote: You have Entered Wrong Answer\n                                                 made by : Somesh Sakya")
			print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			break
		if count==1:
			break



