import requests
import socket
import log
from tracker_requester import *
from torrent_file_reader import *
import aiohttp
import asyncio

connections_to_peers_loop = asyncio.get_event_loop()  # initializing asyncio loop for handling peers connection

# todo check handshake on correctness
handshake = struct.pack(  # creating data for handshaking a peer
    '>B19s8x20s20s',
    19,
    b'BitTorrent protocol',
    info_hash,
    peer_id.encode()
)
# handshake_str = '>B19s8x20s20s' + (19).encode() +  litter
print(handshake)


async def connect_to_peer(peer_address):  # starting connections to the peer
    try:
        reader, writer = await asyncio.wait_for(  # trying to establish connection
            asyncio.open_connection(peer_address[0], peer_address[1]),
            timeout=10
        )
    except:  # if impossible, skip this connection
        return

# todo fix Operation Timed Out while handshaking peer
    writer.write(handshake)  # handshaking a peer
    await writer.drain()  # buffers the data and arranges for it to be sent out asynchronously.
    # peer_handshake = await reader.read(68)  doing nothing, stops program normal flow
    # print(peer_handshake)
    resp = await reader.read()  # Suspends here if there's nothing to be read, also stops program normal flow

    print(resp)
    # print(writer, reader)


async def downloads():  # for future
    pass


async def start_connections():  # function that starts an asynchronous connection with separate peer
    connections = [asyncio.ensure_future(connect_to_peer(j)) for j in peers_addresses]
    # connections = [asyncio.create_task(connect_to_peer(peers_addresses[0]))]
    await asyncio.wait(connections)
    print('The end')


connections_to_peers_loop.run_until_complete(start_connections())  # run connection routine
