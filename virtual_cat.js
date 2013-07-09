var Cat = function(name, tiredness, hunger, lonliness, happiness) {
    this.name = name,
    this.tiredness = tiredness,
    this.hunger = hunger,
    this.lonliness = lonliness,
    this.happiness = happiness,

        this.sleep = function(numMinutes) {
            for (var i=0; i < numMinutes; i++) {
                console.log('z');
            } //closes for loop
        this.tiredness = this.tiredness - numMinutes;
        console.log("Tiredness level: " + this.tiredness);
        main(catName);
        } //closes sleep function

        this.feed = function (amtFood) {
            console.log("Feeding cat");
            for (var i = 0; i < amtFood; i++){
                this.hunger --;
            }
            console.log("Hunger level: " + this.hunger);
            if (this.hunger > 10){
                this.sleep(this.hunger-10);
            }
            main(catName);
        } //closes feed function

        this.play = function(numMinutes, toy) {
            for (var i=0; i < numMinutes; i++){
                console.log("The cat is playing with its " + toy + "!");
                this.tiredness++;
            }
            console.log("The cat played for " + numMinutes + " minutes.");
            console.log("Now its tiredness level is " + this.tiredness);
            main(catName);
        }, //closes play function

        this.pet = function (amtPetting) {
            if (this.tiredness >= -3){
                console.log("Cat doesn't want to be petted right now.");
            }
            else{
                this.lonliness = this.lonliness - amtPetting;
                this.happiness = this.happiness + amtPetting;
                console.log("Lonliness: " + this.lonliness);
                console.log("Happiness: " + this.happiness);
            }
            main(catName);
        }, // closes pet function

        this.status = function() {
            console.log("The status of your cat:");
            console.log("Tiredness: " + this.tiredness);
            console.log("Hunger: " + this.hunger);
            console.log("Lonliness: " + this.lonliness);
            console.log("Happiness: " + this.happiness);
            main(catName);  
        } // closes status function

}//closes Cat class

function main (name) {
console.log("name is: " + name);
console.log("What do you want to do with your cat?");
var reply = prompt("What do you want to do with your cat?");
    if (reply === "feed") {
        console.log("How much do you want to feed your cat?");
        var amountFood = prompt("How much do you want to feed your cat?");
        name.feed(amountFood);
    }
    else if (reply === "pet") {
        console.log("How long do you want to pet your cat?");
        var howLongPet = prompt("How long do you want to pet your cat?");
        name.pet(howLongPet);
    }
    else if (reply === "play") {
        console.log("How long do you want to " + reply +" with your cat, and what toy do you want to use?");
        var response = prompt("How long do you want to " + reply +" with your cat, and what toy do you want to use?");
        var arrayResponse = response.split(" ");
        var howLongPlay = arrayResponse[0];
        var toy = arrayResponse[1];
        name.play(howLongPlay, toy);
    }

    else if (reply === "sleep"){
        console.log("How long do you want your cat to " + reply + "?");
        var sleepTime = prompt("How long do you want your cat to " + reply + "?");
        name.sleep(sleepTime);
    }

    else if (reply === "status") {
        name.status();
    }

    else {
        console.log("Your cat ignores you.");
        main(catName);
    }

}

var tribbles = new Cat ("Tribbles", 5, 5, 5, 5);
var fluffy = new Cat ("Fluffy", 8, 8, 8, 8);
var catName = fluffy;
main(catName);