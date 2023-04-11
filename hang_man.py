from typing import List, Optional
import random


class HangMan:

	def __init__(self, num_words: Optional[int] = -1, attempts: Optional[int] = 7):
		self._attempts_left = attempts
		self._graveyard = []
		self._phrase = HangMan.build_phrase()
		self._hints_left = 3
		self._found_letters = [' ', '\n']
		self._unfound_letters = list(set(self._phrase))
		if ' ' in self._unfound_letters:
			del self._unfound_letters[self._unfound_letters.index(' ')] 
		if '\n' in self._unfound_letters:
			del self._unfound_letters[self._unfound_letters.index('\n')]

	def fail_attempt(self):
		self._attempts_left -= 1

	def get_remaining_attempts(self):
		return self._attempts_left

	@staticmethod
	def build_phrase():
		"""
		Pulls from the ``idioms.txt`` file for all the possible idioms and returns a
		random idiom. 
		"""
		# testing purposes,,,,
		idioms = []
		with open('idioms.txt', 'r') as idioms_file:
			idioms = idioms_file.readlines()
		return random.choice(idioms)

	def get_phrase(self) -> str:
		return self._phrase

	def get_phrase_underscore(self) -> str:
		underscore_phrase = ""
		for i, letter in enumerate(self._phrase):
			underscore_phrase += (letter if letter in self._found_letters else '_') + " "
		return underscore_phrase

	def find_idx_of(self, letter: str) -> List[int]:
		"""
		Given a phrase and the guessed letter, return a list of integers showing the 
		indices of each time that letter appears in the phrase. If the letter does 
		not occur in the phrase, then an empty list is returned, and the letter is 
		added to the graveyard. 		
		
		Args:
			letter (str): the guessed letter.
		Returns:
			List[int]: List of indices of each place where letter occurs in the 
			  phrase
		"""
		letter = letter.lower().strip()
		if letter in self._found_letters:
			return []
		placement = [i for i, let in enumerate(self._phrase) if let == letter]
		if len(placement) > 0:
			self.add_to_found_letters(letter)
		return placement

	def draw_self(self):
		pass

	def give_hint(self):
		"""
		Gives one letter present at some point in the phrase that has not been found
		by the player and subtracts one from the total number of hints left. 
		"""
		if self._hints_left > 0:
			self._hints_left -= 1
			return random.choice(self._unfound_letters)
		else:
			return ">:("

	def get_hints_left(self):
		return self._hints_left
		
	def add_to_found_letters(self, letter: str):
		if letter in self._unfound_letters:
			del self._unfound_letters[self._unfound_letters.index(letter.lower())]
		self._found_letters.append(letter)

	def guess_phrase(self, guess: str) -> bool:
		"""
		Simple check of whether the guessed phrase matches the actual phrase. 
		
		Args:
			guess (str): Guessed phrase by the user.
		Returns:
			bool: whether the two phrases match.
		"""
		if guess.lower().strip() == self._phrase.lower().strip():
			for letter in self._unfound_letters:
				self._found_letters.append(letter)
			self._unfound_letters = []
			return True
		# self.add_to_graveyard(guess.lower().strip())
		return False

	def add_to_graveyard(self, letter):
		"""
		Appends the supplied letter to the graveyard.

		Args: 
			Letter (str): The letter to add to the graveyard.
		"""
		self._graveyard.append(letter)

	def get_graveyard(self):
		"""
		Returns self._graveyard.
		"""
		return self._graveyard
	def command_line_game(self):
		word_guessed = False
		print('Welcome to Hang Man! Continue to guess letters until you want to guess the idiom!'
			  '\nRemember: respond "GUESS" to attempt to guess the whole phrase!')
		turn = 0
		while not word_guessed and self._attempts_left > 0:
			turn += 1
			print(self.get_phrase_underscore())
			print(f'Graveyard: {self.get_graveyard()}')
			letter = input('Guess Letter: ')
			if letter == "GUESS":
				phrase = input('Sounds good, now guess the Phrase! ')
				word_guessed = self.guess_phrase(phrase)
			else:
				self.find_idx_of(letter)
				word_guessed = self.win()

		print(f'{turn} turns elapsed.')
		print(f'\n{self.get_phrase()}Won!' if word_guessed else f'lost : ( \n{self.get_phrase()}')

	def win(self):
		if len(self._unfound_letters) == 0:
			return True
		return False

if __name__ == '__main__':
	# Whenever you want to add changes to the repository, type 
	# `git add .` 
	# `git commit -m "some message"`
	# `git push -u origin main`
	man = HangMan()
	man.command_line_game()




