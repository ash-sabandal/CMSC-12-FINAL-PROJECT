def menu():
    print("""
=======:{ MAIN MENU }:=======
[1] Books Section
[2] Borrowers Section
[3] Logbook Section
[4] Load State
[5] Save State
[6] Exit
=============================
          """)
    choice = input("Input choice: ")
    return choice

def books_section():
    print("""
=====:{ BOOKS SECTION }:=====
[1] Add book
[2] Delete Book
[3] Delete All books
[4] View Book
[5] Edit Book
[6] View Pending
[7] Reurn to Main Menu
=============================
          """)
    choice = input("Input choice: ")
    return choice

def borrowers_section():
    print("""
===:{ BORROWERS SECTION }:===
[1] Borrow Book
[2] Return Book
[3] View All Entries
[4] View Expected Returns
[5] Reurn to Main Menu
=============================
          """)
    choice = input("Input choice: ")
    return choice

def logbook_section():
    print("""
====:{ LOGBOOK SECTION }:====
[1] Visit Library
[2] View All Entries
[3] View Transactions per Day
[4] Reurn to Main Menu
=============================
          """)
    choice = input("Input choice: ")
    return choice

def add_book(books_dict, book_count):
    print("Please enter the information about the book")
    title = input("Title: ")
    author = input("Author: ")
    date_published = input("Date Published (e.g. 9 Jan 2020): ")
    
    # assign book id
    Book_ID = "B" + str(book_count + 1)

    book_count += 1

    # set status
    status = "Available"

    # set list of borrowers
    borrowers_list = []

    # add the book to the books_dict
    books_dict[Book_ID] = [title, author, date_published, status, borrowers_list]
    
    print("SUCCESS:", title, "by", author, "has been added")

    return books_dict, book_count

def del_book(books_dict):
    print("Please enter the information about the book")
    title = input("Title: ")
    author = input("Author: ")

    # iterate in books dictionary, check if the title and author matches with the book info of every book
    for Book_ID, book_info in list(books_dict.items()):
        if title.lower() == book_info[0].lower() and author.lower() == book_info[1].lower():
            books_dict.pop(Book_ID)
            print("SUCCESS:", title, "by", author, "has been deleted")
            return books_dict
    # if done with the iteration and no match found, print the message and return the books dictionary with no deletion
    print("UNSUCCESS: No book matches with", title, "by", author)
    return books_dict

def del_allbooks(books_dict):
    print("These books are about to be deleted: ")
    for book_info in books_dict.values():
        print(book_info[0], "by", book_info[1])

    choice = input("Enter 'y' to continue: ")

    if choice.lower() == 'y':
        books_dict = {}
        print("SUCCESS: All books have been deleted")
        return books_dict
    
    print("UNSUCCESS: The deletion has been cancelled ")
    return books_dict

def view_book(borrowers_dict, logbook_dict, books_dict):
    print("Please enter the information about the book")
    title = input("Title: ")
    author = input("Author: ")

    print("Title\t\t\t\tAuthor\t\t\t\tDate Published\t\tStatus\t\tList of Borowwers")
    j = 0
    # iterate in books dictionary, check if the title and author matches with the book info of every book
    for id, book_info in list(books_dict.items()):
        if title.lower() == book_info[0].lower() and author.lower() == book_info[1].lower():
            j += 1
            print((book_info[0] +((23-len(book_info[0])) * " ")), end="\t\t")
            print((book_info[1] +((23-len(book_info[1])) * " ")), end="\t\t")
            print(book_info[2], end="\t\t")
            print(book_info[3], end="\t")

            for id, borrow_info in borrowers_dict.items():
                for i in range(len(book_info[-1])):
                    if id == book_info[-1][i]:
                        for id, log_info in logbook_dict.items():
                            if id == borrow_info[1]:
                                print(log_info[0], end="\n")
                                print("\t" * 13, end="")

    if j == 0:
        print("UNSUCCESS: No book matches with", title, "by", author)


