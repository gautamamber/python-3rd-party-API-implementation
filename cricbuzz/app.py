from pycricbuzz import Cricbuzz
from flask import Flask, render_template
app = Flask(__name__)
c = Cricbuzz()
@app.route('/')
def index():
	all_matches = []
	matches = c.matches()
	print(c.players_mapping("22482"))
	print("-------------")
	print(c.matchinfo("22482"))
	print("--------")
	print(c.livescore("22482"))
	for i in matches:
		all_matches.append(i['srs'] +  " ====> " + i['status'])
	return render_template("index.html", all_matches = all_matches)

@app.route("/score_card")
def score_card():
	score = c.scorecard("22482")
	scorecard = score['scorecard']
	for i in scorecard:
		print(type(i))
		print("Innings: ", i['inng_num'] )
		print("Batteam is:", i['batteam'])
		print("Bowlteam is:", i['bowlteam'])
		print("Score is: ", i['runs'])
		print("Wickets is:", i["wickets"])
		bat = i['batcard']
		for j in bat:
			print("name is: ", j['name'] + "      " + "Score is: ", j['runs'] + "        "  +  "Fours: ", j['fours'] + "        "  +  "Six: ", j['six'] + "         " +   "dismissal: " , j['dismissal'])
		print("------")
		bowl = ""

	return render_template("live_score.html", i = i)

if __name__ == '__main__':
   app.run()