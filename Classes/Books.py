class Book:
    def __init__(self, title, genre, volumes):
        self.title = title
        self.genre = genre
        self.volumes = volumes

    def get_info(self):
        return f"{self.title} ({self.genre}) - {self.volumes} volumes"

    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_volumes(self):
        return self.volumes
