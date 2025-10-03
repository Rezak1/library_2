book_list = {}

class Library:
    def __init__(self, title = '', author= ''):
        self.title = title
        self.author = author
    
    def add_book(self):
        # self.title = title
        # self.author = author        
        ##book_list.append(self.title)
        book_list[self.title] = self.author
        #book_list.append(self.auther)
        return book_list
    
    def remove_book(self):
        if self.title in book_list: 
            book_list.pop(self.title)
            return f"{self.title} was removed from the library"
        else:
            return f"{self.title} dosen't exist"
        
    def search_book(self):
        if self.title in book_list: 
            return True
        
    def show_books(self):
            return book_list, len(book_list)
            
