import random
import requests
import string
from torrent_file_reader import info_hash, file_decoded, tracker_url
import bencoder
import socket

"""This module requests tracker and receives requests' interval time and peers data"""

peer_id = 'SA' + ''.join(  # generating peer_id parameter to access tracker's url
    random.choice(string.ascii_lowercase + string.digits)
    for i in range(18)
)

conn_parameters = {  # all parameters for accessing tracker's url
    'info_hash': info_hash,
    'peer_id': peer_id,
    'compact': 1,
    'no_peer_id': 0,
    'event': 'started',
    'port': 59696,
    'uploaded': 0,
    'downloaded': 0,
    'left': file_decoded[b'info'][b'length']
}

tracker_response = requests.get(tracker_url, params=conn_parameters)  # get request to tracker url
tracker_data = bencoder.decode(tracker_response.content)  # encoding bytes tracker answer to a dict
# print(tracker_data)

interval = tracker_data[b'interval']  # getting interval of tracker url requests (int)
peers = tracker_data[b'peers']  # getting number of available peers (bytes)


# todo fix this bug
print(peers.decode('utf-8'))



# socket.gethostbyname(socket.gethostname())