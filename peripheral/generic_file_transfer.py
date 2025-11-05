
class IO:

    def __init__(self):
        self.index = "1"
        self.notification_type = 4
        self.local_path = "/home/"


class GenericFileTransfer:
    def __init__(self, index, file_path):

        self.host = "192.168.0.7",
        self.port = 21,
        self.user = "anonymous",
        self.password = "",
        self.passive = true,
        self.timeout = 30,
        self.protocol = "ftp",
        self.local_path = "/home/"

        self.ios:list = [IO()]

    def upload(self, destination):
        # Placeholder for upload logic
        print(f"Uploading {self.file_path} to {destination}...")

    def download(self, source):
        # Placeholder for download logic
        print(f"Downloading from {source} to {self.file_path}...")

    def delete(self):
        # Placeholder for delete logic
        print(f"Deleting file at {self.file_path}...")