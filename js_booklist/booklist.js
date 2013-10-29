var Booklist = function(bookArray) {
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
			if (this.bookshelf[i].read === true){
				read++;
			}
			else {
				unread++;
			}
		}
        this.booksRead = read;
		this.booksNotRead = unread;
		console.log("Total books read: " + this.booksRead);
		console.log("Total books unread: " + this.booksNotRead);
	}

	this.addBook = function(Book){
		this.bookshelf.push(Book);
        console.log("Added " + Book.title + " to your reading list.");
        this.updateCounts();
	};

	this.setCurrentBook = function(Book){
		this.currentBook = Book;
        this.currentBook.read = false;
        this.currentBook.readDate = undefined;
        console.log("Currently reading: " + this.currentBook.title);
        this.updateCounts();
	};

	this.setNextBook = function(){
        for (var i=0; i < this.bookshelf.length; i++){
            if (this.bookshelf[i].read === false) {
				this.nextBook = (this.bookshelf[i]);
                console.log("The next book to read is now " + this.nextBook.title);
				break;
            }
        }
	};
    
	this.finishCurrentBook = function(){
		this.lastBook = this.currentBook;
        this.lastBook.read = true;
        this.currentBook = undefined;
        this.setNextBook();
		this.lastBook.readDate = new Date();
        console.log("Finished reading " + this.lastBook.title);
        this.updateCounts();
		};
};


var Book = function(title, author, genre, read, date){
	this.title = title,
	this.author = author,
	this.genre = genre,
	this.read = read;
	this.readDate = new Date(date)
};

var two666 = new Book("2666", "Roberto Bolano", "fiction", true, "Jul 7, 2013");
var lolita = new Book("Lolita", "Vladimir Nabokov", "fiction", true, "Jun 1997");
var summerland = new Book("Summerland", "Curtis Sittenfeld", "fiction", false);
var bookArray = [lolita, two666];
var aimeeList = new Booklist(bookArray);
//aimeeList.addBook(summerland);
//aimeeList.setCurrentBook(two666);
//aimeeList.finishCurrentBook();
//console.log(aimeeList);