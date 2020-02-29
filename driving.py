country = input('輸入你的國家：')
age = input('請輸入年齡：')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以在台灣考駕照')
	else:
		print('你還不能在台灣考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以在美國考駕照')
	else:
		print('你還不能在美國考駕照')
else:
	print('你只能輸入台灣和美國兩個國家喔')