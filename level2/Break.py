words = ['King','Sky','Blue','Fly','zero']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break;
    else:
        print(f"'{word}' has no vowels")
# in python for loop can have else
# for...else → the else runs when the for loop finishes without reaching break.
# Think of it as:

# break happened → don't run else
# break did NOT happen → run else
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)