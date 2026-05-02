#!/usr/bin/env python3
"""
Background file watcher: automatically sync .md files to Notion on save.
Run once in a terminal: python3 watch_and_sync.py

Press Ctrl+C to stop.
"""

import sys
import os
import time
import subprocess

WORKSPACE = "/Users/naokinishimura/Desktop/整形外科雑誌/hello-world"
SYNC_SCRIPT = os.path.join(WORKSPACE, ".cursor", "sync_to_notion.py")

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("watchdog not found. Install with: pip3 install watchdog --user")
    sys.exit(1)


class MarkdownSyncHandler(FileSystemEventHandler):
    def __init__(self):
        self._last_synced = {}

    def on_modified(self, event):
        if event.is_directory:
            return
        path = event.src_path
        if not path.endswith(".md"):
            return
        # Debounce: skip if same file was synced within 2 seconds
        now = time.time()
        if now - self._last_synced.get(path, 0) < 2.0:
            return
        self._last_synced[path] = now
        print(f"[watcher] Changed: {os.path.relpath(path, WORKSPACE)}")
        subprocess.Popen(
            [sys.executable, SYNC_SCRIPT, path],
            stdout=open(os.path.join(WORKSPACE, ".cursor", "notion-sync.log"), "a"),
            stderr=subprocess.STDOUT,
        )

    on_created = on_modified


if __name__ == "__main__":
    handler = MarkdownSyncHandler()
    observer = Observer()
    observer.schedule(handler, WORKSPACE, recursive=True)
    observer.start()
    print(f"[watcher] Watching {WORKSPACE} for .md changes → Notion sync")
    print("[watcher] Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
