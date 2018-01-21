*Emil Milanov, Boyan Hristov*

# Clean Room Development

## Spezification

Game class

1. Method -> Game start; User selects game mode
1. Method -> Game end;

  * Preconditions: None

### Verifying inputs and setting game states
1. Methode -> Code Make
	- create code
	- verify guess and create hint
	- change turn
1. Method -> Code Break
	- guess code
	- depending on result, improve hope
	- change turn

### AI Methods
1. handleGuess()
1. tryBreak()


1. Method -> User gives input
	- depending on mode, codeMake() or codeBreak()
1. Method -> AI gives input
	- same as above

1. Method (callback) request input from player depending on turn

1. Auto 

## 1. Blackbox
```
Game::init()
Game::start()
```

## 1. Whitebox
```python
game = Game()
self.start()
```

## 2. Blackbox

* Game::start 
  * Preconditions: game not started
  * Postcondition: game winner is known; game is over
## 2. Whitebox
```python
class Game:
	def start(self):
		
		game_mode = self.get_game_mode()

		if gamemode == 0:
			self.code_break()
		else:
			self.code_make()
```

## 3. Blackbox
* Game::code_make
  * Preconditions: 
   	* The user choose to be the code breaker
  	* Code is not known
  * Postconditions:
  	* user broke the code OR
  	* game is quit

## 3. Whitebox

```python
def code_make(self):
	code = self.generate_code()
	game_over = False

	while not game_over:
		guess = self.player_guess()
		
		if guess is None:
			print('Sorry motori, you lose!')
			return
		
		game_over = self.compare(guess, code)

	print('gg ez')

```

## 4. Blackbox
* Game::generate_code
  * Pre: 
    * no code
  * Post:
  	* code with:
  	  * 4 chars length, each char symbolizing a color and being a number from 1 to 6
  	  * no duplicates

## 4. Whitebox

```Python
from random import randint

def generate_code(self):
	
	colors = [1,2,3,4,5,6]
	code = []

	while len(code) < 4:
		rnd_idx = randint(0, len(colors))
		code.append(colors[rnd_idx])
		colors.remove(colors[rnd_idx])

	return code
```

## 5. Blackbox
* Game::player_guess()
  * Preconditions
    * Code is fixed, only programm knows it
  * Postconditions
   	1. Player was given a feedback
   	1. Player is requested to input a guess
   	1. Guess is verified
    * Either
      1. Input is valid (as of given conditions above) OR input is requested again from user
      1. Input from player was received and returned
    * Or
      * Player chooses to quit the game, None is returned

## 5. Whitebox

```Python
def player_guess(self):
	user_input = input('Enter code or q to quit: ')

	if user_input.lower() == 'q':
		return None
	elif self.code_valid(user_input):
		return user_input
	else:
		return self.player_guess()
```

## 6. Blackbox
* Game::code_valid(input)
  * Preconditions
    * User input as string was given
  * Postconditions
    * True if code is valid (as of requirements above)
    * False otherwise

## 6. Whitebox

```Python
def code_valid(self, code):
	allowed = [1,2,3,4,5,6]

  	if len(code) != 4:
  		return False
  	elif len(code) == len(set(code)):
  		return False
  		
  	for c in code:
  		if c not in allowed:
  			return False

  	return True
```

## 7. Blackbox
* Game::compare(guess, code)
  * Pre
    * guess is a valid code
    * code and guess are of equal length and contain only 1 to 6 chars
  * Post:
    * User is given feedback on the code
      * w is placed for each char in code that is both correct and on the right place
      * b is placed for each char in code that is correct but not on the right place
      * . is placed for all wrong characters (non-existant in code)
      * feedback is of length 4, ALWAYS!
    * returns True if guess = code
    * returns False otherwise

## 7. Whitebox

