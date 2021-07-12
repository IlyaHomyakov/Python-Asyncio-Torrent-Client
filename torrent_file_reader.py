import bencoder
import hashlib

"""This module opens a torrent file and parses information from it"""

torrent_file = open('src/ubuntu.torrent', 'rb')  # opening file in read-bytes mode
file_decoded = bencoder.decode(torrent_file.read())  # decoding bytes file to a dict
# print(file_decoded)

tracker_url = file_decoded[b'announce'].decode('utf-8')  # parsing tracker url
name = file_decoded[b'info'][b'name'].decode('utf-8')  # parsing name of the downloading file
size = file_decoded[b'info'][b'length']  # parsing size of downloading file in bytes
size_megabytes = size / 1024 ** 2  # size of downloading file in MB
# print(tracker_url, name, size)

info_hash = hashlib.sha1(  # creating hash from info dict of torrent file
    bencoder.encode(file_decoded[b'info'])
).digest()
