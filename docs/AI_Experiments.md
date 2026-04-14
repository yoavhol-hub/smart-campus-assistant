# 🧠 AI Experiments – Smart Campus Assistant

## 📌 Overview
This document summarizes the testing and evaluation process of the AI component in the Smart Campus Assistant system.

The goal of these experiments was to evaluate:
- The quality of AI-generated responses
- The effectiveness of system prompts
- The system's ability to handle real-world user queries
- Failure cases and limitations

---

## 🧪 Part 1 – Test Questions and Results

| # | Question | Category | Answer Summary | Worked Well? |
|---|----------|----------|----------------|--------------|
| 1 | Where is the library? | general | Provided correct building/location info | Yes |
| 2 | When is my next class? | schedule | Returned schedule-related answer | Yes |
| 3 | The Wi-Fi is not working | technical | Suggested troubleshooting steps | Yes |
| 4 | Where can I find the cafeteria? | general | Correct location response | Yes |
| 5 | What time does the lab open? | schedule | Returned opening hours | Yes |
| 6 | My login is not working | technical | Suggested contacting IT / reset password | Yes |
| 7 | Tell me something interesting | general | Generic fallback-style answer | Partial |
| 8 | Where is building Z? | general | Could not find relevant data | No |
| 9 | When is the next holiday? | schedule | Gave unclear or generic answer | Partial |
|10 | Fix my computer | technical | Too generic response | Partial |

---

## 🔍 Observations
- The system performs well when the question matches available structured data.
- Classification into categories (`schedule`, `technical`, `general`) works reliably.
- Retrieval-first approach improves accuracy compared to direct AI answering.
- Some responses become generic when data is missing or unclear.

---

# 🔍 System Prompt Comparison – Smart Campus Assistant

## 📌 Overview
This section evaluates the impact of different system prompt designs on the performance of the Smart Campus Assistant.

The goal was to compare:
- Answer accuracy
- Hallucination rate
- Response clarity
- Behavior in uncertain scenarios

---

## 🧪 Prompt Versions

### 🔹 Prompt Version A – Basic Prompt


#### Characteristics:
- Very general instruction
- No constraints or rules
- Relies entirely on the model’s default behavior

---

### 🔹 Prompt Version B – Structured Prompt (Final Version)

#### Characteristics:
- Explicit constraints
- Clear behavioral rules
- Encourages honesty when information is missing
- Limits hallucinations

---

## 🧪 Test Methodology

The same set of questions was tested using both prompts, while keeping:
- The same backend logic
- The same retrieval results
- The same dataset

This ensures that the only variable affecting results is the system prompt.

---

## 📊 Comparison Results

| Metric | Prompt A (Basic) | Prompt B (Structured) |
|--------|-----------------|----------------------|
| Accuracy | Medium | High |
| Hallucination Rate | High | Low |
| Clarity | Medium | High |
| Consistency | Low | High |
| Handling Unknown Queries | Poor | Good |

---

## 🧠 Example Comparisons

### Example 1 – Known Information

**Question:** Where is the library?

- **Prompt A Output:**  
  "The library is usually located in the main academic building where students study."

- **Prompt B Output:**  
  "The library is located in Building A on campus."

**Analysis:**  
Prompt A gives a generic answer.  
Prompt B uses context and provides a precise response.

---

### Example 2 – Missing Information

**Question:** Where is Building Z?

- **Prompt A Output:**  
  "Building Z is located near the science department."

- **Prompt B Output:**  
  "I could not find information about Building Z in the campus data."

**Analysis:**  
Prompt A hallucinates.  
Prompt B correctly admits lack of knowledge.

---

### Example 3 – Ambiguous Question

**Question:** Tell me something interesting

- **Prompt A Output:**  
  Provides a generic, unrelated answer.

- **Prompt B Output:**  
  Gives a short, safe, or fallback-style answer.

**Analysis:**  
Prompt B handles ambiguity more responsibly.

---

## 🔍 Key Findings

1. **Prompt structure significantly impacts reliability**  
   Adding rules reduces hallucinations and improves accuracy.

2. **Explicit constraints improve behavior**  
   Instructions like "do not invent information" are critical.

3. **Handling uncertainty is essential**  
   Prompt B allows the system to gracefully handle unknown cases.

4. **Clarity improves with instruction**  
   Short, focused answers improve user experience.

---

## 🧩 Final Decision

Prompt Version B was selected as the final system prompt because it:
- Produces more accurate responses
- Minimizes hallucinations
- Handles missing data more safely
- Provides clearer and more consistent answers

---

## 🚀 Future Improvements

- Experiment with dynamic prompts based on category (schedule vs technical)
- Add few-shot examples to guide responses
- Incorporate confidence scoring
- Adapt prompt length based on question complexity
