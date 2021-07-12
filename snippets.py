import bencoder
import aiohttp

torrent_file = open('src/ubuntu.torrent', 'rb')
file_decoded = bencoder.decode(torrent_file.read())
print(file_decoded)

url = file_decoded[b'announce']
print(url)


def foo():
    def baz():
        print('lol')

foo()