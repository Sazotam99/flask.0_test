from flask import Flask, render_template, request;

app= Flask(__name__);
SPORTS=[
    "Basketball",
    "Football",
    "Cricket"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS);

@app.route("/greet", methods=["POST"])
def greet():
    name=request.form.get("name");
    sports=request.form.get("sport")
    if sports in SPORTS:
        return render_template("greet.html", name=name, status="registered");
    else:
        return render_template("greet.html", name=name, status="not registered")