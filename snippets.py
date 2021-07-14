import socket

import bencoder
import aiohttp
from tracker_requester import peers_addresses

torrent_file = open('torrents/ubuntu.torrent', 'rb')
file_decoded = bencoder.decode(torrent_file.read())
# print(file_decoded)

url = file_decoded[b'announce']
# print(url)

req = b'\x13'
req += b'BitTorrent protocol'

# The optional bits, note that normally some of these are set by most clients
req += b'\x00\x00\x00\x00\x00\x00\x00\x00'
# The Infohash we're interested in.  Let python convert the human readable
# version to a byte array just to make it easier to read
req += bytearray.fromhex("5fff0e1c8ac414860310bcc1cb76ac28e960efbe")
# Our client ID.  Just a random blob of bytes, note that most clients
# use the first bytes of this to mark which client they are
req += bytearray.fromhex("5b76c604def8aa17e0b0304cf9ac9caab516c692")

print(req)


