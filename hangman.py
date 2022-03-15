import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

'''
Testing word
words = ['banana']'''

words = ["abruptly", "absurd", "abyss", "avenue", "awkward", "bagpipes", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "bookworm", "boxcar", "boxful", "buffalo", "buffoon", "buzzing", "cobweb", "cockiness", "crypt", "cycle", "daiquiri", "duplex", "dwarves", "embezzle", "equip", "espionage", "exodus", "faking", "fishhook", "fixable", "funny", "galaxy", "gazebo", "glyph", "gossip", "hyphen", "icebox", "injury", "ivory", "ivy", "jackpot", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "keyhole", "khaki", "kilobyte", "length", "lucky", "luxury","matrix", "microwave", "mystify", "nightclub", "nowadays", "nymph", "onyx", "ovary", "oxygen", "pajama", "pixel", "polka", "psyche", "puppy", "quartz", "queue", "quiz", "rhythm", "rickshaw", "scratch", "spritz", "staff", "strength", "stretch", "stronghold", "subway", "syndrome", "topaz", "transcript", "transplant", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "whiskey", "whomever", "witchcraft", "wizard", "woozy", "xylophone", "youthful", "yummy", "zephyr", "zigzag", "zilch", "zipper", "zodiac", "zombie"]

chosen_word = random.choice(words) # Choose a randon word
end_of_game = False
blank_list = []
word_size = len(chosen_word)
new_word = ""
lives = 6

for i in range(word_size):
    blank_list.append('_')

while not end_of_game:
    guess = input("Guess a letter:").lower()

# Check if the chosen letter is in the word
    for i in range(word_size):
            if chosen_word[i] == guess:
                blank_list[i] = guess # Substitute the blank space
            
    
    new_word = "".join(blank_list) # Turn the list on a string                         
    print(new_word)
        
    if new_word == chosen_word: # Check if words are identical
        print("You win!!!")   
        end_of_game = True
        
    if guess not in chosen_word: # Check if chosen letter is not in the word and take a like if true
        lives -= 1
        if lives == 0:
            print("You loose!")   
            end_of_game = True
            
    print(stages[lives])

        

              
    
            
    
        
       
                            



        
        
