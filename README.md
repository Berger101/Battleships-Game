# Battleships Game

Welcome to the Battleships Game – a classic naval combat experience brought to life in Python! Engage in thrilling battles against the computer and strategically position your fleet to dominate the high seas.

<img src="assets/images/battleshipsgame.png">

## Game Features

### Dynamic Gameplay
- Experience the excitement of naval warfare with a dynamic turn-based gameplay.
- Challenge the computer AI in intense one-on-one battles.

### Fleet Deployment
- Strategically place your fleet of five iconic ships: Carrier (5 cells), Battleship (4 cells), Cruiser (3 cells), Submarine (3 cells), and Destroyer (2 cells).
- Randomized ship placement ensures a unique and challenging experience in each game.

### Tactical Decision-Making
- Take turns to target your opponent's fleet by entering coordinates on the game board.
- Make wise choices to sink your opponent's ships and avoid their relentless attacks.

### Real-Time Feedback
- Receive real-time feedback on hits and misses, accompanied by colorful emojis for a visually engaging experience.
- See the state of the battlefield with a clear display of your and your opponent's boards.

### Victory Conditions
- Win the game by strategically sinking all of your opponent's ships.
- A computer victory occurs when your fleet is entirely submerged beneath the waves.

### Colorful Interface
- Enjoy a visually appealing game interface with color-coded text using the `colorama` library. 

## How to Play
1. Clone the repository to your local machine.
2. Run the game by executing the `run.py` script in your preferred Python environment.

Get ready for an immersive Battleships experience – command your fleet, outsmart your opponent, and claim victory on the high seas!

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Testing
- I tested that this page works in different browsers: Chrome, Firefox, Safari.
- I confirmed that this project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.
- I confirmed that you may choose where to target on the board and either a hit or miss occurs.
- I confirmed that all error handling works, cannot target same coordinates twice, strings and numbers over 9 are invalid inputs.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Local Deployment
Follow these steps to deploy the Monster Slaying Game on your local machine.

  <b>Clone the Repository</b>
  - Open a terminal and run the following command to clone the project repository:

```console
git clone https://github.com/your-username/battleships-game.git
```

  - Replace your-username with your GitHub username.
  <b>Navigate to the Project Directory</b>
  - Change into the project directory by running the following command in your terminal:

```console
cd battleships-game
```

  <b>Open the Game</b>
  - Open the index.html file in your preferred web browser. You can do this by double-clicking the file or right-clicking and choosing "Open with" your browser.
  <b>Enjoy the Game</b>
  - You are now ready to enjoy the Monster Slaying Game on your local machine! Feel free to explore the game interface, battle monsters, and test different strategies.
