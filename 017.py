def wordify(n):
	if n==0:
		return ""
	elif n==1:
		return "one"
	elif n==2:
		return "two"
	elif n==3:
		return "three"
	elif n==4:
		return "four"
	elif n==5:
		return "five"
	elif n==6:
		return "six"
	elif n==7:
		return "seven"
	elif n==8:
		return "eight"
	elif n==9:
		return "nine"
	elif n==10:
		return "ten"
	elif n==11:
		return "eleven"
	elif n==12:
		return "twelve"
	elif n==13:
		return "thirteen"
	elif n==14:
		return "fourteen"
	elif n==15:
		return "fifteen"
	elif n==16:
		return "sixteen"
	elif n==17:
		return "seventeen"
	elif n==18:
		return "eighteen"
	elif n==19:
		return "nineteen"
	elif n==20:
		return "twenty"
	elif n>20 and n<30:
		return "twenty-"+wordify(n%10)
	elif n==30:
		return "thirty"
	elif n>30 and n<40:
		return "thirty-"+wordify(n%10)
	elif n==40:
		return "forty"
	elif n>40 and n<50:
		return "forty-"+wordify(n%10)
	elif n==50:
		return "fifty"
	elif n>50 and n<60:
		return "fifty-"+wordify(n%10)
	elif n==60:
		return "sixty"
	elif n>60 and n<70:
		return "sixty-"+wordify(n%10)
	elif n==70:
		return "seventy"
	elif n>70 and n<80:
		return "seventy-"+wordify(n%10)
	elif n==80:
		return "eighty"
	elif n>80 and n<90:
		return "eighty-"+wordify(n%10)
	elif n==90:
		return "ninety"
	elif n>90 and n<100:
		return "ninety-"+wordify(n%10)
	elif n>=100 and n<1000:
		hundreds = n / 100
		remainder = n - hundreds*100
		if remainder>0:
			return wordify(hundreds)+" hundred and "+wordify(remainder)
		else:
			return wordify(hundreds)+" hundred"
	elif n>=1000 and n<1000000:
		thousands = n / 1000
		remainder = n - thousands*1000
		if remainder>0:
			return wordify(thousands)+" thousand, "+wordify(remainder)
		else:
			return wordify(thousands)+" thousand"
	else:
		return ""

max = 1000 
sum = 0
for i in range(1,max+1):
	words = wordify(i)
	words2 = words.replace("-","").replace(" ","").replace(",","")
	sum += len(words2)

print sum
