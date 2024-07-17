import random
def main():
    '''
    The main function will get input from the user to see if they would like to battle or see stat information on the Pokemon.
    '''

    print("Welcome to Pokemon Battle Game")
    print("")

    # run the list_pokemon function and store the restult in all_pokemon variable
    all_pokemon = list_pokemon()

    # get initial user input to see what they want to use the program for
    init_user_inp = input("Enter a Pokemon's name to see its stats.\nEnter '0' to get stat information about the Pokemon.\nEnter '1' to get a list of Pokemon.\nEnter '-1' to quit.\nEnter any other key to battle: ")

    # run the major functions of the program based on user input
    if init_user_inp == '0':
        stat_info()
    elif init_user_inp == '1':
        # print a list of pokemon in the game
        print("\nList of all Pokemon:")
        for pokemon in all_pokemon:
            print(pokemon)
        print("")
    elif init_user_inp == '-1':
        return
    elif init_user_inp in all_pokemon:
        print_stats(init_user_inp)
    else:
        # get user and CPU Pokemon randomly
        pokemon1, pokemon2 = get_two_random_pokemon(all_pokemon)

        # determine win by result of the Battle and print result
        if initiate_battle(pokemon1, pokemon2) == True:
            print("You win!")
        else:
            print("You lose!")

        # allow user to enter 'y' to restart the main function or quit the program by pressing any other key
    continue_game = input("Would you like to play again? (y/n): ")
    if continue_game == 'y':
        print(""
              ""
              ""
              ""
              "")
        main()
    else:
        print("Thank you for playing.")
        return

def list_pokemon():
    """This function gets and lists the names of the Pokemon"""

    # define pokemon_data as an empty dict
    pokemon_data = {}

    # read the pokemon_stats file and retrieve its data. Not all of it is necessary only, the keys.
    with open('pokemon_stats.txt', 'r') as file:
        for line in file:
            pokemon_info = line.strip().split(': ')
            pokemon_name = pokemon_info[0]
            pokemon_attributes = pokemon_info[1].split(', ')

            pokemon_data[pokemon_name] = {
                'Type 1': pokemon_attributes[0],
                'Type 2': pokemon_attributes[1],
                'Move 1': pokemon_attributes[2],
                'Move 2': pokemon_attributes[3],
                'Move 3': pokemon_attributes[4],
                'Move 4': pokemon_attributes[5],
                'HP': int(pokemon_attributes[6]),
                'Attack': int(pokemon_attributes[7]),
                'Defense': int(pokemon_attributes[8]),
                'Special Attack': int(pokemon_attributes[9]),
                'Special Defense': int(pokemon_attributes[10]),
                'Speed': int(pokemon_attributes[11]),
            }

    return list(pokemon_data.keys())

