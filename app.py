from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hi Sean! This TEST has been a success!'

if __name__== "__main__":
  app.run()
