from flask import request, render_template, redirect, url_for, session, Blueprint
import time
from ML_model.Generative_model.generate import (
    generate_recommendations,
)
from ML_model.Predictive_model.predict import (
    predict_language_quality,
    load_model_and_tokenizer,
)
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv

load_dotenv()
ml_bp = Blueprint('ml_bp', __name__,template_folder='templates',static_folder='static')
#import sys
#sys.path.insert(1, '.')
#from mains import mysql



@ml_bp.route("/inference", methods=["GET", "POST"])
def inference():
    if request.method == 'POST':
        tweet = request.form["tweet"]
        labels = ["good/normal language", "bad language"]
        bad_language_detection_pipeline = load_model_and_tokenizer(
            "vinai/bertweet-base",
            "ML_model/Predictive_model/model/trained_models/bad_language_tweets_detector",
        )
        prompt, prediction = predict_language_quality(
            str(tweet), bad_language_detection_pipeline
        )
        flag = False
        if prediction == "LABEL_0":
            prediction = f"""Tweet contains {labels[1]}, generating \
            recommendations to improve this tweet.."""
            prediction = prediction.replace('  ', '')
            time.sleep(1)
            recommendations = generate_recommendations(f"""Generate three
            modifications to the tweet that have high similarity score to
            the original tweet below in order to remove the bad language in
            it to make it suitable for kids to read.
            The tweet is "{prompt}" Three recommendations: """)
            recommendations = recommendations.split('\n')
            result_class = "bad"
            flag = True
            return render_template('predict.html', tweet=tweet, prediction=prediction,
                                   recommendations=recommendations, result_class=result_class, flag=flag)
        else:
            prediction = f"Tweet contains {labels[0]}, \
            go ahead to tweet this"
            prediction = prediction.replace('  ', '')
            result_class = "good"
            flag = True
            return render_template('predict.html', tweet=tweet, prediction=prediction, result_class=result_class, flag=flag)
    else:
        return render_template('predict.html')
    