def edit_book(books_dict):
    print("Please enter the information about the book")
    title = input("Title: ")
    

    # iterate in books dictionary, check if the title matches with the book info of every book
    for Book_ID, book_info in list(books_dict.items()):
        if title.lower() == book_info[0].lower():
            print("Please enter the new information about the book")
            new_title = input("Title: ")
            new_author = input("Author: ")
            new_date_published = input("Date Published (e.g. 9 Jan 2020): ")

            #edit the values (in a list) 
            books_dict[Book_ID][0] = new_title
            books_dict[Book_ID][1] = new_author
            books_dict[Book_ID][2] = new_date_published

            print("SUCCESS: Information for", title, "has been updated")
            return books_dict
    # if done with the iteration and no match found, print the message and return the books dictionary with no modifications
    print("UNSUCCESS: No book matches with the title of", title)
    return books_dict

""" 
(books dictionary)
B1(book_id): [Title, Author, Date Published, Status, ['BL1', 'BL2', 'BL3']] 

(borrowers dictionary)
BL1(borrow_id): [B1(book_id), L1(log_id), Return Date] 

(logbook dictionary)
L1(log_id): [Person Name, Date, Time, Purpose]
"""

def view_pending(borrowers_dict, logbook_dict, books_dict):
    print("Title\t\t\t\tAuthor\t\t\t\tDate Published\t\tStatus\t\tLast Borowwer\t\t\tReturn Date")
    i = 0
    # iterate in books dictionary
    for book_info in books_dict.values():
        # get only the unavailable books
        if book_info[-2] == "Unavailable":
            i += 1
            print((book_info[0] +((23-len(book_info[0])) * " ")), end="\t\t")
            print((book_info[1] +((23-len(book_info[1])) * " ")), end="\t\t")
            print(book_info[2], end="\t\t")
            print(book_info[3], end="\t")

            # iterate in borrowers dictionary
            for borrow_id, borrow_info in borrowers_dict.items():
                # check where does the last borrower in book info match in Borrow IDs
                if book_info[-1][-1] == borrow_id:
                    # iterate in logbook dictionary
                    for log_id, log_info in logbook_dict.items():
                        # check where does the Log ID in the borrow info match in Log IDs
                        if borrow_info[1] == log_id:
                            print((log_info[0] +((23-len(log_info[0])) * " ")), end="\t\t")
                    print(borrow_info[-1], end="\n")
    if i == 0:
        print("INFO: No pending books found")
    

def borrow_book(borrowers_dict, logbook_dict, books_dict):
    print("Please enter the information about the book")
    title = input("Title: ")
    author = input("Author: ")

    #iterate in books dictionary, check where does the title and author matches with every book info
    for BookID, book_info in books_dict.items():
        if title.lower() == book_info[0].lower() and author.lower() == book_info[1].lower():
            # check if it is available (not borrowed)
            if book_info[-2] == "Available":

                # create entry in logbook dictionary
                logbook_dict = visit_library(logbook_dict)

                #check the last log ID
                Log_ID = list(logbook_dict)[-1]

                #get the matched BookID
                Book_ID = BookID
        
                if borrowers_dict == {}:
                    last_id_no = 0
                # check last Book_ID, remove the 'BL', get the number after 'BL' 
                else:
                    last_id_no = int(list(borrowers_dict.keys())[-1][2:])
                
                # get the date of return
                date_of_return = input("Date of Return (e.g. 9 Jan 2020): ")

                # assign borrow id
                Borrow_ID = "BL" + str(last_id_no + 1)

                # add the borrower to the borrowers_dict
                borrowers_dict[Borrow_ID] = [Book_ID, Log_ID, date_of_return]

                # append Borrow_ID to the book_info[-1] (to the last element of the book_info(list) which is the list containing the list of borrowers)
                book_info[-1].append(Borrow_ID)

                # change the status to unavailable
                book_info[-2] = "Unavailable"

                print("SUCCESS:", title, "by", author, "has been successfully borrowed")
                return borrowers_dict, logbook_dict, books_dict
            
            # if unavailable (borrowed):
            else:
                print("UNSUCCESS:", title, "by", author, "is currently borrowed")
                return borrowers_dict, logbook_dict, books_dict
        
    #if done with the iteration and no match found, print the message and return the dictionaries with no modification
    print("UNSUCCESS: No book matches with", title, "by", author)

    return borrowers_dict, logbook_dict, books_dict

