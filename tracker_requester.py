import ipaddress
import random
import struct

import requests
import string
from torrent_file_reader import *
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
print(tracker_url)
tracker_response = requests.get(tracker_url, params=conn_parameters)  # get request to tracker url
tracker_data = bencoder.decode(tracker_response.content)  # encoding bytes tracker answer to a dict
# print(tracker_data)

interval = tracker_data[b'interval']  # getting interval of tracker url requests (int)
peers_string = tracker_data[b'peers']  # getting number of available peers (bytes)

peers_addresses = []  # initializing peers ip:port array
for i in range(0, len(peers_string), 6):  # parsing ip:port from peers_string bytes string
    peer_ip_bytes, peer_port_bytes = (
        peers_string[i:i + 4], peers_string[i + 4:i + 6]
    )
    peer_ip = str(ipaddress.IPv4Address(peer_ip_bytes))  # convert peer ip to human-readable
    peer_port = struct.unpack('>H', peer_port_bytes)[0]  # convert peer port to human-readable
    peers_addresses.append([peer_ip, peer_port])  # push ip:port to peers array

print(peers_addresses)

# socket.gethostbyname(socket.gethostname())
