import random
import hangman_art

words = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard''woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']

display = []
string = ''
lifes = len(hangman_art.stages) - 1
game_over = False
letter_list = []


#Randonly choose the world
chosen_word = random.choice(words)
#print(f'The word is {chosen_word}')

word_lenght = len(chosen_word)

#Hide the word with '_'
for n in range(word_lenght):
    display.append('_ ')
    
print(hangman_art.logo)

while game_over == False:
    chosen_letter = input('Guess a letter: ')
    letter_list.append(chosen_letter)
    
    if chosen_letter in display:
      print("You've already chose this letter. Try another one.")
    
    if chosen_word.count(chosen_letter) != 0:
        for n in range(word_lenght):
            if chosen_letter == chosen_word[n]: 
                display[n] = chosen_letter
    else:
        lifes -= 1
        print(f'You guessed {chosen_letter}. That is not in the word, you loose a life')
        if lifes == 0:
          print('Game Over. You lost!')
          game_over = True
        else:
          print(f"You guessed {chosen_letter}, that's not in the word. You loose a life.")
        
    print(hangman_art.stages[lifes])

    string = ''.join(display)          
    print(string)
    
    #Finishing the game    
    if string.count('_ ') == 0:
        game_over = True
    
