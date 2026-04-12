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

## Day 9 - March 17, 2026
A deeply satisfying day — started the most in-demand AI skill right now: RAG with LangChain!
1) LeetCode:
1.1) #215 Kth Largest Element — Solved using Min Heap approach. Maintained a heap of size k — the smallest element in the heap is always the kth largest overall. Key insight: heap only guarantees smallest at index 0, rest is NOT sorted — that's what makes it faster than sorting at O(n log k)!
1.2) #33 Search in Rotated Sorted Array — Binary Search on a rotated array. The trick: check which half is sorted first, then determine if target falls in that half. If yes → search that half, if no → search the other. Reduced time complexity from O(n) to O(log n)! 💪
2) Theory — LangChain for LLM Application Development (3 Lessons):
2.1) Lesson 1 — Models, Prompts and Parsers:
PromptTemplate allows reusable prompts with variables — change tone, language style etc. Instead of hardcoding prompts, create templates that work dynamically with different inputs. This is how production AI apps handle prompts!
2.2) Lesson 2 — Memory:
Ever wondered how ChatGPT, Gemini or Claude remember your previous messages? The entire conversation history is sent with every new message! Different memory types handle this differently:

BufferMemory → stores everything word for word
TokenBufferMemory → stores up to X tokens only
SummaryMemory → summarizes old conversations to save space

2.3) Lesson 3 — Chains:
Chains connect multiple AI steps into one pipeline. Router chains find relevant data from uploaded content — like routing math questions to a math chain and physics questions to a physics chain. This directly powers the PDF Chat App!

3)Project 3 — PDF Chat App Started! 💬
Built the complete RAG pipeline today:
"Attention Is All You Need" paper (15 pages)
        ↓
PyPDFLoader → extracted text from all 15 pages
        ↓
RecursiveCharacterTextSplitter → 52 chunks
(chunk_size=1000, overlap=200)
        ↓
OpenAI Embeddings → converted chunks to vectors
        ↓
ChromaDB → stored 52 vectors on disk
        ↓
RetrievalQA Chain → connected ChromaDB to GPT-3.5
        ↓
Answered questions accurately! ✅
Test Results — Model answering from the paper:
Q: What is the attention mechanism?
A: Mapping a query and key-value pairs to output via weighted sum ✅

Q: How many attention heads?
A: 8 attention heads ✅

Q: What optimizer was used?
A: Adam optimizer ✅

Q: What datasets were used?
A: WMT 2014 English-German, English-French datasets ✅

Key Learnings:
-> RAG = Retrieval Augmented Generation — find relevant chunks → feed to GPT → get accurate answers
-> ChromaDB searches by MEANING not just keywords — semantic search!
-> Chunk overlap prevents context loss at chunk boundaries
-> Always hide API keys — never push to GitHub! Use Colab Secrets for safety
-> LangChain updates frequently — always check latest import paths!

⭐Tools used: Python, LangChain, OpenAI API, ChromaDB, PyPDF, Google Colab
🚀Tomorrow:
Morning revision of all topics from Days 3-9
Continue Project 3 — build Streamlit chat interface + deploy!

Confidence today: 7.5/10

## Day 10 - March 18, 2026
A debugging heavy day — but every bug got fixed! 🔧
1) LeetCode:
#153 Find Minimum in Rotated Sorted Array — Binary Search pattern again. Key insight: compare nums[mid] with nums[right] to determine which half the minimum is in. If nums[mid] > nums[right] → minimum is in right half. Clean O(log n) solution! ✅
2) Project 3 — PDF Chat App (Streamlit Interface Built!) 💬
Built the complete Streamlit interface around yesterday's RAG pipeline:
Features built:

. PDF uploader in sidebar
. OpenAI API key input (secure — never hardcoded!)
. Chat interface with message history
. Clear conversation button
. Processing spinner while PDF loads
. Success message showing chunks created

Bugs encountered and fixed:
Bug 1: New PDF still answered from old PDF
→ Cause: ChromaDB reusing same collection
→ Fix: Added uuid to create unique collection per PDF
       collection_name = f"pdf_{uuid.uuid4().hex[:8]}"

Bug 2: Old chat messages showing when new PDF uploaded
→ Cause: Session state not resetting properly
→ Fix: Added st.rerun() to force immediate refresh
Testing Results:
Short stories PDF:
Q: "What is this PDF about?"
A: "Collection of children's stories..." ✅

