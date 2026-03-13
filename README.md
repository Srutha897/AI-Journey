# AI-Journey
My 60-day AI learning journey

---

## Day 1 — March 9, 2026

It was a very productive day. Things I achieved today:

1) Watched 3Blue1Brown "Essence of Linear Algebra" Episodes 1–4.
   Learned how matrices work visually — what vectors really are,
   how transformations work, and why matrix multiplication is just
   chaining two transformations together. Astonishing to finally
   understand the WHY behind the math.

2) Solved 3 DSA problems: #1929, #1295, and #867.
   Problem #867 (Transpose Matrix) was hard at first but after
   the 3B1B lesson, I could visualize what transposing actually
   means geometrically — it clicked immediately after that.

3) Coded matrix multiplication from scratch using 3 nested loops
   (no libraries).
   Hardest part: getting i, j, and k right.
   Breakthrough: thinking of them as "row selector, column
   selector, and walker" made it clear.

5) Rewrote using NumPy. Results:
   - Manual code:     0.00037 seconds
   - NumPy:           0.00011 seconds  (3x faster on 3×3)
   - 300×300 matrix:  ~25,000x faster
   This is WHY neural networks need NumPy/PyTorch — training
   GPT on Python loops would take centuries.

Hardest moment: Figuring out where result=[] should live
                inside vs outside the function.
Best moment:    Seeing NumPy give the same answer instantly.

Tomorrow: Chain Rule & Derivatives —
          how AI figures out which direction to improve.

Confidence today: 8/10 🚀

## Day 02 — March 10, 2026

**Topics:** HashMaps, LeetCode, Micrograd

1. Learned HashMaps deeply via GeeksForGeeks.
   Key insight: O(1) lookup vs O(n) list search.
   On 1 million numbers -> HashMaps are 1 million
   times faster than brute force. This is why they
   matter in production AI systems.

2. Solved LeetCode #49 (Group Anagrams) and
   #1 (Two Sum).
   Approach: brute force first, then HashMap.
   Two Sum complexity improvement:
   Brute force = O(n²) → HashMap = O(n)

3. Watched Karpathy's Micrograd tutorial.
   Built Value class with add + mul operations.
   New tools discovered:
   -> graphviz: visualize computation graphs
   -> __repr__: customize object string output

Every day is a new learning.
Very excited to build again tomorrow! 🚀

Tomorrow: Movie Sentiment Analyzer project+ Leetcode

Confidence: 8/10

## Day 03 - March 11, 2026
Today was such an exciting day — probably one of the best starts I could have asked for!
What I built:
Started my first project in the 60-day AI journey — the Movie Sentiment Analyzer. Completed the data pipeline and model training (Days 3-5). Still to come: Streamlit web app and deployment.

What I learned:
The goal is to predict whether a movie review is positive or negative using machine learning.The goal is to predict whether a movie review is positive or negative using machine learning.
-> Imported and explored the IMDB 50k movie review dataset from Kaggle using Pandas
-> Cleaned raw text data (removed HTML tags, lowercased everything)
-> Checked for missing values — dataset was perfectly clean with zero nulls
-> Visualized sentiment distribution using Matplotlib
-> Converted text to numbers using TF-IDF vectorization
-> Split data into 80% training and 20% testing sets
-> Trained a Logistic Regression model on the vectorized data
-> Evaluated the model and hit 89.47% accuracy 🎉

Tools used: Python, Pandas, Scikit-learn, TF-IDF, Logistic Regression, Google Colab

Hardest Part:
Finding the bug that was killing my accuracy. I was getting 54-55% accuracy for a long time — barely better than random guessing. After a lot of debugging I discovered two issues: first, I wasn't cleaning the text before vectorization. But even after fixing that, accuracy stayed low. Eventually I realized I had used fit_transform on the test data instead of just transform — causing data leakage. The model was being trained and tested on completely different vocabularies! One tiny bug, huge impact. That's the biggest lesson of the day.

Fun part:
Everything honestly — the whole process of building something from scratch, seeing the accuracy jump from 54% to 89.47% after fixing the bug was incredibly satisfying.

LeetCode:
Solved #242 Valid Anagram and #217 Contains Duplicate using HashMaps and HashSets.
Ahead of schedule: Completed Days 3, 4 and 5 in a single sitting!!

Tomorrow: Streamlit web app for the sentiment analyzer, LeetCode, and theory.
Confidence today: 9/10

## Day 04 - March 12, 2026
Today was another productive day — and a historic one with my first ever AI app deployed live on the internet!
LeetCode:
Solved #128 Longest Consecutive Sequence using a HashSet approach.

Started with a sorting approach (O(n log n)) but optimized to O(n) using HashSet
Key insight: a number is only the start of a sequence if num - 1 is not in the set
Hit two bugs along the way:

longest variable was inside the while loop instead of outside — caused wrong answer for single element arrays
Was iterating over nums instead of nums_set — caused Time Limit Exceeded on large inputs with duplicates


Both bugs fixed and solution accepted! ✅

Project 1 — Completed & Deployed! 🎉
Finished and deployed the Movie Sentiment Analyzer live on Streamlit Cloud:

Built Streamlit web app with text input, confidence score and color bar
Added 3 example review buttons using session state
Deployed live — anyone in the world can use it now!
Live URL: https://movie-sentiment-analyzer-v4k7rzwgqy2rweqvbdvjjt.streamlit.app/

Theory:
Watched 3Blue1Brown Essence of Calculus Episode 1 — introduction to derivatives and the intuition behind them. Will be important for understanding how neural networks learn next week.
Tools used: Python, Streamlit, Scikit-learn, Pickle, GitHub
Tomorrow: LeetCode, Theory (Calculus Ep 2), Start Project 2 — Image Classifier with PyTorch 🐱
Confidence today: 8/10
