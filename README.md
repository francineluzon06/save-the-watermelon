# save-the-watermelon

Project description (what, why). - How to run (commands). - How to test (commands). - Features & rules. 
## Project Description: 
This game was created to build a terminal-based word-guessing game in Python where the player must save the watermelon by guessing letters before the "slice counter" runs out.
This project introduces the application of an iterative software process, practicing clean Python, how to U\use Git/GitHub for versioned, professional submissions, and how to write and execute tests; document behavior and known issues.

## How to run (command):
```python
python -m src.game
```
## How to test (commands): 
```python
from src.logic import display_word
```

 ## Rules: 
- Guess letters to reveal the word.
- Each wrong guess removes a slice.
- Lose when slices = 0.
- Win when the full word is revealed.
