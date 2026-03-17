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
1)LeetCode:
Solved #128 Longest Consecutive Sequence using a HashSet approach.

Started with a sorting approach (O(n log n)) but optimized to O(n) using HashSet
Key insight: a number is only the start of a sequence if num - 1 is not in the set
Hit two bugs along the way:

longest variable was inside the while loop instead of outside — caused wrong answer for single element arrays
Was iterating over nums instead of nums_set — caused Time Limit Exceeded on large inputs with duplicates


Both bugs fixed and solution accepted! ✅

2)Project 1 — Completed & Deployed! 🎉
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

## Day 05 - March 13, 2026
Another eventful day — pushed further into deep learning territory with Project 2!
1)LeetCode:
Solved two problems today:
#349 Intersection of Two Arrays — Used HashSet approach. Looped through one set and checked membership in the other. Key learning: don't overcomplicate — the simplest solution is often the best one!
#167 Two Sum II — Introduced a brand new pattern today: Two Pointers. Since the array is sorted, used a left and right pointer moving inward. Much more efficient than brute force O(n²) approach.
2)Project 2 — Image Classifier (Started) 
Began building the Image Classifier using PyTorch and CIFAR-10 dataset (60,000 images across 10 classes):

Set up GPU runtime in Colab
Downloaded CIFAR-10 dataset using torchvision
Learned about transforms pipeline — ToTensor() + Normalize()
Created DataLoader with batch size of 32
Visualized first batch of images in a 2×5 grid

-> Key Learnings today:

Why we train in mini-batches — GPU memory + better generalization
CHW vs HWC format — PyTorch stores images as (Channels, Height, Width) but Matplotlib needs (Height, Width, Channels)
Normalization — scaling pixel values to -1 to 1 makes training faster
You don't need to memorize code — understand the WHY and look up the HOW

3)Theory:
Watched 3B1B Essence of Calculus Episode 2 — the paradox of instantaneous speed and how derivatives solve it using limits. The connection to gradient descent in neural networks is becoming clearer!
Tools used: Python, PyTorch, torchvision, Matplotlib, Google Colab
Tomorrow: Build first CNN from scratch + training loop 
Confidence today: 7/10

## Day 6 -March 14, 2026
A deep learning day — Constructed CNNs and watched a model learn from scratch in real time!
1)LeetCode:
#11 Container With Most Water — Two Pointers pattern. Start with widest container, move the shorter wall inward each time. Key insight: moving the shorter wall is the only way to potentially find more water.
#125 Valid Palindrome — Two Pointers again. Skip non-alphanumeric characters with isalnum(), compare from both ends moving inward. Wrote this one cleanly from scratch with no hints — big confidence boost! ✅
2)Theory — 3B1B Neural Networks Chapter 1:
Finally understood what's actually happening inside a neural network:

Data flows through input → hidden layers → output
Each connection has a weight — not just 0 to 1, but any number including negative
Model starts with random weights and gradually adjusts them to reduce loss
Loss function measures how wrong predictions are
Optimizer adjusts weights after every batch to reduce that loss
This connection to Calculus Ep 2 clicked today — derivatives tell the optimizer exactly which direction to adjust weights!

3)Project 2 — CNN Built and Trained! 
Built a full CNN from scratch in PyTorch and trained it on CIFAR-10 (60,000 images, 10 classes):
Architecture:
Input (3, 32, 32)
→ Conv1 + ReLU + MaxPool → (32, 16, 16)
→ Conv2 + ReLU + MaxPool → (64, 8, 8)
→ Flatten → 4096
→ FC1 + ReLU → 512
→ FC2 → 10 classes
Training results:
Epoch 1:  Loss 1.304 → Accuracy 53%
Epoch 5:  Loss 0.378 → Accuracy 86%
Epoch 10: Loss 0.092 → Accuracy 97%
Watched the model go from random guessing (53%) to 96.89% in 10 epochs — seeing loss drop and accuracy climb in real time was incredible!
Problem discovered — Overfitting:

Training accuracy: 96.89%
Test accuracy: 70.05%

The model memorized training data instead of learning general patterns — like a student who memorizes answers instead of understanding the subject. Will tackle this tomorrow using Transfer Learning with ResNet50!

Key Learnings:
What overfitting is and why it happens
Why test accuracy is more important than training accuracy
How Conv layers, ReLU and MaxPool work together
The full training loop: Forward pass → Loss → Backward pass → Update weights

Tools used: Python, PyTorch, torchvision, Google Colab, GPU (CUDA)
Tomorrow: Fix overfitting using Transfer Learning with ResNet50 — target 90%+ test accuracy! 🎯
Confidence today: 7/10

