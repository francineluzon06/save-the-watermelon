# Design Document (Progression 1)

## Problem Statement
Players must guess the secret word before the watermelon gets fully sliced.
Each incorrect guess removes one slice.

## Target Audience
Casual players and Python beginners learning loops, conditionals, and functions.

## Game Rules
- Guess letters to reveal the word.
- Each wrong guess removes a slice.
- Lose when slices = 0.
- Win when the full word is revealed.

## Core Features
- Random word selection  
- Guess tracking  
- Slice counter  
- Win/lose messages  

## Stretch Goals
- ASCII watermelon art  
- Difficulty settings  
- Scoreboard or hints  

## Data Design
- `secret`: string  
- `guessed`: set  
- `slices`: int  
- `MAX_SLICES`: constant  

## Module Responsibilities
- `game.py`: runs the game  
- `logic.py`: handles gameplay logic  
- `words.py`: stores word list
