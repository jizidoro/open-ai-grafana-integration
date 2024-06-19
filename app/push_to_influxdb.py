from influxdb import InfluxDBClient
from app.utils import load_config

def push_to_influxdb(data):
    config = load_config()
    client = InfluxDBClient(host=config['influxdb']['host'], port=config['influxdb']['port'])
    client.switch_database(config['influxdb']['database'])

    # Example data point
    data_point = [
        {
            "measurement": "usage",
            "tags": {
                "user": "example_user"
            },
            "fields": {
                "requests": data['requests'],
                "tokens": data['tokens']
            }
        }
    ]
    client.write_points(data_point)