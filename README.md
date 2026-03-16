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

- The purpose of this game is to provide a simple guessing game with different difficulty modes and hints to point you to the secret number.
- Bugs found in the original implementation include incorrect hints due to string-int comparison instead of int-int comparison and a swapped normal vs. hard mode range.
- Fixes include enforcing an int-int comparison for correct go higher/go lower hints and a smaller range for normal compared to hard mode to match intuition of what makes the game harder. 

## 📸 Demo

- ![alt text](<Screenshot 2026-03-15 at 9.44.43 PM.png>)
- ![alt text](<Screenshot 2026-03-15 at 9.44.58 PM.png>)
- ![alt text](<Screenshot 2026-03-15 at 9.45.12 PM.png>)
- ![alt text](<Screenshot 2026-03-15 at 9.45.21 PM.png>)

## 🚀 Stretch Features
- ![alt text](<Screenshot 2026-03-15 at 10.18.16 PM.png>)
- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
