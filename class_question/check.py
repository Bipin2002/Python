sentence = input('Type a Sentence: ')
if sentence[0] == 'y' or sentence[0] == 'Y' or sentence[0] == 'p' or sentence[0] == 'P':
    print(f'The Sentence start from "{sentence[0]}".')
else:
    print('The Sentence doesnot start from "y" or "p".')
