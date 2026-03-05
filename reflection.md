# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Very buggy
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  Bug 1: The hints are backwards, so when it said go higher, it meant go lower and vice versa.
  Bug 2: You can't start a new game after winning or losing.
  Bug 3: Your score stays the same between games.
  Bug 4: Your attempts stay the same between games.
  Bug 5: You're allowed to enter values above or below the range.
  Bug 6: You can't actually submit your guess by pressing enter
  Bug 7: The attempts left notifier isn't correct, game ends earlier.
  Bug 8: Normal has a higher range than Hard

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested I fix the ranges on the difficulty modes
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude Code was pretty spot on on all the changes, I verified them and they worked flawlessly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried out the bug again and wrote test cases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I wrote test cases for range checks.
- Did AI help you design or understand any tests? How?
AI helped me with writing more complex test casess.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
secret was changing due to math.rand between 1-100
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
streamlit reruns are pretty intuitive

- What change did you make that finally gave the game a stable secret number?
added low and high parameters for range depending on the difficulty mode and it stayed consistent for each game.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
creating unit tests for my functions more
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I liked the way I used AI here, but I would definitely be a bit more hands on.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Claude code is an incredibly strong tool. Depending on how detaile I crafted my prompts, it could have completed this entire project within one or two prompts. Ultimately, its as good as the user makes it.
