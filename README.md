# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      Purpose of the game is to guess a number between the bounds and get as many points as possible.
- [ ] Detail which bugs you found.
      Bug 1: The hints are backwards, so when it said go higher, it meant go lower and vice versa.
      Bug 2: You can't start a new game after winning or losing.
      Bug 3: Your score stays the same between games.
      Bug 4: Your attempts stay the same between games.
      Bug 5: You're allowed to enter values above or below the range.
      Bug 6: You can't actually submit your guess by pressing enter
      Bug 7: The attempts left notifier isn't correct, game ends earlier.
      Bug 8: Normal has a higher range than Hard
- [ ] Explain what fixes you applied.
      I applied fixes to all of the bugs above and wrote unit tests to make sure they functioned properly.
## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
      <img width="3022" height="1662" alt="Winning game" src="https://github.com/user-attachments/assets/e385f64f-9656-4c16-874c-8cf5a28ab459" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
