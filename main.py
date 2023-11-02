import grpc
import json
import feed_pb2
import feed_pb2_grpc
from google.protobuf.json_format import MessageToJson

GRPC_URL = 'data-feed.flightradar24.com'
METADATA = (
	('fr24-device-id', 'web-fl24'),
)

# data-feed.flightradar24.com SSL certificate
# need to be replaced on Sunday, July 14, 2024 at 15:27:10
CREDENTIALS = grpc.ssl_channel_credentials(open('cert.pem', 'rb').read()) 

channel = grpc.secure_channel(GRPC_URL, CREDENTIALS)
stub = feed_pb2_grpc.FeedStub(channel)

def LiveFeed(data):
	request = feed_pb2.LiveFeedRequest(**data)
	response = stub.LiveFeed(
		request = request, 
		metadata = METADATA
	)
	response = json.loads(MessageToJson(response))

	for flight in response['flights']:
		response['flights'][response['flights'].index(flight)]['flightId'] = hex(flight['flightId'])[2:]

	return response['flights']

data = {
	'bounds': {
		"north": 180,
		"south": -85,
		"west": 180,
		"east": 85
	},
	'settings': {
		"sources": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
		"services": [2],
		"traffic_type": "ALL"
	},
	'stats': False,
	'limit': 1500,
	'maxage': 14400
}
print(LiveFeed(data))