Research paper PDF:
Q: "What is attention?"
A: "Maps query and key-value pairs to output..." ✅

Puzzle PDF (scanned):
→ Garbled text — expected behavior for non-text PDFs
→ Will add user warning about PDF type limitations

Key Learning Today:
"Debugging is not failure — it's engineering. Every bug you fix makes you a better developer."

Also learned:
->uuid for creating unique identifiers
->ChromaDB collection isolation
->Streamlit session state management
->Why scanned PDFs fail text extraction (need OCR)

Tomorrow:
Deploy on Streamlit Cloud
Write README
Project 3 complete! 🎉

Tools used: Python, Streamlit, LangChain, ChromaDB, OpenAI API
Confidence today: 6/10 — Debugging is hard but every bug got fixed! 💪

## Day 11 - March 19, 2026
Short but significant day — Project 3 is now live! 🚀
Project 3 — PDF Chat App DEPLOYED! 💬
Deployed the PDF Chat App on Streamlit Cloud. [https://pdf-chat-app-qjcribffrvfykva3f6tv6r.streamlit.app/]

App successfully answers questions from any text-based PDF using RAG (Retrieval Augmented Generation).
Live test results:
Q: "What is attention?"
A: "An attention function maps a query and 
    key-value pairs to an output..." ✅

Q: "What is transformer architecture?"
A: "A model that relies entirely on attention
    mechanism..." ✅
Live URL: your-streamlit-link
Portfolio status:
Project 1: Movie Sentiment Analyzer ✅ Live
Project 2: Image Classifier ✅ Live
Project 3: PDF Chat App ✅ Live
3 projects deployed in 11 days — ahead of schedule! 💪
Tomorrow: Revision day + start Project 4 (AI Research Agent)
Confidence today: 7/10 — Tired but kept the streak alive! 🔥

## Day 12 - March 20, 2026

Short but focused day — quality over quantity!

**Revision:**
Deep revision of Project 1 — Movie Sentiment Analyzer.
Cleared doubts on:
- train_test_split and what each variable means
- random_state and why it matters for reproducibility
- The complete pipeline from raw CSV to deployed app

**LeetCode:**
**#56 Merge Intervals** — New pattern: Intervals!
Sort by start time → loop through → merge overlapping.
Key insight: use max() when merging end points to handle
edge cases where one interval contains another.
Solved cleanly without hints! ✅

**Tomorrow:**
- Revise Project 2 and Project 3
- LeetCode #57 Insert Interval
- Start Project 4 — AI Research Agent!

**Confidence today: 7/10**

## Day 13 - March 21, 2026

Dedicated revision day — quality over quantity!

**Revision:**
- Deep revision of Project 2 — CNNs, 
  Transfer Learning, PyTorch
- Wrote detailed notes in notebook
- Learned what gradients are and why 
  zero_grad() matters

**Quiz Results: 96/100 🎉**
- TF-IDF ✅
- Data Leakage ✅  
- Transfer Learning ✅
- Training Loop ✅
- Only minor confusions on data leakage 
  vs overfitting — now clarified!

**Tomorrow:**
- LeetCode #57 Insert Interval
- Revise Project 3
- Start Project 4 — AI Research Agent!

**Confidence today: 8.5/10**

## Day 14 - March 22, 2026
Short and focused day — kept the streak alive! 🔥
1)LeetCode:
#57 Insert Interval — Intervals pattern continued. Handled 3 cases cleanly:

Intervals ending before new interval → add as is
Overlapping intervals → merge using min/max
Intervals starting after new interval → add as is

Key insight: Unlike #56, no sorting needed — input is already sorted! Wrote clean code with comments explaining each section. ✅
2)Revision:
Quick revision of Project 3 — RAG pipeline, ChromaDB, chunk overlap and why we used OpenAI over HuggingFace.
Tomorrow:
Full energy day — Start Project 4 (AI Research Agent)! 🤖
Confidence today: 5/10 — Tired but kept the streak! 💪

## Day 15 — March 23, 2026
It was a practical debugging and systems-integration day. Things I achieved today:

1)Solved LeetCode problem #75 (Sort Colors). Implemented the Dutch National Flag algorithm using three pointers (`low`, `mid`, `high`). Key insight: not incrementing `mid` when swapping with `high` because the incoming element is unprocessed. Reinforced in-place partitioning and one-pass optimization (O(n) time, O(1) space).

