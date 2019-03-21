from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
from src.configuration.Configuration import Configuration


# -1(negative) to 1(positive)
def get_sentiment_score(text):
    conf = Configuration()
    iam_apikey = conf.get_ibm_iam_apikey()
    url = conf.get_ibm_url()
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey=iam_apikey,
        url=url
    )

    try:
        response = natural_language_understanding.analyze(text=text, features=Features(sentiment=SentimentOptions())).get_result()
    except Exception as error:
        print(error)
        return None
    return response['sentiment']['document']['score']


def get_sentiment_lable(score):
    if score < -0.3:
        label = "Negative"
    elif score > 0.3:
        label = "Positive"
    else:
        label = "Neutral"
    return label


if __name__ == "__main__":
    text = "It is raining today in Seattle"
    score = get_sentiment_score(text)
    label = get_sentiment_lable(score)
    print(score)
    print(label)
