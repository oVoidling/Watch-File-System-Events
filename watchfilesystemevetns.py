import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source ="C:/Users/HP/Desktop"

class FileMovementHandeler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Opps, someone deleted {event.src_path}")
    def on_modified(self, event):
        print(f"Hey, {event.src_path} file has been modified")
    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")

event_handler = FileMovementHandeler()
observer = Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running....")
except KeyboardInterrupt:
    print("Stopped.")
observer.stop()