import time
import logging
from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler
from plyer import notification

logging.basicConfig(
    filename="folder_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",  
    datefmt="%y-%m-%d %H:%M:%S")

def notify(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=5)
    

class RealTimeFolderMonitor(FileSystemEventHandler):
    def on_created(self,event):
        msg=f"File Created:{event.src_path}"
        print(msg)
        logging.info(msg)
        notify("File Created",event.src_path)
    def on_deleted(self,event):
        msg=f"File Deleted:{event.src_path}"
        print(msg)
        logging.info(msg)
        notify("File Deleted",event.src_path)
    def on_modified(self,event):
        msg=f"File Modified:{event.src_path}"
        print(msg)
        logging.info(msg)
        notify("File Modified",event.src_path)   
    def on_moved(self,event):
        msg=f"File Moved:{event.src_path}"
        print(msg)
        logging.info(msg)
        notify("File Moved",event.src_path)
        
Folder_path=input("Enter Folder Path").strip()


if __name__ == "__main__":
    print(f"Monitoring Started on {Folder_path}")
    event_handler=RealTimeFolderMonitor()
    observer=Observer()
    observer.schedule(event_handler, Folder_path,recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop() 
        print("Monitoring stopped.")
    
    observer.join()        


        

