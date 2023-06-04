



def dark_hall_intro():
    directions = ['right','left','forward']
    print("You're left in a dark hall, you're to choose to go down into any of the three hallways, which way would you like to go? ")
    userInput = ''

    while userInput not in directions:
        userInput = input('Choose options (right or left or forward): ')
        if userInput == 'left':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            
            showHumanFigure()
        elif userInput == 'right':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            
            showSkeletonWall()
        elif userInput == 'forward':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            
            ghostRoom()
        else:
            print('You have not choosen any option')
    




def showHumanFigure():
    directions = ['right', 'left', 'backward']
    print("You see a dark shadowy figure appear in the distance. You are freaking out. Where would you like to go?")
    userInput = ' '

    while userInput not in directions:
        userInput = input('Choose a direction (right or left or backward): ')
        if userInput == 'right':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('You see blood trail on the floor, you follow the direction and you make it to the exit!, You win!')
        elif userInput == 'left':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('You have fallen into an endless valley, You lose!!!')
        elif userInput == 'backward':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            dark_hall_intro()
        else:
            print("You've not choose a valid direction, please choose options")

def showSkeletonWall():
    directions = ['left','forward', 'backward']
    print('You found yourselt into a room full of skeleton walls, you are so scared, where would you go?')
    userInput = ''

    while userInput not in directions:
        userInput = input('choose a direction( left or forward or backward) ')
        if userInput == 'left':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            action = ['hammer', 'no_hammer']
          
            userInput = ''
            while userInput not in action:
                print('choose hammar or no_hammer')
                userInput = input('You must take the hammer and go back to fight the strange creature or you die! ')
                
                if userInput == 'hammer':
                    print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
                    print('go back and fight the strange creatures')
                    userInput = input('choose forward or backward ')

                    break;
                else:
                    print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
                    print('The strange creature has killed you, You lose!')
                quit()
                
        elif userInput == 'forward':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            strangeCreature()
            
        elif userInput == 'backward':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            dark_hall_intro()
        else:
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('Please choose a valid direction')

def strangeCreature():
    actions = ['fight','flee']
    print('A strange creature has appeared. You can either run or fight it. What would you like to do?')
    userInput = ''

    while userInput not in actions:
        userInput = input('You can either chose to fight or flee ')
        weapon = True
        if userInput == 'fight':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            if weapon:
                print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
                print('You have killed the strange creature, You win!')
            else: 
                print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
                print('The strange creature has killed you, You lose!!!')
        else:
            showSkeletonWall()


def ghostRoom():
    directions = ['right', 'left','backward']
    print('You hear strange voices. You think you have awoken some of the ghosts. Where would you like to go?")')
    userInput = ''

    while userInput not in directions:
        userInput = input('Please select a direction( left or right or backward)')
        if userInput == 'right':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('Multiple ghosts emerging from the hallways, you are kiled!!!')

        elif userInput == 'left':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('You have found an exit, You won!!!')
        elif userInput == 'backward':
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            dark_hall_intro()
        else:
            print(f'You have choosen {userInput.upper()}, Goodluck with your adventure')
            print('Please select a valid direction')

        
dark_hall_intro()       









