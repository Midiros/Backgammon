# Backgammon

Project made for the course APR2 in the bachelor's degree study programme Applied informatics at [UJEP](https://ujep.cz).

## Summary

The project is the implementation of the boardgame Backgammon done solely in Python.

## Requirements

- Python 3.11 or higher
- Colorama [link](https://pypi.org/project/colorama/)

## Installation

1. Clone the project to your machine.
2. Run the main game loop in shell:

   ```sh
   cd Backgammon/Classes/
   py board.py
   ```

## Gameplay loop
1. After start the player chooses which of the "gamemodes" they desire to play.
- `player vs. player` - Players each take turn until the end of the game
- `player vs. AI` -  Player takes his turn and afterwards the "opponent" chooses at random from their possible plays.

2. Game starts with a dice roll that decides whiich player starts. Players keep their diceroll.
3. Player that is on turn is presented with moves from which he picks the one he desires. 
4. Afterwards the main game loop starts, in which the players take turns until one moves all of his pieces of the board.
   * If the Player no.2 is the "AI", he is also presented with valid moves from which he picks at random what move to take.
5. The game ends with a statistic for each of the players and a short summary for the type of win and other notable information.

## Credits

The project was solely done by me.

## License

[GPL-3.0](LICENSE) © [Midiros](https://github.com/Midiros).
