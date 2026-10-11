"""Setup or update the French TV channel playlists for NPVR."""

import os
from pathlib import Path

M3U8_FILE = 'french.m3u8'
CHANNEL_DIR = Path('channels')

def generate_playlist_from_channels():
    """Generate the M3U8 playlist from individual channel files."""
    CHANNEL_DIR.mkdir(exist_ok=True)
    with open(M3U8_FILE, 'w', encoding='utf-8') as main_playlist:
        main_playlist.write('#EXTM3U\n')
        for channel_file in CHANNEL_DIR.glob('*.m3u'):
            with open(channel_file, 'r', encoding='utf-8') as f:
                main_playlist.write(f.read())
                main_playlist.write('\n')
    print(f"{M3U8_FILE} has been updated with the latest channels.")

if __name__ == '__main__':
    generate_playlist_from_channels()
