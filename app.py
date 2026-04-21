from flask improt Flask

app =Flask(__name__)

@app.route('/')

def home():
    return "<h1>Devops succeessfull</h1><p>Python +docker+git+aws running</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)