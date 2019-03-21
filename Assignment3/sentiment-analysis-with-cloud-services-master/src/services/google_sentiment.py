import os
import six
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from src.configuration.Configuration import Configuration


# -1(negative) to 1(positive)
def get_sentiment_score(content):
    conf = Configuration()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = conf.get_gcp_file_path()

    client = language_v1.LanguageServiceClient()
    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    try:
        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment
    except Exception as error:
        print(error)
        return None
    # print('Score: {}'.format(sentiment.score))
    return sentiment.score


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
