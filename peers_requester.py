import requests
import socket
import log
from tracker_requester import *
from torrent_file_reader import *
import aiohttp
import asyncio

connections_to_peers_loop = asyncio.get_event_loop()
handshake = struct.pack(
    '>B19s8x20s20s',
    19,
    b'BitTorrent protocol',
    info_hash,
    peer_id.encode()
)

print(handshake)


async def connect_to_peer(peer_address):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(peer_address[0], peer_address[1]),
            timeout=10
        )

    except:
        return

# todo fix Operation Timed Out while handshaking peer
    writer.write(handshake)
    await writer.drain()
    # peer_handshake = await reader.read(68)
    # print(peer_handshake)
    resp = await reader.read()  # Suspends here if there's nothing to be read

    print(resp)
    # print(writer, reader)


async def downloads():
    pass


async def start_connections():
    connections = [asyncio.ensure_future(connect_to_peer(j)) for j in peers_addresses]
    # connections = [asyncio.create_task(connect_to_peer(peers_addresses[0]))]
    await asyncio.wait(connections)
    print('The end')


connections_to_peers_loop.run_until_complete(start_connections())
