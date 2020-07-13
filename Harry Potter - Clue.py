import random as r
from os import system

import time

print(f'\n\n\t\tThe Harry Potter Who-Dunnit Game ')
time.sleep(2)
print(f'\n\n\t\tWho did the killing? Where? And with what?')
time.sleep(2)
print(f'\n\tYou are in a competition with 3 computer opponents. After each of')
print(f'\ttheir turns, you may use new knowledge to reduce your suspect, weapon,')
print(f'\tand crime scene lists.')
time.sleep(7)

who1 = ['Lord Voldemort','Snape','Harry','Ron','Hermione','Dumbledore','Draco','Crabbe','Goyle', 'Lucius']
what1 = ['Avada Kedavra spell','Sword of Goddrick Gryffindor','basalisk fang','rope','Sectumsempra spell','Norwegian Ridgeback Dragon']
where1 = ['Great Hall','Slytherin dorm','Gryffindor dorm','North Tower','kitchen','Chamber of Secrets','Room of Requirement']
victim1 = ['Aunt Petunia','Fluffy','Buckbeak','Scabbers','Dolores Umbridge','Dobby','Nagini']

# who1, what1, and where1 are for the user.  His incorrect answers 
# disappear from his lists with pop().
#
# who2, what2, and where2 are for the computer players.
# Items are not popped off for them. Their guesses are random solely
# random.

who2 = who1[:]
what2 = what1[:]
where2 = where1[:]

who3 = who1[:]
what3 = what1[:]
where3 = where1[:]

who4 = who1[:]
what4 = what1[:]
where4 = where1[:]

	# Now for our random choice of Who, Where, and with What
thewho = r.choice(who1)
thewhat = r.choice(what1)
thewhere = r.choice(where1)
thevictim = r.choice(victim1)

# The com_player_choice function selects random choices for the 
# computer players.

def com_player_who(player):
	"""Generates a random suspect choice for each computer player"""
	if player == 'com2':
		person = r.choice(who2)
	elif player == 'com3':
		person = r.choice(who3)
	else:
		person = r.choice(who4)
	return (person)


def com_player_what(player):
	"""Generates a random weaponn choice for each computer player"""
	if player == 'com2':
		weapon = r.choice(what2)
	elif player == 'com3':
		weapon = r.choice(what3)
	else:
		weapon = r.choice(what4)
	return (weapon)


def com_player_where(player):
	"""Generates a random crime scene for each computer player"""
	if player == 'com2':
		place = r.choice(where2)
	elif player == 'com3':
		place = r.choice(where3)
	else:
		place = r.choice(where4)
	return (place)


