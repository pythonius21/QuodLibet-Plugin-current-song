# -*- coding: utf-8 -*-
"""Writes the current playing song to a text file (for OBS overlays etc)."""

from gi.repository import GObject
from quodlibet.plugins.events import EventPlugin
from quodlibet import app
import os

class NowPlayingToFile(EventPlugin):
    PLUGIN_ID = "Now Playing To File"
    PLUGIN_NAME = "Now Playing To File"
    PLUGIN_DESC = "Writes the current played song in a text file."
    PLUGIN_VERSION = "1.0"

    OUTPUT_FILE = os.path.expanduser("~/Music/current_song.txt")

    def plugin_on_song_started(self, song):
        """Called when a song starts playing"""
        try:
            artist = song("artist") or "Unknown artist"
            title = song("title") or "Unknown title"
            text = f"{artist} - {title}"
            with open(self.OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"[NowPlayingToFile] {text}")
        except Exception as e:
            print(f"[NowPlayingToFile] Error writing to: {e}")

    def plugin_on_song_ended(self, song, skipped):
        """Optional: clears file when song stops"""
        try:
            with open(self.OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write("")
        except Exception:
            pass
