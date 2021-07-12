Main files now are _torrent_file_reader.py_ and _tracker_requester.py_
They can be run separately, but keep in mind that tracker_requester uses variables from torrent_file_reader.

Last issue occurs in tracker_requester module when we try to convert bytes string to utf-8 or another instance like dict
(e.g. lines 6, 7 in torrent_file_reader.py).

`print(peers.decode(b'utf-8'))`

`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbd in position 0: invalid start byte`
