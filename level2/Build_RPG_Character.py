# This stores the symbol for a filled dot.
full_dot = '●'

# This stores the symbol for an empty dot.
empty_dot = '○'


# Define a function called create_character.
# It accepts 4 arguments:
# name          → character's name
# strength      → STR stat
# intelligence  → INT stat
# charisma      → CHA stat
def create_character(name, strength, intelligence, charisma):


    # Check whether name is NOT a string.
    # isinstance(name, str) asks:
    # "Is name a string?"
    #
    # Example:
    # isinstance("ren", str) → True
    # isinstance(123, str)   → False
    #
    # "not" reverses True/False.
    # So this means:
    # "If name is NOT a string..."
    if not isinstance(name, str):

        # Stop the function and return this message.
        return "The character name should be a string"


    # Check whether the name has 0 characters.
    #
    # len(name) gives the number of characters.
    # len("ren") → 3
    # len("")    → 0
    #
    # So this means:
    # "If the name is empty..."
    elif len(name) == 0:

        return "The character should have a name"


    # Check whether the name has more than 10 characters.
    #
    # > means "greater than".
    #
    # len("abcdefghijk") → 11
    # 11 > 10 → True
    elif len(name) > 10:

        return "The character name is too long"


    # Check whether there is a space inside the name.
    #
    # " " is a space.
    #
    # " " in "hello world" → True
    # " " in "ren"          → False
    elif " " in name:

        return "The character name should not contain spaces"


    # Check whether any of the three stats is NOT an integer.
    #
    # strength, intelligence and charisma should all be int.
    #
    # "or" means:
    # If strength is not int
    # OR intelligence is not int
    # OR charisma is not int
    #
    # then return the error.
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):

        return "All stats should be integers"


    # Check whether any stat is less than 1.
    #
    # < means "less than".
    #
    # If even ONE stat is less than 1,
    # return the error.
    elif strength < 1 or intelligence < 1 or charisma < 1:

        return "All stats should be no less than 1"


    # Check whether any stat is greater than 4.
    #
    # > means "greater than".
    #
    # If even ONE stat is greater than 4,
    # return the error.
    elif strength > 4 or intelligence > 4 or charisma > 4:

        return "All stats should be no more than 4"


    # Add all three stats together.
    #
    # The total must be exactly 7.
    #
    # != means "NOT equal to".
    #
    # Example:
    # 4 + 2 + 1 = 7
    # 7 != 7 → False
    #
    # So the error will NOT happen.
    elif strength + intelligence + charisma != 7:

        return "The character should start with 7 points"


    # If none of the previous conditions returned an error,
    # Python reaches this else block.
    else:


        # Build the final character information as ONE string.
        #
        # \n means "new line".
        #
        # name + "\n"
        # means put the name, then move to the next line.
        #
        # full_dot * strength
        # means repeat ● according to strength.
        #
        # If strength = 4:
        # ● * 4 → ●●●●
        #
        # empty_dot * (10 - strength)
        # means create enough empty dots to make 10 dots total.
        #
        # If strength = 4:
        # 10 - 4 = 6
        # ○ * 6 → ○○○○○○

        return name + "\n" \
            + "STR " + full_dot * strength + empty_dot * (10 - strength) + "\n" \
            + "INT " + full_dot * intelligence + empty_dot * (10 - intelligence) + "\n" \
            + "CHA " + full_dot * charisma + empty_dot * (10 - charisma)


# Call the function.
#
# name = "ren"
# strength = 4
# intelligence = 2
# charisma = 1
#
# 4 + 2 + 1 = 7, so all validation passes.
#
# print() displays the value returned by the function.
print(create_character('ren', 4, 2, 1))