def stat_info():
    '''
    This function will get stat information about the Pokemon. It says which type each Pokemon is and will rank them by stat totals.
    '''

    # define pokemon_data as an empty dict
    pokemon_data = {}

    with open('pokemon_stats.txt', 'r') as file:
        for line in file:
            pokemon_info = line.strip().split(': ')
            pokemon_name = pokemon_info[0]
            pokemon_attributes = pokemon_info[1].split(", ")

            # Create dictionary entry with correct data types
            pokemon_data[pokemon_name] = {
                'Type 1': pokemon_attributes[0],
                'Type 2': pokemon_attributes[1],
                'Move 1': pokemon_attributes[2],
                'Move 2': pokemon_attributes[3],
                'Move 3': pokemon_attributes[4],
                'Move 4': pokemon_attributes[5],
                'HP': int(pokemon_attributes[6]),
                'Attack': int(pokemon_attributes[7]),
                'Defense': int(pokemon_attributes[8]),
                'Special Attack': int(pokemon_attributes[9]),
                'Special Defense': int(pokemon_attributes[10]),
                'Speed': int(pokemon_attributes[11]),
            }

        # Calculate total stats for each Pokemon and store them in a dictionary
        pokemon_stats_total = {}
        for pokemon, attributes in pokemon_data.items():
            total_stats = attributes['HP'] + attributes['Attack'] + attributes['Defense'] + attributes['Special Attack'] + attributes['Special Defense'] + attributes['Speed']
            pokemon_stats_total[pokemon] = total_stats

        # Sort Pokemon by their total stats in descending order
        sorted_pokemon_stats = sorted(pokemon_stats_total.items(), key=lambda x: x[1], reverse=True)

        # List Pokemon with the highest stat total
        highest_stat_pokemon = sorted_pokemon_stats[0][0]
        print("")
        print(f"The Pokemon with the highest stat total: {highest_stat_pokemon} (Stat Total: {pokemon_stats_total[highest_stat_pokemon]})")

        # List Pokemon with the lowest stat total
        lowest_stat_pokemon = sorted_pokemon_stats[-1][0]
        print("")
        print(f"The Pokemon with the lowest stat total: {lowest_stat_pokemon} (Stat Total: {pokemon_stats_total[lowest_stat_pokemon]})")

        # List Pokemon with the highest HP stat
        highest_hp_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['HP'])
        print("")
        print(f"The Pokemon with the highest HP stat is: {highest_hp_pokemon} (HP: {pokemon_data[highest_hp_pokemon]['HP']})")

        # List Pokemon with the lowest HP stat
        lowest_hp_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['HP'])
        print("")
        print(f"The Pokemon with the lowest HP stat is: {lowest_hp_pokemon} (HP: {pokemon_data[lowest_hp_pokemon]['HP']})")

        # List Pokemon with the highest attack stat
        highest_attack_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Attack'])
        print("")
        print(f"The Pokemon with the highest Attack stat is: {highest_attack_pokemon} (Attack: {pokemon_data[highest_attack_pokemon]['Attack']})")

        # List Pokemon with the lowest attack stat
        lowest_attack_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Attack'])
        print("")
        print(f"The Pokemon with the lowest Attack stat is: {lowest_attack_pokemon} (Attack: {pokemon_data[lowest_attack_pokemon]['Attack']})")

        # List Pokemon with the highest defense stat
        highest_defense_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Defense'])
        print("")
        print(f"The Pokemon with the highest Defense stat is: {highest_defense_pokemon} (Defense: {pokemon_data[highest_defense_pokemon]['Defense']})")

        # List Pokemon with the lowest defense stat
        lowest_defense_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Defense'])
        print("")
        print(f"The Pokemon with the lowest Defense stat is: {lowest_defense_pokemon} (Defense: {pokemon_data[lowest_defense_pokemon]['Defense']})")

        # List Pokemon with the highest special attack stat
        highest_spattack_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Special Attack'])
        print("")
        print(f"The Pokemon with the highest Special Attack stat is: {highest_spattack_pokemon} (Special Attack: {pokemon_data[highest_spattack_pokemon]['Special Attack']})")

        # List Pokemon with the lowest special attack stat
        lowest_spattack_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Special Attack'])
        print("")
        print(f"The Pokemon with the lowest Special Attack stat is: {lowest_spattack_pokemon} (Special Attack: {pokemon_data[lowest_spattack_pokemon]['Special Attack']})")

        # List Pokemon with the highest special defense stats
        highest_spdefense_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Special Defense'])
        print("")
        print(f"The Pokemon with the highest Special Defense stat is: {highest_spdefense_pokemon} (Special Defense: {pokemon_data[highest_spdefense_pokemon]['Special Defense']})")

        # List Pokemon with the lowest special defense stats
        lowest_spdefense_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Special Defense'])
        print("")
        print(f"The Pokemon with the lowest Special Defense stat is: {lowest_spdefense_pokemon} (Special Defense: {pokemon_data[lowest_spdefense_pokemon]['Special Defense']})")

        # List Pokemon with the highest speed stat
        highest_speed_pokemon = max(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Speed'])
        print("")
        print(f"The Pokemon with the highest Speed stat is: {highest_speed_pokemon} (Speed: {pokemon_data[highest_speed_pokemon]['Speed']})")

        # List Pokemon with the lowest speed stat
        lowest_speed_pokemon = min(pokemon_data, key=lambda pokemon: pokemon_data[pokemon]['Speed'])
        print("")
        print(f"The Pokemon with the lowest Speed stat is: {lowest_speed_pokemon} (Speed: {pokemon_data[lowest_speed_pokemon]['Speed']})")
        print("")

def read_file_and_get_stats(input_file):
    '''Function Reads The pokemon_stats.txt file and retrieves stats and stores them in a dictionary.'''
    pokemon_data = {}
    with open(input_file, 'r') as file:
        for line in file:
            pokemon_info = line.strip().split(': ')
            pokemon_name = pokemon_info[0]
            pokemon_attributes = pokemon_info[1].split(", ")

            # Create dictionary entry with correct data types
            pokemon_data[pokemon_name] = {
                'Type 1': pokemon_attributes[0],
                'Type 2': pokemon_attributes[1],
                'Move 1': pokemon_attributes[2],
                'Move 2': pokemon_attributes[3],
                'Move 3': pokemon_attributes[4],
                'Move 4': pokemon_attributes[5],
                'HP': int(pokemon_attributes[6]),
                'Attack': int(pokemon_attributes[7]),
                'Defense': int(pokemon_attributes[8]),
                'Special Attack': int(pokemon_attributes[9]),
                'Special Defense': int(pokemon_attributes[10]),
                'Speed': int(pokemon_attributes[11]),
            }
    return pokemon_data

def print_stats(input_pokemon):
    '''Function Prints Stats of specific Pokemon.'''

    # read the pokemon_stats file and store all the data in the variable pokemon_data
    pokemon_data = read_file_and_get_stats('pokemon_stats.txt')

    hp = pokemon_data[input_pokemon]['HP']
    attack = pokemon_data[input_pokemon]['Attack']
    defense = pokemon_data[input_pokemon]['Defense']
    spattack = pokemon_data[input_pokemon]['Special Attack']
    spdefense = pokemon_data[input_pokemon]['Special Defense']
    speed = pokemon_data[input_pokemon]['Speed']
    type1 = pokemon_data[input_pokemon]['Type 1']
    type2 = pokemon_data[input_pokemon]['Type 2']

    # run if statement to see if printing type 2 is necessary since not all Pokemon have a secondary typing
    if type2 == None:
        print("")
        print(f"{input_pokemon}'s HP stat is: {hp}")
        print(f"{input_pokemon}'s Attack stat is: {attack}")
        print(f"{input_pokemon}'s Defense stat is: {defense}")
        print(f"{input_pokemon}'s Special Attack stat is: {spattack}")
        print(f"{input_pokemon}'s Special Defense stat is: {spdefense}")
        print(f"{input_pokemon}'s Speed stat is: {speed}")
        print(f"{input_pokemon}'s primary typing is: {type1}")
        print("")
    else:
        print("")
        print(f"{input_pokemon}'s HP stat is: {hp}")
        print(f"{input_pokemon}'s Attack stat is: {attack}")
        print(f"{input_pokemon}'s Defense stat is: {defense}")
        print(f"{input_pokemon}'s Special Attack stat is: {spattack}")
        print(f"{input_pokemon}'s Special Defense stat is: {spdefense}")
        print(f"{input_pokemon}'s Speed stat is: {speed}")
        print(f"{input_pokemon}'s primary typing is: {type1}")
        print(f"{input_pokemon}'s secondary typing is: {type2}")
        print("")




'''Battle Functions'''
def get_two_random_pokemon(input_pokemon_list):
    """This function generates 2 random numbers which correspond to the user_pokemon and cpu_pokemon, based on the Pokemon's key in the dict"""
    randi1 = random.randint(0, len(input_pokemon_list) - 1)
    randi2 = randi1
    while randi1 == randi2:
        randi2 = random.randint(0, len(input_pokemon_list) - 1)

    return input_pokemon_list[randi1], input_pokemon_list[randi2]

def fetch_stats(input_pokemon):
    """This function returns the stats of a Pokemon by calling the read_file_and_get stats function and storing the values in the given variables """
    pokemon_data = read_file_and_get_stats('pokemon_stats.txt')
    hp = pokemon_data[input_pokemon]['HP']
    attack = pokemon_data[input_pokemon]['Attack']
    defense = pokemon_data[input_pokemon]['Defense']
    spattack = pokemon_data[input_pokemon]['Special Attack']
    spdefense = pokemon_data[input_pokemon]['Special Defense']
    speed = pokemon_data[input_pokemon]['Speed']
    type1 = pokemon_data[input_pokemon]['Type 1']
    type2 = pokemon_data[input_pokemon]['Type 2']
    move1 = pokemon_data[input_pokemon]['Move 1']
    move2 = pokemon_data[input_pokemon]['Move 2']
    move3 = pokemon_data[input_pokemon]['Move 3']
    move4 = pokemon_data[input_pokemon]['Move 4']

    return hp, attack, defense, spattack, spdefense, speed, type1, type2, move1, move2, move3, move4

def initiate_battle(user_pokemon, cpu_pokemon):
    '''This function starts the battle'''

    # Determines HP multiplier, applied to both CPU & User Pokemon
    hp_multiplier = 2.5

    # Fetch stats for both the user pokemon and the CPU pokemon
    user_stats = fetch_stats(user_pokemon)
    cpu_stats = fetch_stats(cpu_pokemon)

    # Print which Pokemon user and CPU are using
    print("")
    print("You are using", user_pokemon)
    print("Your foe is using", cpu_pokemon)
    print("")

    # Sets user_stats and cpu_stats tuples equal to local variables which can be used and modified
    raw_user_hp, user_attack, user_defense, user_spattack, user_spdefense, user_speed, user_type1, user_type2, user_move1, user_move2, user_move3, user_move4 = user_stats
    raw_cpu_hp, cpu_attack, cpu_defense, cpu_spattack, cpu_spdefense, cpu_speed, cpu_type1, cpu_type2, cpu_move1, cpu_move2, cpu_move3, cpu_move4 = cpu_stats

    # Adjust CPU and user HP according to HP multiplier
    user_hp = raw_user_hp*hp_multiplier
    cpu_hp = raw_cpu_hp*hp_multiplier

    # initiates the while loop to establish that the battle does not end until either the user pokemon HP or CPU pokemon HP <= 0
    while user_hp > 0 and cpu_hp > 0:
        # Updates the user how much HP each Pokemon has
        print("")
        print(f"{user_pokemon} has {user_hp} hp.")
        print(f"{cpu_pokemon} has {cpu_hp} hp.")
        print("")

        # If statement determines which Pokemon attacks first based on their respective speed stats
        if user_speed >= cpu_speed:
            # Subtracts the user_turn function's return value from CPU's hp and returns the win as True immediately if CPU HP is less than 0
            cpu_hp -= user_turn(user_attack, user_spattack, cpu_defense, cpu_spdefense, cpu_type1, cpu_type2, user_type1, user_type2, user_move1, user_move2, user_move3, user_move4)
            if cpu_hp <= 0:
                win = True
                break
            user_hp -= cpu_turn(cpu_attack, cpu_spattack, user_defense, user_spdefense, user_type1, user_type2, cpu_type1, cpu_type2, cpu_move1, cpu_move2, cpu_move3, cpu_move4)
            if user_hp <= 0:
                win = False
                break
        else:
            user_hp -= cpu_turn(cpu_attack, cpu_spattack, user_defense, user_spdefense, user_type1, user_type2, cpu_type1, cpu_type2, cpu_move1, cpu_move2, cpu_move3, cpu_move4)
            if user_hp <= 0:
                win = False
                break
            cpu_hp -= user_turn(user_attack, user_spattack, cpu_defense, cpu_spdefense, cpu_type1, cpu_type2, user_type1, user_type2, user_move1, user_move2, user_move3, user_move4)
            if cpu_hp <= 0:
                win = True
                break

    # The initiate_battle function returns win, which is a bool value that indicates whether the user won or lost the battle
    return win

def user_turn(user_attack, user_spattack, cpu_defense, cpu_spdefense, cpu_type1, cpu_type2, user_type1, user_type2, user_move1, user_move2, user_move3, user_move4):
    """The user_turn function is used to carry out the user turn and return the damage output"""
    while True:
        try:
            move_input = input(f"Moves:\n1. {user_move1}\n2. {user_move2}\n3. {user_move3}\n4. {user_move4}\n\nPlease enter a number between 1 and 4: ")

            # Convert the input to an integer
            move_index = int(move_input)

            # Check if the input is within the valid range (1 to 4)
            if 1 <= move_index <= 4:
                if move_index == 1:
                    move = user_move1
                elif move_index == 2:
                    move = user_move2
                elif move_index == 3:
                    move = user_move3
                elif move_index == 4:
                    move = user_move4
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-4).")

    adjusted_cpu_defense = cpu_defense/2
    adjusted_cpu_spdefense = cpu_spdefense/2

    attack_defense_difference = user_attack - adjusted_cpu_defense
    spattack_spdefense_difference = user_spattack - adjusted_cpu_spdefense

    # Prevents Negative Damage
    if attack_defense_difference <= 1:
        attack_defense_difference = 1
    if spattack_spdefense_difference <= 1:
        spattack_spdefense_difference = 1

    # Calculate damage
    move_form = get_move_damage(move)['Move Form']

    # Check to see if attack type is special or physical
    if move_form == 'Physical':
        difference_multiplier = (attack_defense_difference / 100)
    elif move_form == 'Special':
        difference_multiplier = (spattack_spdefense_difference / 100)
    else:
        print('user_turn() move_form check error!')

    # Calculates move damage based on conditions
    move_damage = int(get_move_damage(move)['Move Damage'])
    move_accuracy = int(get_move_damage(move)['Move Accuracy'])
    move_type = get_move_damage(move)['Move Type']
    is_super_effective = effectiveness(move_type, cpu_type1, cpu_type2)
    type_attack_bonus = attack_type_bonus(move_type, user_type1, user_type2)
    move_success = rand_acc_check(move_accuracy)

    damage_output = (move_damage * difference_multiplier)
    damage_output *= is_super_effective

    if type_attack_bonus == True:
        damage_output = damage_output*1.5

    # Checks to see if move hit or not
    if move_success == True:
        damage_output = damage_output
        # Print if the move was super effective, not very effective, etc.
        print("")
        print(f"Your Pokemon used {move}!")
        if is_super_effective > 1:
            print("It was super effective.")
        elif is_super_effective < 1 and is_super_effective > 0:
            print("It was not very effective.")
        elif is_super_effective == 0:
            print("It had no effect.")
        print('You did ', damage_output, 'damage.')
        print("")
    else:
        print("")
        damage_output = damage_output*0
        print(f"Your Pokemon used {move}!")
        print("Your attack missed.")
        print("")

    return damage_output

