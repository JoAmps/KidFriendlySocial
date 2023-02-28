from inference import inference
import time


def test_good_language_classification():
    sample_text = """This man has been doing wonderful\
        things for his community, big ups to him for that"""
    expected_output = """Tweet contains good/normal language,\
                 go ahead to tweet this"""
    expected_output = expected_output.replace('  ', '')
    # Actual outputs
    actual_output = inference(sample_text)
    # Assert statement
    assert actual_output == expected_output


def test_bad_language_classification():
    sample_text = """All you cunts that think you are tougher than me,\
             should think twice you dumb fucks"""
    expected_output = """Tweet contains bad language, \
                generating recommendations to improve this tweet.."""
    expected_output = expected_output.replace('  ', '')
    # Actual outputs
    actual_output = inference(sample_text)[0]
    # Assert statement
    assert actual_output == expected_output


def test_number_of_recommendations():
    sample_text = """All you cunts that think you are tougher than me,\
             should think twice you dumb fucks"""
    # Actual outputs
    actual_output = inference(sample_text)[1]
    # Assert statements
    assert len(actual_output) == 3


def test_quality_of_recommendations():
    sample_text = """All you cunts that think you are tougher than me,\
             should think twice you dumb fucks"""
    time.sleep(1)
    # Actual outputs
    list_actual_output = inference(sample_text)[1]

    recommended_outputs = []
    for i in list_actual_output:
        recommended_outputs.append(inference(i))

    expected_output = """Tweet contains good/normal language,\
                 go ahead to tweet this"""
    expected_output = expected_output.replace('  ', '')
    # Assert statements
    assert expected_output == recommended_outputs[0]
    assert expected_output == recommended_outputs[1]
    assert expected_output == recommended_outputs[2]
