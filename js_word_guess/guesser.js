var word = ['F', 'O', 'X'];
var guessed = ['_', '_', '_'];

var guessLetter = function(letter) {
	for (i=0; i<word.length; i++){
		if (letter == word[i]) {
			guessed[i] = word[i];
			console.log("You found a letter!");
		}
	}
	console.log(guessed[0] + guessed[1] + guessed[2]);
	var gameOver = true;
	for (i=0; i<word.length; i++){
		if (guessed[i] == '_'){
			gameOver = false;
		}	
	}
	if (gameOver === true) {
		console.log("Congratulations! You guessed the word.");
	}
};

guessLetter("F");
guessLetter("Q");
guessLetter("O");
guessLetter("D");
guessLetter("X");