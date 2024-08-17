import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
secret_words_list = list(get_secret_words())
from valid_wordle_guesses import get_valid_wordle_guesses
valid_wordle_guesses_list=list(get_valid_wordle_guesses())

full_guesses=[]
feedback_gs=[]
reg_gs=[]
valid_words=set(valid_wordle_guesses_list)
goal= random.choice(list(get_secret_words()))
def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word

        Returns:
            str: Feedback string, based on comparing guess with the secret word
    
        Examples
        >>> get_feedback("lever", "EATEN")
        "-e-E-"
            
        >>> get_feedback("LEVER", "LOWER")
                "L--ER"
            
        >>> get_feedback("MOMMY", "MADAM")
                "M-m--"
            
        >>> get_feedback("ARGUE", "MOTTO")
                "-----"
    '''
    output="-----"
    o_list=list(output)
    g_list=list(guess.lower())
    sw_list=list(secret_word.lower())
    
    for i in range(len(g_list)):
        if g_list[i]==sw_list[i]:
            o_list[i]= g_list[i].upper()
            sw_list[i]="*"
            #Logic error right here below
            if g_list[i] in sw_list:
                g_list[i]="$"
    for i in range(len(g_list)):
        if g_list[i] in sw_list:
            o_list[i]=g_list[i].lower()
            for j in range(len(sw_list)):
                if sw_list[j]==g_list[i]:
                    sw_list[j] = "*"
                    break     
         
    letter = ''.join(o_list)
    feedback_gs.append(letter)
    return letter


def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    """#1st iteration
    return random.choice(list(valid_words))"""
    global valid_words
    a=reg_gs[len(reg_gs)-1]
    #2nd iteration
    for i in range(5):
        to_remove=set()
        if feedback_gs[-1][i]=="-":
            char=a[i].upper()
            print(char)
            
            for word in valid_words:
                if char in word:
                    to_remove.add(word)
        
        #print(len(valid_words)-len(to_remove))                 
        valid_words-=to_remove
    print(valid_words)
            
    return random.choice(list(valid_words))
    """global goal
    to_remove=set()
    for word in valid_words:
        if get_feedback(word,goal)!=feedback_gs[len(feedback_gs)-1]:
            to_remove.add(word)
        valid_words=valid_words-to_remove

    return random.choice(list(valid_words))"""


# TODO: Define and implement your own functions!
def colored_version (feedbackstr: str, guess:str):
    guess=guess.upper()
    reg_gs.append(guess.lower())
    everything=list(guess.upper())
    for i in range(len(feedbackstr)):
        if feedbackstr[i]=="-":
            everything[i]= Back.BLACK+ Fore.WHITE + guess[i]
        elif feedbackstr[i].isupper():
            b = Back.GREEN + Fore.WHITE+ guess[i]
            everything[i]= b
        elif feedbackstr[i].islower():
            c= Back.YELLOW + Fore.WHITE+ guess[i]
            everything[i]=c
    back_full_line= Back.WHITE+ "       "
    back_space= Back.WHITE+ " "
    complete = "".join(everything)
    full_guesses.append(complete)
    print(back_full_line)
    for i in range(len(full_guesses)):
        print(back_space+full_guesses[i]+back_space)
    print(back_full_line)
    return complete


def play_wordle_game():
    #print(get_secret_words())
    global goal
    print(goal)
    first_word = "slate"
    colored_version(get_feedback(first_word,goal),first_word)

    for i in range(5):
        guess= get_AI_guess(full_guesses,feedback_gs,(),())
        colored_version(get_feedback(guess,goal),guess)
        if feedback_gs[len(feedback_gs)-1]==goal:
            print("You won!!")
            break
    

if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    """m=get_feedback("mommy", "MADAM")
    print(m)
    colored_version(m, "mommy")"""
    play_wordle_game()
    pass
