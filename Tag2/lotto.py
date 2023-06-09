import random

# Eine Lottospiel-Simulation

#  4. Benutzer gibt 6 Ziffern ein: input ***
# - genau 6 Stück
# - zwischen 1 und 49
# - keine doppelten Werte
# - müssen danach als Liste von Integer vorliegen
# => [ integer ]


# 1. Es werden 6 Zufallszhalen aus 1-49 gezogen *
# schaeun Sie bei stackoverflow etc nach :-D
# => [ integer ]

# 2. Vergleichen von Tipp und Ziehung * Idee: mit einem Dummy-Tipp entwerfen 1 2 3 4 5 6
# => [ integer ]

# 3 .Ausgabe des Spielergebnisses print
# - Tipp (sortiert)
# - Ziehung (sortiert)
# - Anzahl Treffer
# - Trefferlist (sortiert)

import random

def validate_input(user_numbers, number_count=6, min_value=1, max_value=49):
    # Check if the length of the list is
    if len(user_numbers) != number_count:
        raise ValueError(f"You must enter exactly {number_count} numbers.")

    # Check if all numbers are unique
    if len(user_numbers) != len(set(user_numbers)):
        raise ValueError("All numbers must be unique.")

    # Check if all numbers are between  and
    for num in user_numbers:
        if num < min_value or num > max_value:
            raise ValueError(f"All numbers must be between {min_value} and {max_value}.")

    return True

def lottery_simulation():
    # Generate 6 random numbers
    drawn_numbers = random.sample(range(1, 50), 6)
    drawn_numbers.sort()

    # Get user input
    user_numbers = input("Enter 6 unique numbers between 1-49, separated by spaces: ").split()
    user_numbers = [int(num) for num in user_numbers]

    # Validate user input
    validate_input(user_numbers)

    user_numbers.sort()

    # Compare the lists
    matches = list(set(user_numbers) & set(drawn_numbers))
    matches.sort()

    # Print the results
    print("Your numbers: ", user_numbers)
    print("Drawn numbers: ", drawn_numbers)
    print("Number of matches: ", len(matches))
    print("Matches: ", matches)

lottery_simulation()
