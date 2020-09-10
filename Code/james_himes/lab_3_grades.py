score = input('What is your score?')

score = int(f'{score}')

if score>=97 and score<=100:
    print('Your Grade is A+')
elif score>=96 and score<=93:
	print('Your Grade is A')
elif score>=92 and score<=90:
	print('Your Grade is A-')
elif score>=87 and score<=89:
	print('Your Grade is B+')
elif score>=86 and score<=83:
    print('Your Grade is B')
elif score>=82 and score<=80:
    print('Your Grade is B-')
elif score>=77 and score<=79:
    print('Your Grade is C+')
elif score>=73 and score<=76:
    print('Your Grade is C')
elif score>=72 and score<=70:
    print('Your Grade is C-')
elif score>=67 and score<=69:
    print('Your Grade is D+')
elif score>=63 and score<=65:
    print('Your Grade is D')
elif score>=60 and score<=62:
    print('Your Grade is D-')
elif score>=57 and score<=59:
    print('Your Grade is F+')
elif score>=53 and score<=55:
    print('Your Grade is F')
elif score<=52:
	print('your Grade is F-')
else:
    print('Not a grade!')
