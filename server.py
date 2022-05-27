from flask import Flask

app = Flask('funguycollective')

@app.route("/", methods=['GET'])
def home():
    return "This is the home page"

#create an about endpoint and show your name
@app.route("/about")
def about():
     me = {
        "first": "David",
        "last": "Desilvey",
        "age": "29"
    }
    return "me"


app.run(debug=True)