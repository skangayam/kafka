import json
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
import config


CONFIG = config.get_config()
hashTags = list()
hashTags.append('apple')
hashTags.append('samsung')
data = {"hashTags":hashTags, "content":"a random text string"}
client = KafkaClient(CONFIG['brokerHosts'])
producer = SimpleProducer(client)
producer.send_messages(CONFIG['topicName'], json.dumps(data))