print('Thank you for choosing Day Trip Generator! We hope to create a trip you are happy with!')

import random 
destinations = ['Humboldt Park', 'South Shore Beach', 'The Historic 3rd Ward', 'The Upper East Side']

restaurants = ['Cafe LuLu', 'Guanuato Mexcian', 'DanDan Chinese Cuisine', 'Maharaja Indian Cuisine']

transportation = ['biking', 'taking the bus', ' calling an Uber', 'renting a limosine']

entertainment = ['See a movie at the Avalon Theater', 'Watch the Bucks game at Fiserv Forum', 'Attend a concert at the Summerfest Grounds', 'Tour the Art Museum']

def get_destination():
    destination_choice = random.choice(destinations)
    print(f'We have chosen {destination_choice} as your destination. Does this sound good to you? ')
    user_input = None
    while user_input != 'yes':
        user_input = input('yes or no? ')
        if user_input == 'yes':
            print("Great! Now, let's get you a place to dine!")
        elif user_input == 'no':
            destination_choice = random.choice(destinations)
            print(f"Oh no! Let's try something else. How does {destination_choice} sound? ")
    return destination_choice
dest = get_destination()

def get_restaurant():
    restaurant_choice = random.choice(restaurants)
    print(f'We have chosen {restaurant_choice} as your restaurant. Does this sound good to you? ')
    user_input = None
    while user_input != 'yes':
        user_input = input('yes or no? ')
        if user_input == 'yes':
            print("Great! Now, let's get you a way around town. ")
        elif user_input == 'no':
            restaurant_choice = random.choice(restaurants)
            print(f"Oh no! Let's try something else. How does {restaurant_choice} sound? ")
    return restaurant_choice
food = get_restaurant()

def get_transportation():
    transportation_choice = random.choice(transportation)
    print(f'We have chosen {transportation_choice} as your method of transport. Does this sound good to you? ')
    user_input = None
    while user_input != 'yes':
        user_input = input('yes or no? ')
        if user_input == 'yes':
            print("Great! Finally, let's get you some entertainment for the night!")
        elif user_input == 'no':
            transportation_choice = random.choice(transportation)
            print(f"Oh no! Let's change that. How does {transportation_choice} sound? ")
    return transportation_choice
trans = get_transportation()

def get_entertainment():
    entertainment_choice = random.choice(entertainment)
    print(f'And, we have chosen {entertainment_choice} as your entertainment option! Does this sound good to you? ')
    user_input = None
    while user_input != 'yes':
        user_input = input('yes or no? ')
        if user_input == 'yes':
            print("Great! Let's confirm your trip.")
        elif user_input == 'no':
            entertainment_choice = random.choice(entertainment)
            print(f"Oh no! Let's change that. How does {entertainment_choice} sound? ")
    return entertainment_choice
fun = get_entertainment()

def get_confirmation():
    print('Would you like to confirm your trip? ')
    user_input = input('yes or no? ')
    if user_input == 'yes':
        print(f'Great! the trip we have planned for you is head to {dest}, enjoy some {food}, travel by {trans}, and {fun}')
    elif user_input == 'no':
        print("We're sorry we weren't able to create a trip you were happy with, please feel free to try again whenever you please!")
get_confirmation()
