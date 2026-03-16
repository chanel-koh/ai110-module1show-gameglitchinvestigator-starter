# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked like a minimalist guessing game, with a text box to enter a guess, hints popping up with each incorrect guess, and a toggle menu to choose a difficulty setting. There is also a 'developer debug info' box where I could see the secret number and what the history and scoring looked like on the backend.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints said "go higher" for all my non-correct guesses, regardless if I had to go higher or lower. For example, when the secret number was 22 and my guess was 43, I expected the hint to say "go lower," but it said "go higher" instead. It only said "go lower" if I put 100.
  2. The score in the developer debug info was different than the displayed final score to the game user. For example, when I guessed the secret number correctly, the debug info said my score was 5, but the score displayed to the user was the value of my highest guess, 43. I expected them to be the same.
  3. If you start a new game, the secret number resets but the game is stuck on saying "You already won. Start a new game to play again." For example, once I pressed new game, I expected my guesses to be processed and responded to with "go higher" or "go lower," but the hints only said the "already won" text described above.
  4. Hard mode is a range between 1-50 but normal is between 1-100, which seems harder because there are more possibilities for the secret number.
  5. It takes two 'submit guess' clicks to put the first guess into history. I expected that with each press of "submit guess," the guess would be put in history.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
GitHub Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
For refactoring the check_guess function, I asked Copilot to fix the bug of incorrect go higher/go lower hints. The AI suggested to remove the line giving the intentional bug where if the guess attempt was even, the guess would be trated as a string, giving a string-int comparison. This was correct because without that chunk of code, the check_guess correctly receives a int to give correct go higher/go lower hints. I verified this result by seeing that the string cast was no longer in the code. I also verified this by running the application and seeing that the hints worked correctly when I put a number lower and higher than the secret.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For refactoring the get_range_for_difficulty function, I asked Copilot to fix the range error between normal and hard, since normal had a wider range than hard. The AI suggestion deviated from what I was looking for because I wanted Copilot to swap the ranges of medium and hard. Instead, it kept the range of normal and gave a new range for hard (normal: 1-100, hard: 1-1000 instead of what I was looking for, normal: 1-50, hard: 1-100). I verified the result by comparing the original ranges of the code to the resulting ranges Copilot gave in its answer. I also verified the result by running the application and seeing the ranges for Normal and Hard mode. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested whether a bug was really fiixed through a pytest case and by running the application to see if a bug was fixed. For example, to verify that hints properly said go higher or go lower, I wrote a pytest for each and saw that they passed. I also opened the application and put a guess higher and lower than the secret and saw that it functioned as expected.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest that verified that the hard mode range was between 1 and 100. It showed me that the guess range was properly configured.

- Did AI help you design or understand any tests? How?
  Yes, AI helped design the hard mode range test after I asked it to write a test to verify the guess ranges, a bug that I had just fixed with the assistance of Copilot. AI also helped me understand why some existing tests that tested the higher and lower hints were not passing by explaining that the function I was calling returned a tuple, not a single value like the tests assumed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain Streamlit reruns as a refreshed state of the app - whatever changes were made in the source code are reflected in the rerun. Therefore, whenever you make changes to a Streamlit application's source code, you should rerun it to test the changes. Otherwise, you will still see the old version of the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - One prompting strategy that I want to reuse in the future is to give multistep instructions with a format like we practiced in this project, such as "Move this function to this file, update the logic to accomplish this goal, and update its import in this other file."
  -I would also like to reuse the testing habits practiced in this project, such as using pytest to test simple, smaller pieces of a functionality to ensure it works.

- What is one thing you would do differently next time you work with AI on a coding task?
  -One thing I would do differently is to break down the assistance into multiple phases, such as first identifying the bug, then asking for refactoring suggestions, then writing tests to verify changes. This keeps the prompts much more specific and easily verifyable, as opposed to making a lot of changes at once and just going along with what the AI is doing.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  -This project helped me realize how to use AI as a coding partner rather than the sole driver of the coding process by checking its output and giving human input along the way.
