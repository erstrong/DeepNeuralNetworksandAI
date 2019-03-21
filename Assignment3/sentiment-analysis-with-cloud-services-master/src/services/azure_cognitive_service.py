import requests
from src.configuration.Configuration import Configuration


# 0(negative) to 1(positive)
def get_sentiment_score(text):
    conf = Configuration()

    subscription_key = conf.get_azure_subscription_key()
    text_analytics_base_url = 'https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/'
    sentiment_api_url = text_analytics_base_url + "sentiment"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    documents = {'documents': [
      {'id': '1',
       'language': 'en',
       'text': text}
    ]}
    try:
        response = requests.post(sentiment_api_url, headers=headers, json=documents)
        sentiments = response.json()
        score = sentiments['documents'][0]['score']
    except Exception as error:
        print(error)
        return None
    return score


def get_sentiment_lable(score):
    if score < 0.35:
        label = "Negative"
    elif score > 0.65:
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
