from flask import Flask, render_template

app = Flask(__name__)

# ===== ROUTES =====
@app.route('/')
def home():
    name = "Mekan Chashemow"
    return render_template('home.html', name=name)

@app.route('/about')
def about():
    bio = "I am a teenage developer interested in Python, Flask, and web development."
    return render_template('about.html', bio=bio)

@app.route('/hobbies')
def hobbies():
    hobbies_list = ["Programming", "Reading", "Playing games", "Learning languages"]
    return render_template('hobbies.html', hobbies=hobbies_list)

if __name__ == '__main__':
    app.run(debug=True)
