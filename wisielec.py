from tkinter import *
from tkinter import ttk
from random import randint


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.lives = 6
        self.gameOver = False

        self.wordListArtists = [
            "Joji", 
            "Eminem", 
            "Drake", 
            "The Weeknd", 
            "Kendrick Lamar", 
            "Post Malone", 
            "Billie Eilish", 
            "Taylor Swift", 
            "Bruno Mars", 
            "Sabrina Carpenter", 
            "Arctic Monkeys", 
            "Imagine Dragons", 
            "Travis Scott", 
            "Lana Del Rey", 
            "Olivia Rodrigo", 
            "Gorillaz"
        ]

        self.wordListAnimals = [
            "Fox", 
            "Capybara", 
            "Pigeon", 
            "Penguin", 
            "Elephant", 
            "Tiger", 
            "Wolf", 
            "Otter", 
            "Koala", 
            "Dolphin", 
            "Crocodile", 
            "Giraffe", 
            "Kangaroo", 
            "Raccoon", 
            "Hedgehog" 
        ]

        self.wordListGames = [
            "Minecraft", 
            "Fortnite", 
            "League of Legends", 
            "Dead by Daylight", 
            "Valorant", 
            "Counter Strike", 
            "Apex Legends", 
            "Overwatch", 
            "Terraria", 
            "Stardew Valley", 
            "Cyberpunk 2077", 
            "Elden Ring", 
            "The Witcher", 
            "Brawl Stars", 
            "Rocket League" 
        ]

        self.selectedWord = ""
        self.hiddenWord = ""
        self.guessedLetters = []

        self.categoryFrame = ttk.Frame(root)
        self.gameFrame = ttk.Frame(root)

        self.showCategoryUI()
        self.showGameUI()

        self.gameFrame.pack_forget()
        self.categoryFrame.pack(fill="both", expand=True)

    ## Random element from word list
    def chooseRandom(self, list):
        return list[randint(0, len(list) - 1)]

    def chooseCategory(self, category):
        if category == "Artists":
            self.selectedWord = self.chooseRandom(self.wordListArtists)
        elif category == "Animals":
            self.selectedWord = self.chooseRandom(self.wordListAnimals)
        else:
            self.selectedWord = self.chooseRandom(self.wordListGames)

        # print("Wybrano:", self.selectedWord)

        self.guessedLetters = []
        self.lives = 6
        self.gameOver = False

        self.hiddenWord = self.hideTheWord(self.selectedWord)

        self.categoryFrame.pack_forget()
        self.gameFrame.pack(fill="both", expand=True)

        self.wordLabel.config(text=self.hiddenWord)
        self.livesLabel.config(text=f"❤️ Lives: {self.lives}")

    ## UI
    def showCategoryUI(self):
        ttk.Label(self.categoryFrame, text="Choose category", font=("Arial", 32)).pack(pady=20)

        ttk.Button(
            self.categoryFrame,
            text="Artists",
            command=lambda: self.chooseCategory("Artists")
        ).pack()

        ttk.Button(
            self.categoryFrame,
            text="Animals",
            command=lambda: self.chooseCategory("Animals")
        ).pack()

        ttk.Button(
            self.categoryFrame,
            text="Games",
            command=lambda: self.chooseCategory("Games")
        ).pack()

    def hideTheWord(self, word): 
        hiddenWord = "" 

        for c in word:
            if c == " ": 
                hiddenWord += "  " 
            else: hiddenWord += "_ " 

        return hiddenWord
    
    def showWinScreen(self):
        self.clearGame()

        ttk.Label(
            self.gameFrame,
            text="🎉 YOU WIN! 🎉",
            font=("Arial", 40)
        ).pack(pady=100)

        ttk.Button(
            self.gameFrame,
            text="RESTART",
            command=self.restartGame
        ).pack(pady=20)

    def showLoseScreen(self):
        self.clearGame()

        ttk.Label(
            self.gameFrame,
            text=f"💀 YOU LOST!\nWord was: {self.selectedWord}",
            font=("Arial", 30)
        ).pack(pady=100)
        
        ttk.Button(
            self.gameFrame,
            text="RESTART",
            command=self.restartGame
        ).pack(pady=20)


    def clearGame(self):
        for widget in self.gameFrame.winfo_children():
            widget.destroy()

    def restartGame(self):
        self.lives = 6
        self.gameOver = False
        self.selectedWord = ""
        self.guessedLetters = []

        for widget in self.gameFrame.winfo_children():
            widget.destroy()

    
        self.showGameUI()

    
        self.gameFrame.pack_forget()
        self.categoryFrame.pack(fill="both", expand=True)
    
    def showGameUI(self):
        ttk.Label(self.gameFrame, text="HANGMAN THE GAME", font=("Arial", 32)).pack(pady=20)

        ttk.Button(
            self.gameFrame,
            text="QUIT",
            command=self.root.destroy
        ).place(x = 720, y = 0)

        self.wordLabel = ttk.Label(
            self.gameFrame,
            text = "",
            font=("Consolas", 20)
        )
        self.wordLabel.pack(pady=20)

        self.entryWord = ttk.Entry(
            self.gameFrame,
            font=("Consolas", 20)
        )
        self.entryWord.pack(pady=20)
        self.entryWord.insert(0, "Enter the letter")

        ttk.Button(
            self.gameFrame,
            text="SUBMIT",
            command=self.guessLetter
        ).pack()

        self.livesLabel = ttk.Label(
            self.gameFrame,
            text="❤️ Lives: 6",
            font=("Consolas", 18)
        )
        self.livesLabel.pack(pady=10)

    def guessLetter(self):
        if self.gameOver:
            return
        
        letter = self.entryWord.get().lower()
        self.entryWord.delete(0, END)

        if not letter:
            return
        
        if letter in self.guessedLetters:
            return
        
        self.guessedLetters.append(letter)

        if letter not in self.selectedWord.lower():
            self.lives -= 1
            self.livesLabel.config(text=f"❤️ Lives: {self.lives}")

            if self.lives <= 0:
                self.gameOver = True
                self.showLoseScreen()
                return
            
        newHidden = ""

        for c in self.selectedWord:
            if c.lower() == letter:
                newHidden += c + " "
            elif c == " ":
                newHidden += "  "
            elif c.lower() in self.guessedLetters:
                newHidden += c + " "
            else: 
                newHidden += "_ "
        
        if letter not in self.guessedLetters:
            self.guessedLetters.append(letter)
        
        self.hiddenWord = newHidden

        self.wordLabel.config(text=self.hiddenWord)

        if "_" not in self.hiddenWord:
            self.gameOver = True
            self.showWinScreen()

## GAME START
root = Tk()
root.geometry("800x600")
root.resizable(False, False)

app = HangmanGame(root)

root.mainloop()