def return_book(logbook_dict, books_dict):
    print("Please enter the information about the book")
    title = input("Title: ")
    author = input("Author: ")

    #iterate in books dictionary, check where does the title and author matches with every book info
    for book_info in books_dict.values():
        if title.lower() == book_info[0].lower() and author.lower() == book_info[1].lower():
            # check if it is unavailable (borrowed)
            if book_info[-2] == "Unavailable":

                # create entry in logbook dictionary
                logbook_dict = visit_library(logbook_dict)

                # change the status to available
                book_info[-2] = "Available"

                print("SUCCESS:", title, "by", author, "has been successfully returned")
                return logbook_dict, books_dict
            
            # if available (not borrowed):
            else:
                print("UNSUCCESS:", title, "by", author, "is currently not borrowed")
                return logbook_dict, books_dict
        
    #if done with the iteration and no match found, print the message and return the dictionaries with no modification
    print("UNSUCCESS: No book matches with", title, "by", author)

    return logbook_dict, books_dict

""" 
(books dictionary)
B1(book_id): [Title, Author, Date Published, Status, ['BL1', 'BL2', 'BL3']] 

(borrowers dictionary)
BL1(borrow_id): [B1(book_id), L1(log_id), Return Date] 

(logbook dictionary)
L1(log_id): [Person Name, Date, Time, Purpose]
"""

def view_all_entries_borrow(borrowers_dict, logbook_dict, books_dict):
    print("Borrow ID\tTitle\t\t\t\tAuthor\t\t\t\tDate Published\t\tReturn Date\t\tBorowwer")
    for borrow_id, borrow_info in borrowers_dict.items():
        print(borrow_id, end="\t\t")
        # iterate in books dictionary
        for book_id, book_info in books_dict.items():
            # check where does the book ID in borrow info match in Book IDs
            if borrow_info[0] == book_id:
                print((book_info[0] +((23-len(book_info[0])) * " ")), end="\t\t")
                print((book_info[1] +((23-len(book_info[1])) * " ")), end="\t\t")
                print(book_info[2], end="\t\t")
        print(borrow_info[-1], end="\t\t")
        
        # iterate in logbook dictionary
        for log_id, log_info in logbook_dict.items():
            # check where does the log ID in borrow info match in Log IDs
            if borrow_info[1] == log_id:
                print(log_info[0], end="\n")

def view_expected_returns(borrowers_dict, logbook_dict, books_dict):
    return_date = input("Enter return date to view (e.g. 9 Jan 2020): ")
    print("Borrow ID\tTitle\t\t\t\tAuthor\t\t\t\tDate Published\t\tStatus\t\tBorowwer")
    i = 0
    for borrow_id, borrow_info in borrowers_dict.items():
        # get the matches with the return date input
        if borrow_info[-1].lower() == return_date.lower():
            i += 1
            print(borrow_id, end="\t\t")
            # iterate in books dictionary
            for book_id, book_info in books_dict.items():
                # check where does the book ID in borrow info match in Book IDs
                if borrow_info[0] == book_id:
                    print((book_info[0] +((23-len(book_info[0])) * " ")), end="\t\t")
                    print((book_info[1] +((23-len(book_info[1])) * " ")), end="\t\t")
                    print(book_info[2], end="\t\t")
                    print(book_info[3], end="\t\t")

            # iterate in logbook dictionary
            for log_id, log_info in logbook_dict.items():
                # check where does the log ID in borrow info match in Log IDs
                if borrow_info[1] == log_id:
                    print(log_info[0], end="\n")
    if i == 0:
        print("INFO: No expected returns on", return_date)


def visit_library(logbook_dict):
    print("Please enter the following information for the log entry")
    name = input("Person Name: ")
    date = input("Date (e.g. 9 Jan 2020): ")
    time = input("Time (e.g. 10:30AM): ")
    purpose = input("Purpose (borrow, return, or visit): ")

    if logbook_dict == {}:
        last_id_no = 0

    # check last Book_ID, remove the 'L', get the number after 'L' 
    else:
        last_id_no = int(list(logbook_dict.keys())[-1][1:])
    
    # assign book id
    Log_ID = "L" + str(last_id_no + 1)

    # add the book to the books_dict
    logbook_dict[Log_ID] = [name, date, time, purpose]
    
    return logbook_dict

