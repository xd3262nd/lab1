# Part 1

name = input('What is your name? ')
birthday_month = input('What month were you born in? ')

print(f'Hello, {name}!')

if birthday_month.lower() == 'august':
    print('Happy birthday month!')

print(f'There are {len(name)} letters in your name')


# Part 2
num_class = input('How many classes are you taking this semester? ')

counts = 0
class_list = list()

while not counts == int(num_class):
    class_name = input('Enter the name of the class: ')
    counts += 1
    class_list.append(class_name)


if int(num_class) == len(class_list):
    print('The classes you are taking are: ')
    for classes in class_list:
        print(classes)

# Part 3


def convert(sentence):

    # If the sentence is empty, nothing will be done
    if(len(sentence) == 0 ):
        return

    # Create an empty string
    new_sentence = ''

    # Change the entire sentence into lowercase
    lower_sentence = sentence.lower()
    # Get the first text as lowercase
    new_sentence += lower_sentence[0].lower()

    # Loop through each character within the sentence
    for i in range(1, len(lower_sentence)):

        if (lower_sentence[i] == ' '):
            new_sentence += lower_sentence[i+1].upper()
            i += 1
        elif (lower_sentence[i-1] != ' '):
            new_sentence += lower_sentence[i]

    print(new_sentence)




original_sentence = input('Please enter a sentence here: ')
convert(original_sentence)







