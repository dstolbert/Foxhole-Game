class FoxholeGame():

	def __init__(self):

		# Class initilization method

		self.counter = 0
		self.inputs = []

	def check_hole(self, holes):

		print(f'The fox could be in holes {holes}')

		try:
			checked_hole = int(input('Select a hole to check: '))
		except:
			print('Eror: Not an available hole')
			self.check_hole(holes)

		# Track input and increment counter
		self.inputs.append(checked_hole)
		self.counter += 1

		if checked_hole in holes:

			# Drop the selected hole from the holes list
			holes.remove(checked_hole)
			
			# Calculate the possible holes for the next day
			holes = self.next_day(holes)
			holes.sort()

			# Repeat until no holes remain
			if len(holes) > 0:
				self.check_hole(holes)
			else:
				self.win()

		else:
			print(f'{checked_hole} is not one of the available holes. Please try again.')
			self.check_hole(holes)

	def next_day(self, holes):

		tmp = []

		for hole in holes:
			if (hole-1) > 0:
				tmp.append(hole-1)

			if (hole+1) <= self.n_holes:
				tmp.append(hole+1)

		return list(set(tmp))

	def win(self):
		print(f'Congratulations!! You solved the game in {self.counter} rounds')
		print(f'Here are the holes you checked: {self.inputs}')

	def play(self):
		# Get user input for the number of days selected
		
		try:
			self.n_holes = int(input('Select the number of holes to play with: '))
			self.check_hole(list(range(1, self.n_holes+1)))
		except:
			print('Error: Please enter a positive integer value')
			self.play()


game = FoxholeGame()
game.play()
