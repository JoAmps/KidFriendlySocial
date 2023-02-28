from Generative_model.generate import (
    generate_recommendations,
)
from Predictive_model.predict import (
    predict_language_quality,
    load_model_and_tokenizer,
)
from flask import Flask, request
import warnings
import time

warnings.filterwarnings("ignore")


app = Flask(__name__)


@app.route("/")
def hello():
    return """Welcome to AI enhancing language of tweets
            for young audiences"""


@app.route("/inference", methods=["POST"])
def inference():
    tweet = request.args.get("text")
    labels = ["good/normal language", "bad language"]
    bad_language_detection_pipeline = load_model_and_tokenizer(
        "vinai/bertweet-base",
        "ML_model/Predictive_model/model/trained_models/bad_language_tweets_detector",
    )
    prompt, prediction = predict_language_quality(
        str(tweet), bad_language_detection_pipeline
    )

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
        return {"prediction": prediction,
                "recommendations": recommendations
                }

    else:
        prediction = f"Tweet contains {labels[0]}, \
        go ahead to tweet this"
        prediction = prediction.replace('  ', '')
        return {
            "prediction": prediction
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
