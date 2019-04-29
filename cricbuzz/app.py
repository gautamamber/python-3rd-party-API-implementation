from pycricbuzz import Cricbuzz
c = Cricbuzz()

def matches():
	matches = c.matches()
	print(matches)

matches()