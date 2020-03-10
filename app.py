from flask import Flask, jsonify

app = Flask(__name__)

a = {'a':'coba flask', 'b':'coba mongodb', 'c':'coba reatapi'}


@app.route('/')
def tes():
    return jsonify(a)


if __name__ == '__main__':
    app.run(debug=True)
