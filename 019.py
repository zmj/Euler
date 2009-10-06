def daysInMonth(month, year):
	if month==0: #jan
		return 31
	elif month==1: #feb
		if year%400==0 or (year%100!=0 and year%4==0):
			return 29
		else:
			return 28
	elif month==2: #march
		return 31
	elif month==3: #april
		return 30
	elif month==4: #may
		return 31
	elif month==5: #june
		return 30
	elif month==6: #july
		return 31
	elif month==7: #august
		return 31
	elif month==8: #sept
		return 30
	elif month==9: #oct
		return 31
	elif month==10: #nov
		return 30
	elif month==11: #dec
		return 31
	else:
		print "error: month"+str(month)+" year"+str(year)

day = 1
numFirstSundays = 0

for year in range(1900, 2001):
	for month in range(0, 12):
		if day == 0 and year>1900 and year<2001:
			numFirstSundays += 1
		day = (day + daysInMonth(month, year)) % 7

print numFirstSundays
