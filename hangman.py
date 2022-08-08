import click
import random

words = []
with open('c:/Users/D0298891/Desktop/deutsch.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split('\n')]
        words.append(inner_list)

won = False
fails = 0
keyword = ''
keyword_array = []
amount_letters = 0


@click.group()
def main():
    pass


@main.command()
def play():    
    fails = 0
    game_over = False
    found_array = []
    found_letters = 0

    keyword = random.choice(words)[0].lower()
    amount_letters = len(keyword)

    for i in keyword:
        keyword_array.append(i)

    for i in range(amount_letters):
        found_array.append('_')
    
    click.echo("Your word: {}".format(found_array))
    click.echo("Tries: {}/5".format(fails))

    while not game_over:
        guess = click.prompt(" Enter your guess: ", type=str).lower()
        found_letters_save = found_letters
        for i in range(len(keyword_array)):
            if guess == keyword_array[i]:
                found_letters += 1
                found_array[i] = guess
        if found_letters == found_letters_save:
            fails += 1
            click.echo('The letter "{}" is not part of the word. Try {}/5'.format(guess, fails))
        else:
            click.echo('Hit! Updated word: {}'.format(found_array))

        if fails == 5:
            game_over = True
            won = False
            click.echo('Game Over. The word was {}'.format(keyword))

        if keyword_array == found_array:
            game_over = True
            won = True
            click.echo('You WIN!!!')


if __name__ == "__main__":
    main()