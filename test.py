from confluent_kafka import admin
from config import config

if __name__ == "__main__":
    admin = admin.AdminClient(config)
    cluster_metadata = admin.list_topics()
    for topic in iter(cluster_metadata.topics.values()):
        print(f'{topic}')
        for p in iter(topic.partitions.values()):
            print(f'partition:{p.id}, isrs:{p.isrs}')