2) Started building the 4th project, AI Research Agent. The system takes a query, searches the web, processes results, and generates an answer autonomously — a shift from simple LLM usage to agent-based workflows.
Set up LangChain, OpenAI API, and DuckDuckGo search in Google Colab. Observed how agents use the ReAct (Reason + Act) pattern to iteratively think, act, and refine outputs.

Ran into multiple real-world issues:
->Dependency/import errors with LangChain. Instead of deeply modifying the setup, reused the working environment and reran cells to stabilize execution.
->API key error (`Illegal header value`). Root cause: extra whitespace/newline characters in the key. Fixed by re-entering the API key correctly and rerunning the setup. ---->Also learned the importance of not exposing API keys.

Key realization: a lot of real engineering work is not writing new code, but fixing environment issues, rerunning pipelines, and ensuring everything works end-to-end.

Best moment: Successfully running the agent and seeing it search the web and generate an answer autonomously.

Hardest moment: Debugging setup issues and identifying that the API key formatting was the root cause rather than the code itself.

Tomorrow: Improve the agent output formatting and better understand how to control responses.

Confidence today: 8/10 🤖

## Day 16 - March 24, 2026
What I built:
1) Completed Project 4 — AI Research Agent. Built a full Streamlit UI on top of the LangChain ReAct agent from Day 15 and deployed it live on Streamlit Cloud.
2)LeetCode:
Solved #435 Non-overlapping Intervals. Key insight: sort by end time (greedy) — always keep the interval that ends earliest to leave maximum room for future intervals. Different from #56 Merge Intervals which sorts by start time because the goal is different — here we want to maximize intervals that fit, not merge neighbors.
-> Project 4 UI:

   Used return_intermediate_steps=True instead of StreamlitCallbackHandler to capture agent thinking steps and render them manually in the UI
   Built 3 feature cards (ReAct Pattern, Live Web Search, GPT-3.5 Turbo) with colored borders
   Dark theme with gradient title, purple thinking box, green final answer box
   st.form for Enter key support on search
   
-> Deployment battle:
   Hit multiple errors on Streamlit Cloud — Python 3.14 incompatibility with LangChain 0.1.20, version conflicts between langchain-core and langchain. Fixed by manually        setting Python 3.11 in Streamlit Cloud settings and pinning correct library versions in requirements.txt. Root cause: forgot requirements.txt before first deploy +          accidentally selected Python 3.14.
Key lesson:
   Always create requirements.txt with pinned versions BEFORE deploying. Without it, the platform installs latest everything — which may break older library versions.
   Live URL: https://researchagent-f5wfyafgyctbcyrjkbg53t.streamlit.app/
Confidence: 8/10
Tough deployment but pushed through every error. UI looks professional and portfolio-ready.

## Day 17 - March 25, 2026
Today was a solid revision day — quiz score of 95/100 shows the concepts are really sticking!
1) LeetCode:
Solved #20 Valid Parentheses — first Stack pattern problem.

Key insight: Stack is LIFO — the last opening bracket must be closed first
Used a closeToOpen dictionary mapping closers to their expected openers
Two checks on every closing bracket: is stack non-empty? does top match expected opener?
If either fails → return False immediately. Empty stack at end = True ✅

2) Project 3 Revision — PDF Chat App 🧠
Revised all core RAG concepts:

Full pipeline: PDF → extract → chunk → embeddings → ChromaDB → retrieve → GPT answers
Sharpened: chunking isn't just for speed — GPT has a hard context window limit. A 100 page PDF literally cannot be sent in one go
Sharpened: RecursiveCharacterTextSplitter splits by paragraphs first, then sentences, then characters — smarter than blind cutting
Scanned PDF limitation: PyPDF returns garbled text because scanned PDFs are images with no text layer. Fix = OCR tools like pytesseract

Quiz Score: 95/100 🎉
Consistent deep understanding across all RAG concepts — pipeline, ChromaDB, embeddings, UUID bug, QA chain all solid.
Tools used: Python, LangChain, ChromaDB, OpenAI, Streamlit
Tomorrow: Project 4 revision + quiz, LeetCode Stack pattern (#155 Min Stack), Job prep — resume update with all 4 projects 🚀

Confidence today: 8/10

## Day 18 - March 26, 2026
Today was a power day — quiz, revision, resume and even a deep dive into how the agent thinks!
1) LeetCode:
Solved #155 Min Stack — second Stack pattern problem.