def cpu_turn(cpu_attack, cpu_spattack, user_defense, user_spdefense, user_type1, user_type2, cpu_type1, cpu_type2, cpu_move1, cpu_move2, cpu_move3, cpu_move4):
    """The cpu_turn function is used to carry out the CPU turn and return the damage output"""
    while True:
        randi = random.randint(1, 4)
        if randi == 1:
            move = cpu_move1
        elif randi == 2:
            move = cpu_move2
        elif randi == 3:
            move = cpu_move3
        else:
            move = cpu_move4

        adjusted_user_defense = (user_defense / 2)
        adjusted_user_spdefense = (user_spdefense / 2)

        attack_defense_difference = cpu_attack - adjusted_user_defense
        spattack_spdefense_difference = cpu_spattack - adjusted_user_spdefense


        if attack_defense_difference <= 1:
            attack_defense_difference = 1

        if spattack_spdefense_difference <= 1:
            spattack_spdefense_difference = 1

        move_form = get_move_damage(move)['Move Form']

        if move_form == 'Physical':
            difference_multiplier = (attack_defense_difference / 100)
        elif move_form == 'Special':
            difference_multiplier = (spattack_spdefense_difference / 100)
        else:
            print('cpu_turn() move_form error!')

        # Calculate move damage
        move_damage = int(get_move_damage(move)['Move Damage'])
        move_accuracy = int(get_move_damage(move)['Move Accuracy'])
        move_type = get_move_damage(move)['Move Type']
        is_super_effective = effectiveness(move_type, user_type1, user_type2)
        type_attack_bonus = attack_type_bonus(move_type, cpu_type1, cpu_type2)
        move_success = rand_acc_check(move_accuracy)

        damage_output = (move_damage * difference_multiplier)
        damage_output *= is_super_effective

        # Multiply damage output by 1.5 if the type_attack bonus returns True
        if type_attack_bonus == True:
            damage_output = damage_output*1.5

        if move_success == True:
            damage_output = damage_output
            # Print if move is super effect, not very effective, etc.
            print("")
            print(f"Your foe's Pokemon used {move}!")
            if is_super_effective > 1:
                print("It was super effective.")
            elif is_super_effective < 1 and is_super_effective > 0:
                print("It was not very effective.")
            elif is_super_effective == 0:
                print("It had no effect.")
            print('They did ', damage_output, 'damage.')
            print("")
        else:
            damage_output = 0
            print("")
            print(f"Your foe's Pokemon used {move}!")
            print("The foe's attack missed.")
            print("")

        return damage_output


