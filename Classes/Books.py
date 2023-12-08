class Book:
    def __init__(self, title, genre, volumes):
        self.title = title
        self.genre = genre
        self.volumes = volumes

    def get_info(self):
        volumes_str = " ".join(str(volume) for volume in self.volumes)
        return f"{self.title} ({self.genre}) - Volumes: ({volumes_str})"


    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_volumes(self):
        return self.volumes