Key insight: use two stacks running in parallel — one for actual values, one tracking the minimum at every state
Every push → append to both stacks. Every pop → pop from both stacks
getMin() just returns minStack[-1] → O(1) instant, no looping needed
Important guard: self.minStack[-1] if self.minStack else val — prevents IndexError on empty stack
Had the right idea independently before explanation — two stacks approach was correct! ✅

2) Project 4 Revision — AI Research Agent 🧠
Revised all core concepts:

AI Agent vs LLM: agent plans, uses tools, reasons autonomously — not just question → answer
ReAct pattern: Reason → Act → Observe loop. Stops when agent has enough info
max_iterations=10 prevents infinite loops AND protects OpenAI API budget from infinite calls
handle_parsing_errors=True catches formatting errors → tells agent to retry instead of crashing
return_intermediate_steps=True captures thinking steps as data → rendered manually in UI
api_key.strip() removes hidden \n, \r, \t characters that cause LocalProtocolError
LangChain Tool needs 3 things: name, func, description — better description = better results

Quiz Score: 97/100 🏆 Best quiz score yet! 

3) Agent Search Behavior 🔍
Discovered why agent sometimes fails on Step 1: GPT-3.5 adds quotes to search queries ("color mixing red and yellow") from training habits. Quoted searches are rigid → irrelevant results. Fix: add "WITHOUT quotes" to tool description. Agent correctly self-corrects in Step 2 — ReAct loop working as designed.
Tools used: Python, LangChain, PyTorch, Streamlit, ChromaDB, OpenAI
Tomorrow: Start Project 5 — FastAPI + Railway.app, LeetCode Stack pattern (#232 Implement Queue using Stacks), Job prep continues 🚀
Confidence today: 9/10

## Day 19 - March 27, 2026
Today was a focused job prep day — LinkedIn fully updated and two more Stack problems solved!
1) LeetCode:
Solved #232 Implement Queue using Stacks — third Stack pattern problem.

Key insight: two stacks flip the order — pour Stack1 into Stack2 to get FIFO from LIFO
Only pour when Stack2 is empty — pouring every time would break the order
Extracted repeated logic into helper method move() — clean software engineering approach
empty() checks BOTH stacks with and — queue isn't empty if Stack2 still has items even when Stack1 is empty
Solution was clean and correct on first attempt ✅

2) LinkedIn Updated 💼
Complete profile overhaul for ML/AI Engineer roles:

Headline: "AI/ML Engineer | Python | LangChain | RAG Pipelines | 4 Deployed AI Projects | Open to Work"
About section: highlights 4 deployed projects, MS CS GPA 3.67, open to USA roles
Skills: replaced React/JS skills with ML/AI stack — PyTorch, LangChain, RAG, ChromaDB, NLP, LLMs, Computer Vision etc.
Added all 4 AI projects with live URLs and tech stack descriptions
Turned on Open to Work for ML/AI Engineer, Data Scientist, Python Developer roles in USA

Tools used: Python, LangChain, PyTorch, Streamlit, ChromaDB, OpenAI
Tomorrow: Start Project 5 — Smart URL Content Extractor (FastAPI + BeautifulSoup + GPT-3.5 + Railway.app), LeetCode Stack pattern 🚀
Confidence today: 8/10

## Day 20 - March 28, 2026
Today was Project 5 kickoff — Worked with FastAPI and it's working locally!
1) Project 5 — AI Resume Analyzer (Day 1 of build) 🚀
Set up FastAPI backend from scratch and built two working endpoints:

-> What I built:
   GET / → health check endpoint, confirms API is running
   POST /extract-resume → accepts PDF upload, extracts all text using PyPDF2

-> How the PDF extraction works:
   User uploads PDF
         ↓
   FastAPI receives file via UploadFile
         ↓
   io.BytesIO wraps raw bytes into file-like object
         ↓
   PyPDF2.PdfReader reads all pages
         ↓
   Returns filename, page count, text preview, full text

