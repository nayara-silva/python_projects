print('Welcome to the tip calculator.')
bill_total = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people_no = int(input('How many people to split the bill? '))

total_per_person = round(bill_total * (1 + tip_percentage / 100) / people_no, 2)

#print(f'Each person should pay: ${total_per_person}')
print('Each person shoul pay: ${:.2f}'.format(total_per_person))
