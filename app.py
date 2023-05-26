from flask import Flask
app = Flask(__name)

@app.route("/") # end point /

if __name__ == "__main__":
  app.run(debug=True)