def get_move_damage(move):
    '''The get_move_damage function reads the pokemon_moves.txt file and returns all its data(not just damage)'''
    move_data = {}
    with open('pokemon_moves.txt', 'r') as file:
        for line in file:
            move_info = line.strip().split(': ')
            move_name = move_info[0]
            move_attributes = move_info[1].split(", ")

            move_data[move_name] = {
                'Move Type': move_attributes[0],
                'Move Damage': move_attributes[1],
                'Move Accuracy': move_attributes[2],
                'Move Form': move_attributes[3],
            }

    # Check if the move exists in move_data
    if move in move_data:
        return move_data[move]
    else:
        # Handle case where move doesn't exist
        return {'Move Type': 'Unknown', 'Move Damage': '0', 'Move Accuracy': '0', 'Move Form': 'Unknown'}

def effectiveness(move_type, type1, type2):
    '''The effectiveness function returns effectiveness based on the move_type, and the primary and secondary type of the defending Pokemon.
    This function returns 0, .25, .5, 1, 2, or 4'''

    # Defines effectiveness_data1 as an empty dict for which types a type is super effective against
    effectiveness_data1 = {}

    # Defines effectiveness_data2 as an empty dict for which types a type is not very effective against
    effectiveness_data2 = {}

    # Defines effectiveness_data2 as an empty dict for which types a type has no effect on
    effectiveness_data3 = {}

    # Reads super effective file
    with open('super_effective_types.txt', 'r') as file:
        for line in file:
            effectiveness_info = line.strip().split(': ')
            if len(effectiveness_info) >= 2:
                type_name = effectiveness_info[0]
                super_effective_types = effectiveness_info[1].split(', ')
                effectiveness_data1[type_name] = super_effective_types

    # Reads not very effective file
    with open('not_very_effective_types.txt', 'r') as file:
        for line in file:
            resistance_info = line.strip().split(': ')
            if len(resistance_info) >= 2:
                type_name_r = resistance_info[0]
                not_very_effective_types = resistance_info[1].split(', ')
                effectiveness_data2[type_name_r] = not_very_effective_types

    # Reads no effect file
    with open('no_effect_types.txt', 'r') as file:
        for line in file:
            no_effect_info = line.strip().split(': ')
            if len(no_effect_info) >= 2:
                type_name_n = no_effect_info[0]
                no_effect_types = no_effect_info[1].split(', ')
                effectiveness_data3[type_name_n] = no_effect_types

    # Initiates effect equal to 1, which is the base case
    effect = 1

    # Checks to see if move_type is in effectiveness_data1 dict
    if move_type in effectiveness_data1:
        # If the move type is super effective again the primary type of the defending Pokemon, multiply effectiveness by 2
        if type1 in effectiveness_data1[move_type]:
            effect *= 2
        # If the move type is super effective again the secondary type of the defending Pokemon, multiply effectiveness by 2 again or for the first time
        if type2 in effectiveness_data1[move_type]:
            effect *= 2

    # Checks to see if move_type is in effectiveness_data2 dict
    if move_type in effectiveness_data2:
        # If the move type is super effective again the primary type of the defending Pokemon, multiply effectiveness by .5
        if type1 in effectiveness_data2[move_type]:
            effect *= 0.5
        # If the move type is super effective again the primary type of the defending Pokemon, multiply effectiveness by .5 again or for the first time
        if type2 in effectiveness_data2[move_type]:
            effect *= 0.5

    # Checks to see if move_type is in effectiveness_data3 dict
    if move_type in effectiveness_data3:
        # If the move type has no effect on either the primary or the secondary type set effect to zero
        if type1 in effectiveness_data3[move_type] or type2 in effectiveness_data3[move_type]:
            effect = 0

    return effect
def attack_type_bonus(move_type, type1, type2):
    '''This function determines whether a move will have same att. bonus applied or not'''
    if move_type == type1 or move_type == type2:
        return True
    else:
        return False

def rand_acc_check(accuracy):
    randi = random.randint(1, 100)

    if randi > accuracy:
        return False
    else:
        return True



# Calls main funciton
if __name__ == "__main__":
    main()
