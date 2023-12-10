import func

books_dict = {}
book_count = 0
borrowers_dict = {}
logbook_dict = {}

while True:
    x = func.menu()
    if x == "1":
        while True:
            x1 = func.books_section()
            if x1 == '1':
                books_dict, book_count = func.add_book(books_dict, book_count)
            elif x1 == '2':
                books_dict = func.del_book(books_dict)
            elif x1 == '3':
                books_dict = func.del_allbooks(books_dict)
            elif x1 == '4':
                func.view_book(borrowers_dict, logbook_dict, books_dict)
            elif x1 == '5':
                books_dict = func.edit_book(books_dict)
            elif x1 == '6':
                func.view_pending(borrowers_dict, logbook_dict, books_dict)
            elif x1 == '7':
                break
            else:
                print("Invalid Choice!")
    elif x == "2":
        while True:
            x2 = func.borrowers_section()
            if x2 == '1':
                borrowers_dict, logbook_dict, books_dict = func.borrow_book(borrowers_dict, logbook_dict, books_dict)
            elif x2 == '2':
                logbook_dict, books_dict = func.return_book(logbook_dict, books_dict)
            elif x2 == '3':
                func.view_all_entries_borrow(borrowers_dict, logbook_dict, books_dict)
            elif x2 == '4':
                func.view_expected_returns(borrowers_dict, logbook_dict, books_dict)
            elif x2 == '5':
                break
            else:
                print("Invalid Choice!")
    elif x == "3":
        while True:
            x3 = func.logbook_section()
            if x3 == '1':
                logbook_dict = func.visit_library(logbook_dict)
            elif x3 == '2':
                func.view_all_entries_logbook(logbook_dict)
            elif x3 == '3':
                func.view_transactions_per_day(logbook_dict)
            elif x3 == '4':
                break
            else:
                print("Invalid Choice!")
    elif x == "4":
        books_dict, book_count = func.load_state("books.dat")
        borrowers_dict = func.load_state("borrowers.dat")
        logbook_dict = func.load_state("logbook.dat")
        print("SUCCESS: State has been loaded")
    elif x == "5":
        func.save_state(books_dict, book_count, "books.dat")
        func.save_state(borrowers_dict, book_count,  "borrowers.dat")
        func.save_state(logbook_dict, book_count, "logbook.dat")
        print("SUCCESS: State has been saved")
    elif x == "6":
        break
    else:
        print("Invalid Choice!")