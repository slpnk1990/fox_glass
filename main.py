from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    myfile = open("templates/index.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page



if __name__ == "__main__":
    app.run()