-> Concepts learned today:
   FastAPI → API framework, faster than Flask, auto-generates /docs
   uvicorn → the server that runs FastAPI (--reload for auto-restart)
   GET vs POST → GET fetches data, POST sends data to server
   Swagger UI → /docs auto-generated by FastAPI, lets you test endpoints directly in browser
   async/await → handles multiple requests simultaneously without waiting
   io.BytesIO → wraps raw bytes to look like a file so PyPDF2 can read it
   Case sensitivity → pypdf2 vs PyPDF2 — Python imports are case sensitive!

Tested successfully:
   Uploaded real resume PDF → API extracted 2 pages of text perfectly ✅
   /docs showing both endpoints with interactive testing ✅

Tech Stack so far: FastAPI, PyPDF2, uvicorn, Pydantic, python-dotenv
Tomorrow: Build job URL scraping endpoint (BeautifulSoup), Build GPT-3.5 analysis endpoint, Connect everything together into full pipeline
Tools used: Python, FastAPI, PyPDF2, uvicorn
Confidence today: 8/10

## Day 21 - March 29, 2026
Today was a massive build day — Project 5 backend is fully complete! 🎉
1)Project 5 — AI Resume Analyzer Backend Complete 🚀
Built a full FastAPI backend with 5 endpoints from scratch:
⭐Endpoints built:
   GET / → health check, confirms API is running
   POST /extract-resume → accepts PDF upload, extracts all text using PyPDF2
   POST /scrape-job → takes job URL, scrapes with BeautifulSoup, returns clean text
   POST /analyze → takes resume text + job text, GPT-3.5 returns structured analysis
   POST /full-analyze → combines everything in one call — PDF + job URL → complete AI analysis

⭐Full backend pipeline:
   PDF upload → PyPDF2 extracts text
   Job URL → BeautifulSoup scrapes page
   Both → GPT-3.5 analyzes → JSON response
   What GPT-3.5 returns:
   json{
     "match_score": 80,
     "strengths": [...],
     "missing_skills": [...],
     "suggestions": [...],
     "summary": "..."
   }
⭐New concepts learned today:
   FastAPI → modern Python API framework, faster than Flask, auto-generates /docs (Swagger UI)
   uvicorn → server that runs FastAPI, --reload auto-restarts on code changes
   GET vs POST → GET fetches data, POST sends data to server
   async/await → handles multiple requests simultaneously without blocking
   UploadFile + File(...) → how FastAPI receives uploaded files
   Form(...) → required when sending files + text together in one request
   io.BytesIO → wraps raw bytes into file-like object so PyPDF2 can read it
   BeautifulSoup → parses HTML, removes script/style/nav tags, extracts clean text
   User-Agent header → makes requests look like real browser to avoid being blocked
   Structured output → telling GPT exact JSON format to return makes parsing reliable
   Pydantic → validates incoming data automatically
   Swagger UI → /docs auto-generated by FastAPI, lets you test all endpoints in browser

⭐Known issue to fix tomorrow:
   Scraper sometimes grabs sidebar content instead of actual job description. 
   Fix: target specific HTML containers like main, article, divs with "job-description" class.

Tomorrow:
Fix scraper, Complete Streamlit frontend, Deploy backend to Railway.app, Deploy frontend to Streamlit Cloud

Tools used: Python, FastAPI, PyPDF2, BeautifulSoup, OpenAI GPT-3.5, Pydantic, uvicorn
Confidence today: 8/10

## Day 22 - March 30, 2026
Today was a MASSIVE day — Project 5 fully built and deployed! First full-stack AI app with separate backend and frontend deployments! 🎉
⭐Project 5 — AI Resume Analyzer COMPLETE 🚀
What it does:
Upload your resume PDF + paste any job description → AI gives instant match score, strengths, missing skills and suggestions powered by GPT-3.5.
Full pipeline:
User uploads PDF + pastes job description
        ↓
Streamlit frontend (Streamlit Cloud)
        ↓
FastAPI backend (Railway.app)
        ↓
PyPDF2 extracts resume text
BeautifulSoup scrapes job URL
GPT-3.5 analyzes both together
        ↓
Returns match score, strengths,
missing skills, suggestions ✅
Backend — FastAPI on Railway.app:

⭐5 endpoints: health check, PDF extraction, job scraping, analysis, full analysis
Scraper targets main content using <main>, <article>, job-description divs
Improved prompt with CRITICAL INSTRUCTIONS — tells GPT to look everywhere in resume
Form(...) for receiving files + text together in one request
job_text_override — paste text directly when URL scraping fails

