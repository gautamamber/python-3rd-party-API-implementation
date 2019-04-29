from pycricbuzz import Cricbuzz
from flask import Flask, render_template
app = Flask(__name__)
c = Cricbuzz()
@app.route('/')
def index():
	all_matches = []
	matches = c.matches()
	for i in matches:
		all_matches.append(i['srs'] +  " ====> " + i['status'])
	return render_template("index.html", all_matches = all_matches)

if __name__ == '__main__':
   app.run()