import pandas


data = pandas.read_csv("Day-26/nato_phonetic_alphabet.csv")


letter_dict = {
    row.letter:row.code for (index, row) in data.iterrows()
}


game_on = True
while game_on:
    code_list = []
    user_word = input("Enter a word: ").upper()
    code_list = [
        letter_dict[letter] for letter in user_word
    ]
    print(code_list)





