from random import randint

categories = ["Music Artists", "Animals", "Games"]
wordListArtists = ["Joji", "Eminem", "Drake"]
wordListAnimals = ["Fox", "Capybara", "Pigeon"]
wordListGames = ["Fortnite", "Dead by Daylight", "League of Legends"]

def chooseRandomItemInList(list):
    randomIndex = randint(0, len(list) - 1) ## Losuje index dla elementu listy (Początkowy index = 0, końcowy = długość listy)
    return list[randomIndex] ## Zwraca element listy z losowej pozycji

def hideTheWord(word):
    hiddenWord = ""
    print("The word is: ", word)
    for c in word:
        if c == " ":
            hiddenWord += " "
        else: 
            hiddenWord += "_"

    return hiddenWord

def startGuessing(word, hiddenWord):
    hiddenWord = list(hiddenWord) ## Konwersja na liste
    attempts = 0
    life = 8
    print("The game begins!, Enter a letter below :)")
    while life != 0: ## Game LOOP
        userLetter = input("> ")
        
        hit = False

        for i, c in enumerate(word.lower()): ## Loop po słowie 
            if c == userLetter.lower():
                hiddenWord[i] = word[i]
                hit = True

        if hit:
            print("Correct:", "".join(hiddenWord))
            attempts += 1
        else:
            print("Wrong!")
            life -= 1
            print("❤️: ", life)
            attempts += 1
            if life == 0:
                print("💔 You failed miserably")

        if "_" not in hiddenWord:
            print("You win!")
            print("Stats:")
            print("Attempts: ", attempts)
            print("❤️: ", life)
            break

if __name__ == '__main__':
    print("Welcome to HANGMAN THE GAME.")
    print("Choose your category: ")
    for key in categories:
        print(key)

    chosenCategory = input("> ")
    if chosenCategory.lower() in [c.lower() for c in categories]:
        print("Chosen category:", chosenCategory)
    
    print(chosenCategory)

    if chosenCategory.lower() == categories[0].lower():
        word = chooseRandomItemInList(wordListArtists)
        hiddenWord = hideTheWord(word)
        startGuessing(word, hiddenWord)
    elif chosenCategory.lower() == categories[1].lower():
        word = chooseRandomItemInList(wordListAnimals)
        hiddenWord = hideTheWord(word)
        startGuessing(word, hiddenWord)
    else:
        word = chooseRandomItemInList(wordListGames)
        hiddenWord = hideTheWord(word)
        startGuessing(word, hiddenWord)