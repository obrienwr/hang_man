from typing import List, Optional


class HangMan:

	def __init__(self, num_words: Optional[int] = -1):
		self._graveyard = []
		self._phrase = ""
		pass

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
		pass

	def draw_man(self):
		pass

	def give_hint(self):
		print("no")
		pass

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
		pass

	def win(self):
		pass

if __name__ == '__main__':
	# Whenever you want to add changes to the repository, type 
	# `git add .` 
	# `git commit -m "some message"`
	# `git push -u origin main`
	man = HangMan()
	man.give_hint()
	
