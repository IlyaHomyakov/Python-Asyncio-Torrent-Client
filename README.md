Last issue: During handshake in asyncio loop nothing is returned from peers, then catching TimeoutError:
[Errno 60] Operation timed out.

Problem occurs in peers_requester module

Main modules now are _torrent_file_reader.py_, _tracker_requester.py_ and _peers_requester.py_.
They can be run separately, but keep in mind that one module may use variables from another.

_torrent files are in **torrent** folder_
