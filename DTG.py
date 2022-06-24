# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment 
# if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

print('Thank you for choosing Day Trip Generator! We hope to create a trip you are happy with!')

import random 
destinations = ['Humboldt Park', 'South Shore Beach', 'The Historic 3rd Ward', 'The Upper East Side']

import random
restaurants = ['Cafe LuLu', 'Guanuato Mexcian', 'DanDan Chinese Cuisine', 'Maharaja Indian Cuisine']

import random
transportation = ['biking', 'taking the bus', ' calling an Uber', 'renting a limosine']

import random
entertainment = ['See a movie at the Avalon Theater', 'Watch the Bucks game at Fiserv Forum', 'Attend a concert at the Summerfest Grounds', 'Tour the Art Museum']

def get_destination():
    destination_choice = random.choice(destinations)
    print(f'We have chosen {destination_choice} as your destination.')
    return destination_choice
get_destination()

def get_restaurant():
    restaraunt_choice = random.choice(restaurants)
    print(f'We have chosen {restaraunt_choice} as your restaurant.')
    return restaraunt_choice
get_restaurant()

def get_transportation():
    transportation_choice = random.choice(transportation)
    print(f'We have chosen {transportation_choice} as your method of transport.')
    return transportation_choice
get_transportation()

def get_entertainment():
    entertainment_choice = random.choice(entertainment)
    print(f'And, we have chosen {entertainment_choice} as your entertainment option!')
    return entertainment_choice
get_entertainment()

def get_user_opinion():
    print('Are you happy with all of your results?')
    opinion = input('yes or no? ')
    return opinion
result = get_user_opinion()

def settle_opinion(response):
    if response == 'no':
        print("Oh no! We're sorry you're not happy with your results. No problem, let's change that!")
    elif response == 'yes':
        print("Perfect! we're happy that you're happy!")
settle_opinion(result)

def get_change(response):
    if response == 'no':
        print('What would you like to change?')
        change = input ("enter '1' for destination, enter '2' for restaurant, enter '3' for transport, and enter '4' for entertainment: ")
        return change
change_result = get_change(result)

def get_rerun(response):
    new_destination_choice = random.choice(destinations)
    cont_loop = True
    while cont_loop == True:
        if change_result == '1':
            print(f'How about {new_destination_choice} as your destination? ')
            decision = input('yes or no? ')
        if decision == 'yes':
            cont_loop = False
        else:
            cont_loop = True
get_rerun(change_result)



    













































