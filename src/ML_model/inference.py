from Generative_model.generate import (
    generate_recommendations,
)
from Predictive_model.predict import (
    predict_language_quality,
    load_model_and_tokenizer,
)
import time


def inference(tweet):
    labels = ["good/normal language", "bad language"]
    bad_language_detection_pipeline = load_model_and_tokenizer(
        "vinai/bertweet-base",
        "Predictive_model/model/trained_models/bad_language_tweets_detector",
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
        return (prediction, recommendations)

    else:
        prediction = f"Tweet contains {labels[0]}, go ahead to tweet this"
        return prediction


if __name__ == "__main__":

    inference("""All you cunts that think you are tougher than me,
             should think twice you dumb fucks""")
