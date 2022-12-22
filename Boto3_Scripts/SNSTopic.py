import logging
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-1'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sns_client = boto3.client('sns', region_name=AWS_REGION)


def create_topic(name):
    """
    Creates a SNS notification topic.
    """
    try:
        topic = sns_client.create_topic(Name=name)
        logger.info(f'Created the SNS topic {name}.')

    except ClientError:
        logger.exception(f'Unable to create the SNS topic {name}.')
        raise
    else:
        return topic
        
def subscribe(topic, protocol, endpoint):
    """
    Subscribe to a topic using the endpoint as email OR SMS
    """
    try:
        subscription = sns_client.subscribe(
            TopicArn=topic,
            Protocol=protocol,
            Endpoint=endpoint,
            ReturnSubscriptionArn=True)['SubscriptionArn']
    except ClientError:
        logger.exception(
            "Couldn't subscribe {protocol} {endpoint} to topic {topic}.")
        raise
    else:
        return subscription


if __name__ == '__main__':

    topic_name = 'wk-15-sns-topic'
    logger.info(f'Creating the SNS topic {topic_name}...')
    topic = create_topic(topic_name)
    
    topic_arn = 'your-topic-ARN'
    protocol = 'email'
    endpoint = 'your-email'

    logger.info('Subscribing to a SNS topic...')

# Creates an email subscription
    response = subscribe(topic_arn, protocol, endpoint)

    logger.info(
        f'Subscribed to a topic successfully.\nSubscription Arn - {response}')   
