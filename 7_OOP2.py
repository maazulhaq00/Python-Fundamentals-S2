class Book:
    def __init__(self, title, author, rating, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.price = price

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Rating: {self.rating}")
        print(f"Price: {self.price}")


class eBook(Book): #inheritance
    def __init__(self, title, author, rating, price, download_url):
        super().__init__(title, author, rating, price)
        self.download_url = download_url

    def show_details(self): #polymorphism
        super().show_details()
        print(f"Download Url: {self.download_url}")



eb1 = eBook("Learning Python", "Hamza", 4.5, 2467, "https://www.python.org/downloads/windows/")

eb1.show_details()




