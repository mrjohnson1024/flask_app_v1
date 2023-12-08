from flask import Flask, render_template

app = Flask(__name__)

LIST = [{
    'id': 1,
    'name': "First item",
    'location': "Phoenix, AZ",
    'qty': '47'
}, {
    'id': 2,
    'name': "Second item",
    'location': "Atlanta, GA",
    'qty': '6874'
}, {
    'id': 3,
    'name': "Third item",
    'location': "Chicago, IL",
    'qty': '11254'
}]


@app.route("/")
def something():
  return render_template('home.html', items=LIST)


@app.route("/items")
def items():
  return "Here is a new route!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
