import random
from colorama import init, Fore, Back, Style
import requests
def main():
  rulesOfTheGame = '''Guess the 5 letter word (wordle) in 6 tries
  If you guess the word, all letters are green, you won
  If you guess wrong, you get hints based on the wordle (word to guess)
  A green hint is displayed if the letter in your guess is also in the wordle and at the same position 🟩
  A yellow hint is displayed if the letter in your guess is also in the wordle but at the wrong position 🟨
  No hint is displayed if the letter in your guess is not in the wordle ⬜
  If you have not guessed the word after 6 tries, you lost
  If you have not guessed the word after 6 tries, the wordle is revealed'''
  
  print('Welcome to the Game \n\nHere are the rules: ', rulesOfTheGame)



def playGame():
  
  def is_english_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    response = requests.get(url + word)
    return response.status_code == 200
  
  def from_list():
    url = 'https://raw.githubusercontent.com/Eric-Lloyd/wordle-list/main/words-dict.json'
    response =requests.get (url)
    json_dict=response.json()
    
    return(json_dict['words'])
   
  
  def is_valid(word):
    if not len(word) == 5:
      return False
    return is_english_word(word)
  
  
  wordOfTheDay = random.choice(from_list())
  #print('\n'+ wordOfTheDay)
  
  
  
  def colours(userGuess, wordOfTheDay):
    hint = ""
    for inx in range(len(userGuess)):
        if wordOfTheDay[inx] == userGuess[inx]:
          hint = hint + Fore.WHITE+Back.GREEN+userGuess[inx].center(3)
          hint = hint + Style.RESET_ALL
  
        elif userGuess[inx] in wordOfTheDay:
          hint = hint + Fore.WHITE+Back.YELLOW+userGuess[inx].center(3)
          hint = hint + Style.RESET_ALL
  
        else:
          hint = hint +  Fore.BLACK+Back.WHITE+userGuess[inx].center(3)
          hint = hint + Style.RESET_ALL
    return hint
  
  
  def hasAnyGreenLetter(guess, answer):
    for inx in range(len(guess)):
      if answer[inx] == guess[inx]:
        return True
    return False
  
  def hasAnyYellowLetter(guess, answer):
    for inx in range(len(guess)):
      if guess[inx] in answer:
        return True
    return False
  
  def getUserFeedback(userGuess, wordOfTheDay):
      if attempt > 0:
          if hasAnyGreenLetter(userGuess, wordOfTheDay):
              return 'Great job! You have one or more correct letters in the right position. Keep going!'
          elif hasAnyYellowLetter(userGuess, wordOfTheDay):
              return 'Almost there! Some of your letters are correct, but they need to be rearranged. Keep guessing!'
          else:
              return 'Oops! None of the letters you guessed are correct. Keep trying!'
  
      return ''
        
     
  
  
  attempt = 6
  
  while attempt >0:
    userGuess = str(input('\nGuess the word: '))
    
   
    if is_valid(userGuess): 
      attempt -= 1
  
      print(colours(userGuess, wordOfTheDay))
  
      def printAttemptMessage(attempt,wordOfTheDay):
        if attempt ==1:
          print('Last chance! Only 1 try left.')
        elif attempt==0:
          print('You lost! :( The word of the day is '+ Fore.WHITE + Back.RED + wordOfTheDay + Style.RESET_ALL)
        else:
          if attempt > 0 and userGuess != wordOfTheDay:
              print('You have', attempt, 'attempts left')
      
      printAttemptMessage(attempt,wordOfTheDay)
      
      if userGuess == wordOfTheDay:
        print('\n', 'Bingo')
        break
     
    
      
      feedback = getUserFeedback(userGuess, wordOfTheDay)
      print(feedback)
  
    else:
      print('Oops! Your word is not valid. Try again!')
  
  return ' '

def doesUserWantToPlayAgain():
  x=str(input('Do you want to play again? (yes/no?)'))
  #print(x)
  if x=='yes':
     playGame()
  else:
    return 'Bye! See you soon.'
  return ''  
  
 
main()
print(playGame())
print(doesUserWantToPlayAgain())
