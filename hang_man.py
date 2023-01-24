from typing import List, Optional


class HangMan:

	def __init__(self, num_words: Optional[int] = -1):
		pass

	def get_phrase(self) -> str:
		pass

	def find_idx_of(self, phrase, letter) -> List[str]:
		pass

	def draw_man(self):
		pass

	def give_hint(self):
		print("no")
		pass

	def guess_phrase(self, guess: str) -> bool:
		pass

	def add_to_graveyard(self, letter):
		pass

	def win(self):
		pass

if __name__ == '__main__':
	man = HangMan()
	man.give_hint()
	
