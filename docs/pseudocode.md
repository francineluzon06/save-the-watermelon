# Pseudocode (Progression 2)
```python
FUNCTION play_game
  secret ← random word
  guessed ← empty set
  slices ← MAX_SLICES

  PRINT welcome message

  WHILE slices > 0 AND word not complete
    DISPLAY masked word
    guess ← user input
    IF invalid input THEN repeat
    IF guess already guessed THEN notify
    ADD guess to guessed
    IF guess in word THEN display success
    ELSE slices ← slices - 1
    IF word fully revealed THEN player wins

  IF slices = 0 THEN player loses
END FUNCTION
```
