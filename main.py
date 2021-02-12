import random
def isGreater(user, comp):
  
  user_won = 'User Won!'

  if user == comp: return 'It\'s a Tie!'

  if user == 0 and comp == 2:
    return user_won
  elif user == 1 and comp == 0:
    return user_won
  elif user == 2 and comp == 1:
    return user_won
  else: return 'Computer Won!'


list = [0,1,2]
map= {0: 'Rock', 1:'Paper', 2:'Scissors'}
comp = random.choice(list)
comp_choice = map[comp]

choices = \
  '''
  0: Rock
  1: Paper
  2: Scissors
  '''
while(True):
  print(choices)
  user = input('Enter user choice: ')

  try:
    if int(user) not in list:
      print('\nEnter valid choice')
    else: 
      break
  except Exception:
    print('\nEnter valid choice')
    pass

print(f'User choice: {map[int(user)]}')
print(f'Computer choice: {comp_choice}')


print(isGreater(int(user), comp))

