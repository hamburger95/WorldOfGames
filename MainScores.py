from Utils import SCORES_FILE_NAME
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')


def score_server():
    try:
        with open(f"{SCORES_FILE_NAME}") as f:
            current_score = f.read()
            return render_template('Scores_Game.html', SCORE=current_score)
    except IOError:
        with open("Scores.txt", "wt") as out_file:
            return render_template('Score_error.html')

    finally:
        f.close()
