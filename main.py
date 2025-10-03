from library import Library 

continue_playing = True
print("Welcome. This is a program to manage a library books.")
print("You can add, remove and search a book.")


while continue_playing:

    print("\nEnter 'a' for add book, 'r' for remove book, 's' for search a book and 'all' to dispaly all the books")
    print("a/r/s/all? ")
    
    request = input()
    
    if request.lower() == 'a':
        print('adding a new book')
        print("Insert 'title' and 'auther' (using ',' to separate inputs) ")
        
        input_str = input() 
        title, auther = input_str.split(',')
        book = Library(title, auther)
        book.add_book()
        print(f"'{title}' was added successfully")


    elif request.lower() == 'r':
        print("removing a book")
        print("Enter title of a book to remove from the library") 
        title = input()
        book = Library(title)
        print(book.remove_book())

    
    elif request.lower() == 's':
        print('searching a book')
        print('Insert "title" of the book')    
        title = input() 
        book = Library(title)
        if book.search_book():
            print(f"\n'{title}' exist")
        else:
            print(f"\nSorry, '{title}' dosen't exist")

        
    elif request.lower() == 'all':
        book = Library()
        books, count = book.show_books()
        if count > 0:
            print(f"\nWe have {count} book(s)")
            print("All the book in this library: ")
            print(books)
        else:
            print("\nWe don't have any book")
        
    else:
        print("\nIncorrect input")



    print("\nDo you want to continue y/n? ")
    answer = input()
    if answer.lower() =='y':
        continue_playing = True
    elif answer.lower() =='n':
        continue_playing = False
        print("Thank you\nSee you later")       
    else: 
        print("\nIncorrect input\n")
        print("See you later")
        continue_playing = False
