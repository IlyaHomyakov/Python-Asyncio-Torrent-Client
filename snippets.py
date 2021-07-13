import socket

import bencoder
import aiohttp
from tracker_requester import peers_addresses

torrent_file = open('torrents/ubuntu.torrent', 'rb')
file_decoded = bencoder.decode(torrent_file.read())
print(file_decoded)

url = file_decoded[b'announce']
print(url)

answer = socket.connect((peers_addresses[0][0], peers_addresses[0][1]))
print(answer)
