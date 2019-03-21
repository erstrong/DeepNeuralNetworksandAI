import pandas as pd
from src.services import ibm_watson
from src.services import google_sentiment
from src.services import azure_cognitive_service
from src.services import amazon_comprehend


def fetch_result_from_services():
    input_dataset = pd.read_csv('cleaned_merged_data.csv')

    sliced_dataset = input_dataset
    sliced_dataset = sliced_dataset.rename(columns={'Sentiment': 'ActualLabel'})

    sliced_dataset['IbmScore'] = sliced_dataset.apply(lambda x: ibm_watson.get_sentiment_score(x['Text']), axis=1)
    sliced_dataset['IbmLabel'] = sliced_dataset.apply(lambda x: ibm_watson.get_sentiment_lable(x['IbmScore']), axis=1)

    sliced_dataset['GCPScore'] = sliced_dataset.apply(lambda x: google_sentiment.get_sentiment_score(x['Text']), axis=1)
    sliced_dataset['GCPLabel'] = sliced_dataset.apply(lambda x: google_sentiment.get_sentiment_lable(x['GCPScore']),
                                                      axis=1)

    sliced_dataset['AzureScore'] = sliced_dataset.apply(
        lambda x: azure_cognitive_service.get_sentiment_score(x['Text']), axis=1)
    sliced_dataset['AzureLabel'] = sliced_dataset.apply(
        lambda x: azure_cognitive_service.get_sentiment_lable(x['AzureScore']), axis=1)

    sliced_dataset['AWSScoreLabel'] = sliced_dataset.apply(
        lambda x: amazon_comprehend.get_sentiment_score_label(x['Text']), axis=1)

    sliced_dataset.to_csv('output.csv', index=None)


def get_aws_part(input, inde):
    input = input.replace("(", "").replace(")", "").replace("'", "").split(",")[inde].strip()
    return input


def fix_aws_column():
    df = pd.read_csv('output.csv')
    df['AWSLabel'] = df.apply(lambda x: get_aws_part(x['AWSScoreLabel'], 3), axis=1)
    df['AWSPosScore'] = df.apply(lambda x: get_aws_part(x['AWSScoreLabel'], 0), axis=1)
    df['AWSNegScore'] = df.apply(lambda x: get_aws_part(x['AWSScoreLabel'], 1), axis=1)
    df['AWSNeuScore'] = df.apply(lambda x: get_aws_part(x['AWSScoreLabel'], 2), axis=1)
    del df['AWSScoreLabel']
    df.to_csv("output_for.csv", index=None)


if __name__ == "__main__":
    fetch_result_from_services()
    fix_aws_column()
