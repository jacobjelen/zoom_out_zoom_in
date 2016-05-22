from flask import Flask
from src.map import Map
app = Flask(__name__)

@app.route("/")
def zoom_in_zoom_out():
	Map().run()
	return "ok"

if __name__ == "__main__":
    app.run(debug=True)