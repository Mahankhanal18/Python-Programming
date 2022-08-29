import sys
user1 = input("Enter first person's name ")
user2 = input("Enter second person's name ")
print('...........Choose rock/paper/scissor.........')
user1_choice = input('%s, what is your choice ' % user1)
user2_choice = input("%s, what about your's " % user2)


def compare(u1, u2):
    if u1 == u2:
        return 'It is a tie '
    elif u1 == 'paper':
        if u2 == 'rock':
            return 'Paper Wins '
        else:
            return 'Scissor Wins '
    elif u1 == 'scissor': 

        if u2 == 'paper':
            return 'Scissor Wins '
        else:
            return 'Rock Wins '
    elif u1 == 'rock':
        if u2 == 'scissor':
            return 'Rock Wins '
        else:
            return 'Paper Wins '
    else:
        return 'Please input the valid information  '
    sys.exit()


print(compare(user1_choice, user2_choice))

print('Thanks for playing the game')
