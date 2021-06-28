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

- onAction
  - Whenever the user moves the joy stick or presses a button this is called and you can set whatever variables you need to
    update your game.

Here is a very simple game that uses all these functions. I have take out the implementation details of the functions to focus on the core of the logic.

```python
	class FlappyBird:
		__init__(self, info):
			self.screenSize = info;

		update():
			updateBird();
			updatePipes();

		draw():
			drawBackground();
			drawPipes();
			drawBird();

		onAction(action)
			if (action is Actions.ACTION_BUTTON):
				bird.jump()
```
