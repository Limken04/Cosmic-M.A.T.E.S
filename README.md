# Cosmic M.A.T.E.S gmaes

Cosmic M.A.T.E.S is an action-packed 2D space shooter from a neighboring parallel world. Written in Python using Pygame, this game lets you control your character with either the keyboard or a joystick. Prepare to fight through waves of enemies and face epic boss battles that will test your skills in this intergalactic adventure!

## Game launch

- Clone the repository: ``
- Change directory: `cd cosmic-Mates-pygame`
- Create a virtual environment: `python -m venv env`
- Activate the virtual environment: `source env/Scripts/activate`
- Install requirements: `pip install -r requirements.txt`
- Run the game: `python main.py`

## Controls

Shoot: SPACE
Move: Arrow keys
Pause: P
Exit: Esc

## Gameplay

[![Cosmic Mates](https://)](https:// "Cosmic Mates")

## Images

![alt text](images/l.png "Cosmic Mates")
![alt text](images/g0.png "Gameplay")
![alt text](images/g1.png "Gameplay")
![alt text](images/g2.png "Gameplay")
![alt text](images/g3.png "Gameplay")


The script you've described outlines the core mechanics and flow of a 2D space shooter game built using Pygame. Let's summarize and further break down its key components and how they contribute to the overall game structure.

1. Imports and Initialization
Modules: The script relies on Pygame for game development, with additional modules managing specific game entities like bullets, enemies, power-ups, and background animations.
Initialization: Pygame is initialized to set up the game window, ensuring the game has a canvas for rendering the game elements.
2. Main Function
Background Music: Starts playing background music to enhance the game atmosphere.
Animation: The animate_screen() function possibly handles any intro sequence or splash screen animation before transitioning to the main game loop.
3. Sprite Groups
Sprite Groups: These allow the game to organize various entities such as explosions, bullets, enemies, and power-ups into collections that can be iterated over and updated during each frame of the game. This helps with rendering and collision detection.
4. Game Variables
Player Stats: Variables like health, bullets, and score keep track of player state during gameplay.
Boss Stats: Variables track the boss's health and whether it's currently spawned.
Background Management: Different backgrounds can be loaded based on the player's score, making the game environment dynamic.
5. Asset Loading
Images and Sounds: Game assets are preloaded for efficiency, including player sprites, enemy sprites, and sound effects like shooting and explosions. This helps avoid delays during gameplay when switching between assets.
6. Game Loop
The game loop runs continuously, ensuring smooth gameplay until the user exits or the game is over.

Event Handling: The game constantly checks for inputs from the player, allowing the player to control movement, shooting, and pausing.
Player Controls: The player moves in response to key presses or joystick input, while shooting bullets in the chosen direction.
Background Scrolling: The background scrolls downward, creating the illusion of movement through space. The speed or type of background can change based on the score to reflect progress.
7. Enemy and Boss Spawning
Progressive Difficulty: Enemies spawn more frequently or in larger numbers as the score increases. This keeps the game challenging as the player progresses.
Boss Mechanic: Bosses spawn at predefined score intervals, presenting a more difficult challenge. Audio cues warn the player when a boss is about to appear.
8. Collision Detection
Collision Handling: The game checks for interactions between game entities, such as:
Bullets hitting enemies.
Player collecting power-ups.
Player hitting hazards (e.g., meteors, black holes).
Collisions can affect player health, increase score, or trigger explosion effects.
9. Health and Score Management
Health Bar: Displays the player's health visually, providing feedback on how much damage they can take before losing.
Score Tracking: The player’s score increases when they destroy enemies or collect items. The game can also save the high score across sessions.
10. Rendering
Frame-by-frame Drawing: Each frame, the game re-draws all elements (player, enemies, bullets, explosions, health bar) to the screen.
Display Updates: At the end of the loop, the screen is updated, ensuring that changes to game entities and background are reflected visually.
11. Game Over Condition
Game Over State: When the player's health reaches zero, a game over screen is displayed, followed by the option to restart or quit the game. Variables like health and score reset when a new game starts.
12. Cleanup and Exit
Exiting the Game: The game ensures a clean exit by properly closing the Pygame window and stopping background processes like music.
Summary
The Python script offers a well-structured 2D space shooter game with:

Player Controls: Smooth player movement and shooting mechanics.
Progressive Challenge: Increasing difficulty with enemy and boss spawning.
Collision and Interaction Handling: Mechanisms for detecting and responding to collisions between the player, enemies, bullets, and power-ups.
Health and Score Management: Clear feedback on health and score, with game progression and challenge scaling.
Visual and Audio Feedback: Real-time rendering of the game world, with sound effects to enhance the experience.