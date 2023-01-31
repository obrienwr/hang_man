from typing import List, Optional
import random


class HangMan:

	def __init__(self, num_words: Optional[int] = -1):
		self._graveyard = []
		self._phrase = HangMan.build_phrase()
		self._hints_left = 3
		self._found_letters = []
		self._unfound_letters = list(set(self._phrase))
		if ' ' in self._unfound_letters:
			del self._unfound_letters[self._unfound_letters.index(' ')] 
		if '\n' in self._unfound_letters:
			del self._unfound_letters[self._unfound_letters.index('\n')]

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
		placement = [i for i, let in enumerate(self._phrase) if let == letter]
		if len(placement) > 0:
			self.add_to_found_letters(letter)
		else:
			self.add_to_graveyard(letter)
		return placement

	def draw_man(self):
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
			
		
	def add_to_found_letters(self, letter: str):
		del self._unfound_letters[self._unfound_letters.index(letter.lower())]
		self._found_letters.append(letter)

	def guess_phrase(self, guess: str) -> bool:
		"""
		Simple check of whether the guessed phrase matches the actual phrase. 
		
		Args:
			guess (str): Guessed phrase by the user.
		Returns:
			bool: whether or not the two phrases match.
		"""
		pass

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

	def win(self):
		pass

if __name__ == '__main__':
	# Whenever you want to add changes to the repository, type 
	# `git add .` 
	# `git commit -m "some message"`
	# `git push -u origin main`
	man = HangMan()
	print(man.get_phrase())
	print(man._found_letters)
	print(man._unfound_letters)
	print(man.give_hint())
	print(man.find_idx_of('h'))
	print(man.get_graveyard())
	print(man._found_letters)
	print(man._unfound_letters)
	print(man.give_hint())

