from random import sample

i, j = 0, 0
def generate_randoms():
    return sample(range(0,10), 4)

def check_user_input(user_input):
    if (len(user_input) != 4) or (not user_input.isdigit()):  # Repeat until correct format is entered
        return 'Please enter exactly 4 digits.'
    else:
        return trials(user_input, i , j)    

def trials(user_input, i , j):
    random_list = generate_randoms()
    for n in (user_input):          # Checks if each of the entered digits is in a list
        if (int(n) in random_list): # Checks if the guessed number is in the right position 
            if (user_input.index(n) != random_list.index(int(n))):  
                i+= 1
            else:
                j+= 1
    return {'correct_pos': j, 'incorrect_pos': i}

