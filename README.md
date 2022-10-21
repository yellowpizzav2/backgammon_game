# Welcome to the beautiful game of Backgammon.

### by Max Dinkelspiel and Elias Olcina

This game was created as our first project as NOD Coding Bootcamp (BC#4) 2022. It was supposed to be focused on functional programming and we created around 25 function for the game. We wanted a challenge and therefore decided to have a go at the game of Backgammon.

According to Wikipedia:
> *Backgammon is a two-player game of contrary movement in which each player has fifteen pieces, known traditionally as 'men' (short for 'tablemen') but increasingly known as 'checkers' in the US in recent decades. These pieces move along twenty-four 'points' according to the roll of two dice.* </br>
>
>![This is what the normal board looks like](https://i.imgur.com/koK7yPS.png)




This is how we present the board in the console for players to play. The board with the white background is the jupyter representation</br>
![The Game Board](https://i.imgur.com/eHEGr4J.png) 

The game is played by first rolling a die each to determine who goes first. The player with the highest roll use the dice just rolled to play their first turn. We promting the user to input which point they want to move from to which point they want move.



```
Player 1 (●), your turn.
Remaining die/dice:
+ - - - - +   + - - - - +
|  o      |   |  o      |
|         |   |    o    |
|      o  |   |      o  |
+ - - - - +   + - - - - +
Current board:
  ₁ ₁ ₁ ₁ ₁ ₁   ₁ ₂ ₂ ₂ ₂ ₂
  ³ ⁴ ⁵ ⁶ ⁷ ⁸   ⁹ ⁰ ¹ ² ³ ⁴
|━━━━━━━━━━━━━━━━━━━━━━━━━━━|
| ●       o   | o         ● |
| ●       o   | o         ● |
| ●       o   | o           |
| ●           | o           |
| ●           | o           |
|             |             |
|━━━━━━━━━━━━━━━━━━━━━━━━━━━|
|             |             |
| o           | ●           |
| o           | ●           |
| o       ●   | ●           |
| o       ●   | ●         o |
| o       ●   | ●         o |
|━━━━━━━━━━━━━━━━━━━━━━━━━━━|
  ₁ ₁ ₁ ₀ ₀ ₀   ₀ ₀ ₀ ₀ ₀ ₀
  ² ¹ ⁰ ⁹ ⁸ ⁷   ⁶ ⁵ ⁴ ³ ² ¹
From which row do you want to move a marker? (1-24):
```
The numbers above and below the board are the indices that correspond to each point 

We have removed the PIP score and the betting feature from the game since neither of us knows how that actually works and most people we know have never played with the feature.

In order to play the game you just have to download the python file and python it in your terminal/cmd. There are no real requirements.

```
python main.py
```