⭐Frontend — Streamlit on Streamlit Cloud:
Professional clean UI — light background, blue accents, card shadows
Radio button outside form → switches between URL and paste text instantly
Color coded match score — green (70%+), orange (50-70%), red (below 50%)
Strengths, missing skills, suggestions displayed in clean cards

⭐Deployment — two separate platforms:
Backend → Railway.app (FastAPI needs always-on server)
Frontend → Streamlit Cloud (Streamlit's native platform)
Connected via Railway public URL in frontend requests

Bugs fixed today:
Form(...) → required when sending files + text together
Radio button inside form → moved outside so UI updates instantly
Missing /full-analyze in Railway URL → Method Not Allowed error
match_score returned as string → wrapped with int() to fix NameError
job_text_override → added to backend so paste text works properly

Live URLs:

🔧 Backend: [https://web-production-48a5b.up.railway.app]
🎨 Frontend: [https://ai-resume-analyzer-frontend-studcmhielp9u7jq46lwsz.streamlit.app]

New skills learned:
Railway.app → deploy FastAPI backend, environment variables, Procfile
Procfile → tells Railway how to start server (uvicorn main:app --host 0.0.0.0 --port $PORT)
Two deployment architecture → backend and frontend on separate platforms talking via API
int() conversion → GPT sometimes returns numbers as strings

Tools used: Python, FastAPI, PyPDF2, BeautifulSoup, OpenAI GPT-3.5, Streamlit, Railway.app, Pydantic, uvicorn
Tomorrow: LeetCode Stack pattern, update resume + LinkedIn with Project 5, quiz on Projects 4 & 5 🚀
Confidence today: 8/10

## Day 23, March 31, 2026
Short day but a meaningful one.
1) Job Applications:
Spent the morning actively applying for AI/ML roles. Sent out multiple applications with tailored cover letters across roles including AI Automation Engineer, Junior AI Developer, and LLM Engineer positions. Each cover letter was customized to the specific job description — mapping projects directly to requirements rather than sending generic applications.
2) LeetCode:
#121 Best Time to Buy and Sell Stock — Greedy/Sliding Window pattern.
Tracked two variables — running minimum price and maximum profit — in a single O(n) pass. Key insight: using the global minimum fails because it doesn't respect the constraint that you must buy before you sell. The running minimum naturally enforces order.
Also hit a motivational wall today. Pushed through it, solved one problem, and proved myself wrong. Sometimes one small win is enough to reset momentum.
Confidence today: 6/10 — Tough mentally but kept the streak alive. 

## Day 24, April 1, 2026

**LeetCode:**
#53 Maximum Subarray — Kadane's Algorithm!

Key insight: At each element make one decision. Extend current subarray or start fresh. If current sum goes negative, starting fresh wins.

Implemented in O(n) single pass using:
max(num, current_sum + num)

Handled all-negative edge case correctly by
initializing with nums[0] instead of 0. ✅

**Job Applications:**
Actively applying to AI/ML roles on LinkedIn.
Building application volume consistently.

**Confidence today: 7/10**

## Dev Log — Day 25, April 2, 2026
1) LeetCode:
#150 Evaluate Reverse Polish Notation(Stack pattern)
Key insight: numbers go onto the stack, operators pop two operands and push the result back. Order of popping matters. Second pop is the left operand, first pop is the right operand. Used int(a/b) instead of // to correctly truncate toward zero for negative numbers.
2) Revision:
Reviewed concepts from previous projects: reinforcing understanding of RAG pipelines, agent architecture, and production deployment patterns.
Confidence today: 7/10

## Day 26 - April 3, 2026
Solid LeetCode day — two HashMap problems solved with optimized approaches
1) LeetCode:
#1512 Number of Good Pairs

Brute force first (commented out) → O(n²) nested loop counting matching pairs
Optimized with HashMap → O(n) single pass
Key insight: if a number appears n times, the number of pairs = n*(n-1)/2 (combinations formula)
Example: if 2 appears 4 times → 4*3/2 = 6 pairs 

2) #169 Majority Element

Used HashMap to count frequency of each number
Tracked running maximum frequency
Returned element as soon as its count exceeds len(nums)/2
Key insight: majority element appears more than n/2 times — first element to cross that threshold is the answer 