def view_all_entries_logbook(logbook_dict):
    print("Log_ID\tPerson Name\t\t\tDate\t\t\tTime\t\tPurpose")
    
    for log_id, log_info in logbook_dict.items():
        print(log_id, end="\t")
        for i in range(len(log_info)):
            if i == 0:
                print((log_info[i] +((23-len(log_info[i])) * " ")), end="\t\t")
            else:
                print(log_info[i], end="\t\t")
        print()

def view_transactions_per_day(logbook_dict):
    transact_day = input("Enter transaction date to view (e.g. 9 Jan 2020): ")
    print("Log_ID\tPerson Name\t\t\tDate\t\t\tTime\t\tPurpose")
    i = 0
    for log_id, log_info in logbook_dict.items():
        # get only those who match with the input transaction day
        if transact_day.lower() == log_info[1].lower():
            i += 1
            print(log_id, end="\t")
            for i in range(len(log_info)):
                if i == 0:
                    print((log_info[i] +((23-len(log_info[i])) * " ")), end="\t\t")
                else:
                    print(log_info[i], end="\t\t")
            print()
    if i == 0:
        print("INFO: No transactions found on", transact_day)

def save_state(dict, book_count, filename):
    fileHandle = open(filename, "w")

    # all are ciphered per line
    if filename == "books.dat":
        # write the book_count in the first line
        fileHandle.write(cipher(str(book_count), "s") + "\n")
        # write the book id and book info in the succeeding lines, all separated by ";" 
        for k, v in dict.items():
            text = (k + ";" + v[0] + ";" + v[1] + ";" + v[2] + ";" + v[3] + ";" + str(v[4]))
            fileHandle.write(cipher(text, "s") + "\n")

    elif filename == "borrowers.dat":
        # write the borrow id and borrow info per line, all separated by ";" 
        for k, v in dict.items():
            text = (k + ";" + v[0] + ";" + v[1] + ";" + v[2])
            fileHandle.write(cipher(text, "s") + "\n")

    elif filename == "logbook.dat":
        # write the log id and log info per line, all separated by ";" 
        for k, v in dict.items():
            text = (k + ";" + v[0] + ";" + v[1] + ";" + v[2] + ";" + v[3])
            fileHandle.write(cipher(text, "s") + "\n")

    fileHandle.close()

def load_state(filename):
    fileHandle = open(filename, "r")
    dict = {}

    # all are deciphered per line
    if filename == "books.dat":
        i = 0
        for line in fileHandle:
            line = cipher(line[:-1], "l") + "\n"
            # first line is for the book count
            if i == 0:
                book_count = int(line[:-1])
                i += 1
            else:
                line_split = line.split(";")

                borrowers = []
                for i in line_split[-1][1:-2].split(", "):
                    if i != "":
                        borrowers.append(str(i[1:-1]))

                dict[line_split[0]] = [line_split[1], line_split[2], line_split[3], line_split[4], borrowers]
        return dict, book_count

    elif filename == "borrowers.dat":
        for line in fileHandle:
            line = cipher(line[:-1], "l") + "\n"
            line_split = line.split(";")
            dict[line_split[0]] = [line_split[1], line_split[2], line_split[3][:-1]]

    elif filename == "logbook.dat":
        for line in fileHandle:
            line = cipher(line[:-1], "l") + "\n"
            line_split = line.split(";")
            dict[line_split[0]] = [line_split[1], line_split[2], line_split[3], line_split[4][:-1]]

    fileHandle.close()
    return dict

def cipher(text, state):
    characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[]\;',./{}|:<>?"
    # numbers of shift depend on the line's length
    # if save, positive shift
    if state == "s":
        num = len(text)
        if num % len(characters) == 0 or num % len(characters) == 26:
            num = len(characters) // 2
    # if load, negative shift
    elif state == "l":
        num = len(text) * -1
        if -num % len(characters) == 0 or -num % len(characters) == 26:
            num = (len(characters) // 2) * -1

    new = ""
    for i in text:
        for j in range(len(characters)):
            if i == characters[j]:
                new += characters[(j + num) % len(characters)]
    return new