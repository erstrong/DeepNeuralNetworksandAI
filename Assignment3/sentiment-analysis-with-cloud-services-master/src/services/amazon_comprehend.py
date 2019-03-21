import boto3

from src.configuration.Configuration import Configuration


def get_sentiment_score_label(text):
    conf = Configuration()
    aws_access_key_id = conf.get_aws_access_key_id()
    aws_secret_access_key = conf.get_aws_secret_access_key()
    region_name = conf.get_aws_region_name()

    comprehend = boto3.client(service_name='comprehend',
                              region_name=region_name,
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

    try:
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    except Exception as error:
        print(error)
        return None

    pos_score = response['SentimentScore']['Positive']
    neg_score = response['SentimentScore']['Negative']
    neu_score = response['SentimentScore']['Neutral']
    mixed_score = response['SentimentScore']['Mixed']

    sentiment = response['Sentiment'].title()
    if sentiment is 'Mixed':
        sentiment = 'Neutral'
        neu_score = mixed_score

    return pos_score, neg_score, neu_score, sentiment


if __name__ == "__main__":
    text = "It is raining today in Seattle"
    result = get_sentiment_score_label(text)
    print(result)