def list_reduction(person, weapon, place, difficulty):
	"""Allows the user to narrow their suspect, weapon, and/or crime
	scene lists"""
	print('\n')
	print('SUSPECT LIST')
	for person in who1:
		print(f'{who1.index(person)} - {person}')
		
	print(f'\nWho would you like to remove from your suspect list?')
	suspect = input(f'Press ENTER for none: ')
	if suspect != '':
		suspect = int(suspect)
		print(f'\n{who1[suspect].title()} has been removed from the list.')
		who1.pop(suspect)
	
	print('\n')
	print('WEAPON LIST')
	for weapon in what1:
		print (f'{what1.index(weapon)} - {weapon}')
		
	print(f'\nWhat weapon would you like to remove from the list?')
	weapon = input(f'Press ENTER for none: ')
	if weapon != '':
		weapon = int(weapon)
		print(f'\n{what1[weapon].title()} has been removed from the list.')
		what1.pop(weapon)
		
	
	print('\n')
	print(f'CRIME SCENE LIST')
	for place in where1:
		print(f'{where1.index(place)} - {place}')
		
	print(f'\nWhat location would you like to remove from the list?')
	place = input(f'Press ENTER for none: ')
	if place != '':
		place = int(place)
		print(f'\n{where1[place].title()} has been removed from the list.')
		where1.pop(place)
	# Now we reduce lists for the computer players if the difficulty
	# level is Medium or Difficult.
	
	if cards_shown == 3:
		
		if difficulty == '3':
			if person in who2:
				x = who2.index(person)
				who2.pop(x)
			if weapon in what2:
				x = what2.index(weapon)
				what2.pop(x)
			if place in where2:
				x = where2.index(place)
				where2.pop(x)
			if person in who3:
				x = who3.index(person)
				who3.pop(x)
			if weapon in what3:
				x = what3.index(weapon)
				what3.pop(x)
			if place in where2:
				x = where2.index(place)
				where2.pop(x)		
			if person in who4:
				x = who4.index(person)
				who4.pop(x)
			if weapon in what4:
				x = what4.index(weapon)
				what4.pop(x)
			if place in where4:
				x = where4.index(place)
				where4.pop(x)
		if difficulty == '2':
			y = r.choice(range(1,3))
			if y == 1:
				if person in who2:
					x = who2.index(person)
					who2.pop(x)		
				if person in who3:
					x = who3.index(person)
					who3.pop(x)
				if person in who4:
					x = who4.index(person)
					who4.pop(x)
			elif y == 2:
				if weapon in what2:
					x = what2.index(weapon)
					what2.pop(x)			
				if weapon in what3:
					x = what3.index(weapon)
					what3.pop(x)			
				if weapon in what4:
					x = what4.index(weapon)
					what4.pop(x)
			else:
				if place in where2:
					x = where2.index(place)
					where2.pop(x)
				if place in where2:
					x = where2.index(place)
					where2.pop(x)
				if place in where4:
					x = where4.index(place)
					where4.pop(x)
						

#		
# We begin the game here.
#

print("""
		Please select your difficulty level:
		[1] Easy
		[2] Medium
		[3] Difficult
		""")
difficulty = input('Enter here: ')
print('\n\n\tThank you.\n\n')
time.sleep(1)
if difficulty == '1':
	print('\n\tThe difficulty level is Easy.')
elif difficulty == '2':
	print('\n\tThe difficulty level is Medium.')
else:
	print('The difficulty level is Difficult.')
time.sleep(3)

system('cls')

