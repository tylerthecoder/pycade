# pycade

Want to create a game for pygame? Follow this guide.

All the games in pygame are stored in the `dev/games` folder

The most simple game consists of an `update` function and a `draw` function.
. The draw function takes your game state and draws it to the screen. There shouldn't be any logic in your draw function.

List of methods you can add to take advantage of the `pycade`

- \_\_init\_\_

  - This is a python function that is called whenever a new class is made, it will pass all the info you need to start your program (screen size, etc...)

- update
  - The update function handles all of your game logic (moving characters, applying damage, etc... )
- draw

- lastActions

- newActions
