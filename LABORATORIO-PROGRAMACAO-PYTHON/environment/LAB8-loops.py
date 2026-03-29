import random  # importa a biblioteca para gerar número aleatório

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 10)  # gera número aleatório entre 1 e 10
isGuessRight = False  # controla se o usuário acertou

# loop continua até o usuário acertar
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    # verifica se o palpite está correto
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True  # encerra o loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        