while True:
	# Player One's turn.  This is the user.
	#  Print the list of suspects.
	print(f'\n\n')
	print(f'SUSPECT LIST')
	for person in who1: 
		print(f'{who1.index(person)} - {person}')
	
	print('\n')

	cards_shown = 3  # This is the number of cards shown for incorrect guesses
	print(f'\n\nPLAYER ONE, please make a guess as to who')
	my_who_guess = input(f'killed {thevictim}. Enter the number beside the suspect: ')
	my_who_guess = int(my_who_guess)
	if who1[my_who_guess] != thewho:
		print(f'\nYou discover that {who1[my_who_guess]} is not the murderer.\n')
		who1.pop(my_who_guess)
	else:
		print(f'\nThere is no evidence that {who1[my_who_guess]} is not the murderer!') 

	#  Print the list of weapons.
	print(f'\n\n')
	print(f'WEAPON LIST')
	for weapon in what1:
		print(f'{what1.index(weapon)} - {weapon}')

	print('\n')
	my_what_guess = input('\tWhat was used? Enter the number beside the weapon: ')
	my_what_guess = int(my_what_guess)
	if what1[my_what_guess] != thewhat:
		print(f'\nYou discover that {what1[my_what_guess]} did not kill {thevictim}.\n')
		what1.pop(my_what_guess)
	else:
		print(f'\nThere is no evidence showing {what1[my_what_guess]} is not the murder weapon!')

	#  Print the list of possible crime scenes.
	print(f'\n\n')
	print(f'CRIME SCENE LIST')
	for place in where1:
		print(f'{where1.index(place)} - {place}')

	print('\n') 
	my_where_guess = input(f'\tAnd where was {thevictim} murdered? ')  
	my_where_guess = int(my_where_guess)
	if where1[my_where_guess] != thewhere:
		print(f'\nYou discover that {where1[my_where_guess]} is not the crime scene.\n')
	else:
		print(f'\nNo one disproves that {where1[my_where_guess]} is the scene of the crime!')

	#  THE ACCUSATION SECTION

	accusation = input(f'\nWould you like to solve the murder? (y/n) ')
	if accusation == 'y':
		print('\n\nTHE SUSPECTS')
		for person in who2: 
			print(f'{who2.index(person)} - {person}')
		my_who_guess = input('\n\tOkay, who done it? ')
		
		print('\n\nTHE WEAPONS')
		for thing in what2:
			print(f'{what2.index(thing)} - {thing}')
		my_what_guess = input ('\n\tWith what? ')
		
		print('\n\nTHE CRIME SCENE')
		for place in where2:
			print(f'{where2.index(place)} - {place}')
		my_where_guess = input ('\n\tAnd where? ')
		
		my_who_guess = int(my_who_guess)
		my_what_guess = int(my_what_guess)
		my_where_guess = int(my_where_guess)
		
		if who2[my_who_guess] == thewho: 
			if what2[my_what_guess] == thewhat: 
				if where2[my_where_guess] == thewhere:
					print(f'\n\n\n\tYou solved the mystery! You win!!!')
					break
		else:
			print(f'\n\n\n\tYour accusation is false!  You lose the game!')
			break
			
		# PLAYER TWO'S TURN
	
	player = 'com2'	
	person = com_player_who(player)
	weapon = com_player_what(player)
	place = com_player_where(player)
	
	cards_shown = 0
	if person != thewho:
		cards_shown += 1
	if weapon != thewhat:
		cards_shown += 1
	if place != thewhere:
		cards_shown += 1
		
	print(f'\n\nPLAYER TWO is guessing that {person.upper()} killed {thevictim}')
	print(f'with the {weapon.upper()} in the {place.upper()}.\n')
	print(f'\nPLAYER TWO learns has {cards_shown} incorrect guesses.')
	
	if cards_shown == 0:
		print(f'\nPLAYER TWO accuses {person} of killing {thevictim}')
		print(f'with the {weapon} in the {place}.  PLAYER TWO wins the game!')
		break
		
	# All players can narrow their lists.
	list_reduction(person, weapon, place, difficulty)  
	
		# PLAYER THREE'S TURN
	
	player = 'com3'	
	person = com_player_who(player)
	weapon = com_player_what(player)
	place = com_player_where(player)		
	
	cards_shown = 0
	if person != thewho:
		cards_shown += 1
	if weapon != thewhat:
		cards_shown += 1
	if place != thewhere:
		cards_shown += 1
		
	print(f'\n\nPLAYER THREE is guessing that {person.upper()} killed {thevictim}')
	print(f'with the {weapon.upper()} in the {place.upper()}.\n')
	print(f'PLAYER THREE learns that {cards_shown} are incorrect.')
	
	if cards_shown == 0:
		print(f'\nPLAYER THREE accuses {person} of killing {thevictim}')
		print(f'with the {weapon} in the {place}.  PLAYER THREE wins the game!')
		break
	
	list_reduction(person, weapon, place, difficulty)  
	
		# PLAYER FOUR'S TURN
		
	player = 'com4'	
	person = com_player_who(player)
	weapon = com_player_what(player)
	place = com_player_where(player)		
	
	cards_shown = 0
	if person != thewho:
		cards_shown += 1
	if weapon != thewhat:
		cards_shown += 1
	if place != thewhere:
		cards_shown += 1
		
	print(f'\n\nPLAYER FOUR is guessing that {person.upper()} killed {thevictim}')
	print(f'with the {weapon.upper()} in the {place.upper()}.\n')
	print(f'PLAYER FOUR learns that {cards_shown} are incorrect.')
	
	if cards_shown == 0:
		print(f'\nPLAYER FOUR accuses {person} of killing {thevictim}')
		print(f'with the {weapon} in the {place}.  PLAYER FOUR wins the game!')
		break
	
	list_reduction(person, weapon, place, difficulty)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