## Day 7 - March 15, 2026
"Always trust the process — you'll eventually get there!" 💪
A massive day of learning — went from 70% to 90.94% test accuracy and understood exactly why every decision mattered!
1) LeetCode:
-> #3 Longest Substring Without Repeating Characters — First Sliding Window problem! Used HashSet + two pointers. Window expands right, shrinks from left when duplicate found. Key optimization: use a Set not a List for O(1) lookup instead of O(n).
-> #424 Longest Repeating Character Replacement — Trickier Sliding Window. Key insight: you don't actually replace characters — you just check if window size - most frequent character count ≤ k. If not, shrink from left. Took a few attempts but got there!
2)Theory — 3B1B Neural Networks Chapter 2 (Gradient Descent):

-> Weights and biases are adjusted after every batch based on how wrong the model was
. Gradient descent = finding the lowest point in a loss landscape
. Model starts with random weights → calculates loss → adjusts weights slightly → repeats millions of times
. Connected directly to Calculus Ep 2 — derivatives tell the optimizer which direction to adjust weights!
. loss.backward() = calculate gradients, optimizer.step() = adjust weights

3) Project 2 — Transfer Learning with ResNet50 🚀
Today's full results:
Approach                   Train Accuracy       Test Accuracy
CNN from scratch             96.89%             70.05% (overfit!)
ResNet50 last layer only     81.70%             ~80%
ResNet50 + fine tuning       97.60%             90.94% ✅

-> Key Learnings:
. Overfitting & Early Stopping:
If we train to 100% accuracy the model starts memorizing instead of learning. When a new image appears it says "I never saw this exact image!" and fails. Early stopping catches the sweet spot where the model learned general features without memorizing specific examples.
. The 32x32 vs 224x224 Bug:
ResNet50 was trained on ImageNet with 224x224 images. Its architecture is specifically designed for that size — feeding 32x32 CIFAR-10 images crushed the features to nothing by the final layers → only 42% accuracy. After resizing to 224x224 → 90.94%! Always check the expected input size in model documentation before using pretrained models!
. Why Transfer Learning Works:
Early layers learned universal features (edges, textures) → frozen, kept intact
Layer4 learned ImageNet-specific features → unfrozen, adapted to CIFAR-10
Final layer replaced entirely for our 10 classes
Result: 23 million params of existing knowledge + fine tuning = 90.94% in minutes!

. Why 90.94% > 70.05% (not just Transfer Learning):
The CNN from scratch overfit badly (97% train, 70% test). ResNet50 with fine tuning generalized properly because it already understood visual features deeply — it learned WHAT cats look like, not just WHICH training images were cats.

Tools used: Python, PyTorch, torchvision, ResNet50, Google Colab, GPU (CUDA)
Tomorrow: Build Gradio web app + deploy on HuggingFace Spaces 🖼️
Confidence today: 8.5/10

## Day 8 - March 16,2026
Another huge day — Project 2 is now live on HuggingFace Spaces with 91% accuracy!
1) LeetCode:
#344 Reverse String — Classic Two Pointers problem. Used left and right pointers swapping characters inward. Key thing: modify the list in place — no returning a new list!
#567 Permutation in String — Sliding Window + HashMap combined. Instead of generating all permutations (impossible for long strings!), used a fixed size window of len(s1) sliding through s2. Compared character frequency maps — if they match, a permutation exists. Clean O(n) solution!
2) Theory — 3B1B Neural Networks Chapter 3 (Backpropagation):
The clearest explanation of how neural networks actually learn:

We cannot change activations directly — only weights and biases
Model makes prediction → checks how wrong it was → goes backwards through the network
For each weight asks: "Did increasing this weight make things better or worse?"
Nudges weights up or down based on their contribution to the error
Highly active neurons get nudged more — barely active neurons barely change
This backward correction process = Backpropagation
Connected directly to loss.backward() in our PyTorch code!

3) Project 2 — Image Classifier DEPLOYED! 🎉
Full journey today:

Saved trained ResNet50 model using torch.save()
Built Gradio web app with image upload + top 3 predictions
Deployed live on HuggingFace Spaces
Tested with real images — 100% cat, 99% airplane, 100% frog!

Test Results:
CNN from scratch:        70.05% test accuracy
ResNet50 last layer:     81.70% training accuracy  
ResNet50 + fine tuning:  91.03% test accuracy ✅
Key Learnings today:

Gradio is specifically designed for AI model demos — much easier than Streamlit for image tasks
HuggingFace Spaces = free deployment for AI models
CPU is enough for inference — GPU only needed for training
The Flag button in Gradio = users can report wrong predictions for model improvement
Why airplane got 99% airplane + 1% bird — both have wings, model was intelligently uncertain!

Also scored 10/10 on a quiz covering everything from Days 3-8 — TF-IDF, overfitting, backpropagation, transfer learning! 💪
Tools used: Python, PyTorch, torchvision, ResNet50, Gradio, HuggingFace Spaces
Live URL: [https://huggingface.co/spaces/srutha4/cifar10-image-classifier](https://huggingface.co/spaces/srutha4/cifar10-image-classifier)
Tomorrow: Start Project 3 — PDF Chat App using LangChain + RAG! 💬
Confidence today: 8.5/10
