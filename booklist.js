/* An object-oriented book-list!

Create a class through the constructor invocation pattern. BookList = function() {}
BookLists should have the following properties:
Number of books marked as read (eg, BookList.booksRead)
Number of books marked not read yet
Next book to read(book object)(eg, BookList.nextBook() - returns a Book)
Current book being read (book object)
Last book read(book object)
An array of all the Books (eg BookList.bookShelf - is an array.)
Create another class called Book. Book = function() {}
Each book should have several properties:
Title, Genre, Author
Read (true or false)
Read date, can be blank, otherwise needs to be a JS Date() object
Every Booklist should have a few methods:
.add(book) - should add a book to the books list.
.finishCurrentBook()
Should mark the book that is currently being read as read
Give it a read date of new Date(Date.now())
Change the last book read to be the book that just got finished
Change the current book to be the next book to be read
Change the next book to be read property to be the first unread book you find in the list of books
Booklists and Books might need more methods than that. Try to think of more that might be useful.
*/

Booklist = function(bookArray) {
    this.booksRead = 0;
    this.booksNotRead = 0;
    this.currentBook = undefined;
	this.nextBook = undefined;
	this.lastBook = undefined;
	this.bookshelf = bookArray;

	this.updateCounts = function(){
		var read = 0;
		var unread = 0;
		for (var i=0; i < this.bookshelf.length; i++){
			if (this.bookshelf[i].read === True){
				read++;
			}
			else {
				unread++;
			}
		this.booksRead = read;
		this.booksNotRead = unread;
		console.log("Total books read: " + this.booksRead);
		console.log("Total books unread: " + this.booksNotRead);

		}
	}

	this.add = function(Book){
		this.bookshelf.push(Book);
        console.log("Added " + Book.title + " to your reading list.");
        this.updateCounts;
	};

	this.setCurrentBook = function(Book){
		this.currentBook = Book;
        this.currentBook.read = false;
        this.currentBook.readDate = undefined;
        console.log("Currently reading: " + this.currentBook.title);
	};

	this.setNextBook = function(Book){
        for (var i=0; i < this.bookshelf.length; i++){
            console.log(this.bookshelf[i].title);
            if (this.bookshelf[i].read === false) {
				this.setNextBook(this[i]);
                console.log("The next book to read is now " + this.nextBook.title);
				break;
            }
        }
	};
    
	this.finishCurrentBook = function(){
		this.lastBook = this.currentBook;
        this.lastBook.read = true;
        this.currentBook = undefined;
		//this.lastBook.readDate = new Date();
        console.log("Finished reading " + this.lastBook.title);
        this.updateCounts();
		};
};



var Book = function(title, author, genre, read, date){
	this.title = title,
	this.author = author,
	this.genre = genre,
	this.read = read;
	this.readDate = new Date(date);
};

var two666 = new Book("2666", "Roberto Bolano", "fiction", true, "Jul 7, 2013");
var lolita = new Book("Lolita", "Vladimir Nabokov", "fiction", true, "Jun 1997");
var summerland = new Book("Summerland", "Curtis Sittenfeld", "fiction", false);
var bookArray = [lolita, two666];
var aimeeList = new Booklist(bookArray);
aimeeList.add(summerland);
aimeeList.setCurrentBook(two666);
//aimeeList.setNextBook(summerland);
aimeeList.finishCurrentBook();