class Game:
	def start(self):
		game_mode = self.get_game_mode()
			
		if game_mode == 0:
			self.code_break()
		else:
			self.code_make()

	# ---------------- USER BREAKS CODE -------------------------------------------------------

	def code_make(self):
		code = self.generate_code()
		game_over = False

		while not game_over:
			guess = self.player_guess()
			game_over = self.compare(guess, code)

		print('gg ez')

	def get_game_mode(self):
		uinput = input('Select 0 to make a code or 1 to break a code')

		if uinput == '0':
			return 0
		elif uinput == '1':
			return 1

		return get_game_mode()

	def generate_code(self):
		colors = [1,2,3,4,5,6]
		code = []

		while len(code) < 4:
			rnd_idx = randint(0, len(colors))
			code.append(colors[rnd_idx])
			colors.remove(colors[rnd_idx])

		return code

	def player_guess(self):
		user_input = input('Enter code or q to quit: ')

		if user_input.lower() == 'q':
			return None
		elif self.code_valid(user_input):
			return user_input
		else:
			return self.player_guess()

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

	# ---------------- USER MAKES CODE -------------------------------------------------------


if __name__ == "__main__":
	Game().start()