## Modules Required
* prettytable
* matplotlib
* pygame


## Q1 "mdirectory.py"

1. Upon starting the program the file "entries.csv" is read and the corresponding entries are added to the Marks Directory. When the user exits the entries are saved back to the "entries.csv" file.

2. There are 6 types of choices available to the user:
    * Choice 1: Exit
    * Choice 2: Display Marks Directory
    * Choice 3: Add Entry
    * Choice 4: Search Entry
    * Choice 5: Remove Entry
    * Choice 6: Update Entry

3. Upon clicking any option, the user is prompted accordingly.


## Q2 "map.py"

1. There are 3 types of commands available to the user:
    * Command 1: {Distance}, {Direction} (e.g., "3, NW")
    * Command 2: Interpret
    * Command 3: Plot

2. Once a user is done, they are expected to press ENTER with empty input.

## Q3 "kaooa.py"

1. The game starts with the turn of the crow. The crows can be placed anywhere until all 7 crows have been placed. Afterward, to move a crow, first click on the crow you want to move, then click on the position (which should be empty) to which you want to move it.

2. The Vulture has to be placed on the first turn. After that, you can simply click on the position where you want to move the vulture to.

3. If the vulture can kill a crow, it must do so.

4. If the crows block the vulture such that the vulture can't make a move, then the crows win.

5. If 4 crows are killed, the Vulture wins as it cannot be blocked now.