```Python
def compare(self, guess, code):
	w_s = 0
	b_s = 0
	dots = 0
	
	for i in range(len(guess)):
		if guess[i] == code[i]:
			w_s += 1
		elif guess[i] in code:  # because unique chars in code and guess
			b_s += 1
		else:
			dots += 1

	print('Feedback: {}'.format(('w' * w_s) + ('b' * 'b_s') + ('.' * dots)))

	if w_s == 4:
		return True
	
	return False
```

## 8. Blackbox
* Game::get_game_mode
  * Pre
    * nothing
  * Post
    * return 0 for user choose to make the code OR
    * return 1 for user choose to break the code

## 8. Whitebox

```Python
def get_game_mode()
	uinput = input('Select 0 to make a code or 1 to break a code')

	if uinput == '0':
		return 0
	elif uinput == '1':
		return 1

	return self.get_game_mode()
```


## 9. Blackbox

* code_break()
  * Precoditions:
    * The user choose to be the code maker
    * Code is not known
  * Postconditions:
    * If the user cheats, error message is printed and user is requested feedback again
    * If the user feedback is not provided, then the game is quit
    * If the ai guessed the code, game is ended

## 9. Whitebox

```python
def code_break(self):
		game_over = False
		feedback = ''
		print('Make up your mind and select a 4 chars long code with number from 1 to 6 and no duplicates. Write it down somewhere. When feedback is requested from you, you should place' + 
			'one w for each char that was in the right position, b for each char that is in your code but wrong position and for all other chars.')

		while not game_over:
			guess = self.ai_guess(feedback)

			if guess is None:
				print('Common, don\'t change your code in runtime, loser! Give me some feedback again!')

			feedback = self.get_user_feedback(guess)

			if feedback is None:
				print('gtfo loser!')

			game_over = feedback == 'wwww'

		print('gg ez')
```

## 10. Blackbox
* get_user_feedback(self, guess)
  * Preconditions:
    * ai has guessed a code
	* code guess is valid
  * Postconditions:
	* user gives a valid guess (as per description above

## 10. Whitebox
```python
def get_user_feedback(self, guess):
	print("Is this your code: " + guess)
	response = input("Feedback pls: ")

	if self.validate_user_feedback(response):
		print("invalid response")
		self.get_user_feedback(guess)
	
	# format response
	chars = list(response)
	chars.sort(reverse=True)
	return "".join(chars)
	
```

## 11. Blackbox
* validate_user_feedback(self, guess):
  * Preconditions:
	* code is valid
  * Postconditions:
	* returns True if feedback is of length 4 and has proper format

## 11. Whitebox

```python
def validate_user_feedback(self, response):
	allowed = ['w', 'b', '.']

	if len(response) != 4:
		print("Feedback not of length 4")
		return False
	elif len(response) - len(response.replace('.', '') > 2:
		print("No way to have more than 2 points")
		return False

	for c in response:
		if c not in allowed:
			print(str(c) + " is not an allowed character")
			return False
	
	return True
```

## 13. Blackbox
* __init__()
  * Preconditions
    * none
  * Postconditions:
    * Initialized variables needed for ai_guess

## 13. Whitebox

```python
def __init__(self):
	self.pool = self.gen_pool()
	self.unused = self.pool + []
```


## 12. Blackbox
* ai_guess(self, feedback)
  * Preconditions:
    * user feedback is valid
	* user feedback is not 'wwww'
  * Postconditions:
    * returns a new valid guess

## 12. Whitebox
```python
def ai_guess(self, feedback):
	new_guess = self.generate_code()
	return new_guess
```

## 12. Whitebox
```python
def ai_guess(self, feedback):
	self.pool = self.eliminate_from_pool(feedback, self.last_guess)

	if len(self.pool) == 1:
		return self.pool[0]
	elif len(self.pool) == 0:
		return None

	scores  = [self.get_score(x, self.pool) for x in self.unused]
	best_score = scores.argmax()

	result = self.unused[best_score]
	self.unused.remove(result)
	self.pool.remove(result)

	self.last_guess = result
	
	return result
```