Confidence today: 8/10

## Day 27 - April 4, 2026
Good day today — solved two LeetCode problems and studied some important ML theory that I've been meaning to revisit.
1) LeetCode:
#2325 Decode the Message
Built a character mapping dictionary from the key to the alphabet. Used chr(97) to start from 'a' and increment for each new unique character I found. Skipped spaces when building the mapping, then decoded the message character by character.
Key insight: chr(97) = 'a', chr(98) = 'b' — ASCII values make character mapping really clean.
#771 Jewels and Stones
Looped through stones and checked if each stone matched a jewel. Used a HashMap to track counts and incremented the total whenever there was a match.
Key insight: checking if i in jewels works directly on a string, but using HashMap makes lookup O(1). 
Both problems used the same HashMap character frequency/mapping pattern — it's starting to feel natural now.
2) ML Theory revisited — Overfitting, Underfitting & Bias-Variance Tradeoff:
Today I revised overfitting vs underfitting and the bias-variance tradeoff:
Overfitting vs Underfitting:
Underfitting → model is too simple, performs badly on both train and test data
Overfitting → model is too complex, performs great on training data but fails on test data

Bias-Variance Tradeoff:
Bias → error from wrong assumptions, model too simple, misses real patterns
Variance → model too sensitive to training data, memorizes noise
Total Error = Bias² + Variance + Irreducible Error
The goal is always to find the sweet spot where total error is minimized

The bullseye analogy really helped me understand it:
Low Bias + Low Variance  → hits bullseye consistently 
High Bias + Low Variance → consistent but always wrong
Low Bias + High Variance → scattered, unpredictable
High Bias + High Variance → worst case

How to fix each:
High Bias → more features, complex model, train longer
High Variance → more data, regularization (L1/L2), dropout

Confidence today: 7.5/10

## Day 28 - April 5, 2026
Short day but kept the streak alive! 
1) LeetCode:
#205 Isomorphic Strings
This one was interesting. The key was realizing I needed TWO hashmaps, not one. One mapping from s → t and another from t → s.
Why two? Because with just one direction, "badc" and "baba" would incorrectly return True. The reverse mapping catches cases where two different characters in s try to map to the same character in t.
Used zip(s, t) to iterate both strings simultaneously — clean approach.
Key insight: both mappings must be consistent. If a character is already mapped, it must map to the same character every time. If it maps to something different → not isomorphic, return False immediately. 
What I learned today:
Bidirectional HashMap mapping is a pattern I'll see again — whenever a problem needs a one-to-one relationship between two things, two hashmaps are usually the clean solution.
Confidence today: 7/10

## Day 29 - April 6, 2026
Productive day — LeetCode, job applications, and ML theory! 
1) LeetCode: #645 Set Mismatch
Really elegant solution once I saw it. Used the math trick — if I know what the sum SHOULD be and what the sum actually IS, I can find both the duplicate and the missing number in one go.

actual_sum - set_sum → gives the duplicate (extra value being counted twice)
expected_sum - set_sum → gives the missing number

Key insight: set(nums) removes duplicates, so comparing sum(set(nums)) vs sum(nums) immediately reveals the duplicate. And comparing against the expected sum n*(n+1)//2 reveals the missing number. No loops needed beyond the built-ins! ✅
This felt more like a math problem than a coding problem — and I love when that happens.
2) Job Applications:
Continued applying to AI/ML roles on LinkedIn. Building application volume consistently.
3) ML Theory — Evaluation Metrics (Beyond Accuracy):
Today I learned why accuracy alone can be a liar. If 99% of my data is Class A, a model that always guesses A is 99% accurate — but completely useless. That really clicked for me.
What I studied:
Precision vs Recall:

Precision → of everything I predicted as positive, how many were actually positive? 
Recall → of all actual positives, how many did I catch? 
The tradeoff: improving one usually hurts the other
Example: in medical diagnosis, missing a sick patient (low recall) is far worse than a false alarm (low precision)

F1-Score:

Harmonic mean of Precision and Recall
Better than accuracy when data is imbalanced
Punishes models that are extremely good at one but terrible at the other

ROC-AUC:

Plots True Positive Rate vs False Positive Rate at different thresholds
AUC = area under that curve → closer to 1.0 = better model
Useful for comparing models regardless of threshold

Connection to my projects:

Project 1 (Movie Sentiment) → my dataset was balanced (25k positive, 25k negative) so accuracy was fair to use. If it was imbalanced, I'd need F1-Score instead!
In real healthcare or fraud detection projects → always use Precision, Recall and F1, never just accuracy

Confidence today: 7.5/10

## Day 30 - April 7, 2026
Hit the 30-day mark today! 🎉 Half way through the 60-day journey and still going strong.
1) Job Applications:
Continued applying to AI/ML roles actively. Building application volume consistently — focusing on Tier 1 companies where my projects speak louder than LeetCode scores.
2) SQL:
Began learning SQL today using SQLite with Python. Covered the fundamentals:

What I learned:
What a database is — like an Excel sheet with rows and columns
conn → connection to the database (the handshake)
cursor → the messenger that runs queries and fetches results
What practice.db is — SQLite stores everything in one single file, no server needed
Why .db files look like gibberish in text editors — they're binary files, not plain text

Queries I practiced:
sql-- Get everything
SELECT * FROM employees;

-- Filter with WHERE
SELECT * FROM employees
WHERE department = 'AI Engineering';

-- Conditions
WHERE salary > 90000
WHERE department = 'AI Engineering' AND city = 'Dallas'
WHERE city = 'Dallas' OR city = 'Austin'

-- Specific columns only
SELECT name, salary FROM employees
WHERE salary > 90000;
Key insights:

Indentation doesn't matter in SQL — it's only for human readability
* : means all columns
WHERE filters rows — only returns rows that match the condition
Train-test split doesn't cause overfitting/underfitting — it's the tool to detect it

Tomorrow:
Continue SQL — ORDER BY, LIMIT, GROUP BY, JOINs
LeetCode — get back on track with Trees pattern
Job applications

Confidence today: 8/10 

## Day 31 - April 8, 2026
What I did today:
1) Solved LeetCode #645 — Set Mismatch
2) Applied to a few jobs
3) Rest day after 30 days of intense sprinting

-> LeetCode #645 — Set Mismatch
Used a set to track seen numbers, found the duplicate by checking if a value already existed in the set, then found the missing number by iterating 1 to n and checking what wasn't in the set.
Time complexity: O(n)
Space complexity: O(n) — set stores up to n elements
What I understood:
Sets give O(1) lookup which makes duplicate detection efficient
Two separate passes — one to find duplicate, one to find missing
Clean separation of concerns

Honest reflection:
Tired day after 30 days of non-stop building. Kept the streak alive anyway. That matters more than the problem difficulty today.
Streak: 31 days ✅
Confidence today : 6/10

## Day 32 — April 9, 2026

### Today's Progress
- Solved 4 LeetCode problems  
- Completed interview prep session  

### LeetCode Problems
- **#2114 — Maximum Number of Words in Sentences**  
  Iterated through sentences, split by spaces, and tracked the maximum word count.

- **#771 — Jewels and Stones**  
  Used a set for O(1) lookups to efficiently count matching characters.

- **#1108 — Defanging IP Address**  
  Iterated through the string and replaced "." with "[.]".

- **#2011 — Final Value After Operations**  
  Parsed each operation and incremented/decremented a counter accordingly.

### Interview Prep
Continued structured preparation for technical interviews (AI/ML + SWE roles).

### Reflection
**Lesson learned:** Keep going until you reach the end.  
**Confidence level:** 8/10

## Day 33 - April 10, 2026
Today's Progress:

->Solved LeetCode #242 — Valid Anagram
->Applied for jobs**
->Developed targeted application strategy

LeetCode #242 — Valid Anagram
Used a hashmap to track character frequencies. Iterated through both strings, compared counts to determine if they're anagrams.
Approach: O(n) time | O(n) spac
Application Strategy:
Developed a targeted strategy for specific companies — focusing on role alignment and tailoring approach accordingly.
COnfidence: 8/10

## Day 34 - April 11, 2026
Today's Progress:

Solved LeetCode #347 — Top K Frequent Elements

LeetCode #347 — Top K Frequent Elements
Used a hashmap to count frequencies, then a min-heap of size k to efficiently track the top k elements. When heap exceeds k, pop the minimum frequency element.
Time: O(n log k) | Space: O(n)
Key concepts applied: defaultdict, heapq, min-heap pattern for top-k problems.
Confidence: 8/10
