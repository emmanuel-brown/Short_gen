const readline = require('readline');

// Generate a random number between 1 and 10
const randomNumber = Math.floor(Math.random() * 10) + 1;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function askForGuess() {
  rl.question('Guess a number between 1 and 10: ', (answer) => {
    // Check if the guess is correct
    if (parseInt(answer) === randomNumber) {
      console.log('You guessed the number!');
      rl.close();
    } else {
      console.log('Wrong guess, try again');
      askForGuess();
    }
  });
}

askForGuess();