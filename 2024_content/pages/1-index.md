Title:
Date: 2025-07-18
save_as: index.html

<!-- <h4>News</h4>

<div class="row">
<div class="alert alert-success" role="alert">
<p> [2024/09/11] The accepted papers are now available on <a href="https://openreview.net/group?id=KDD.org/2024/Workshop/KDD_Cup_CRAG">OpenReview</a>.</p>
<p> [2024/09/07] Slides of the workshop are <a href="/pages/schedule.html"> available</a>.</p>
<p> [2024/07/30] The paper submission deadline has been extended to Aug 09 2024 11:59PM UTC-0.</p>
<p> [2024/07/29] We are excited to announce <a href="https://discourse.aicrowd.com/t/meta-crag-challenge-2024-winners-announcement/">the winners of the Meta CRAG Challenge 2024</a>.</p>
<p> [2024/06/13] The CRAG paper has been featured by Hugging Face <a href="https://huggingface.co/papers?date=2024-06-10">Daily Papers</a> and covered by several media outlets (<a href="https://www.marktechpost.com/2024/06/11/advancing-reliable-question-answering-with-the-crag-benchmark/">1</a>, <a href="https://analyticsindiamag.com/comprehensive-rag-benchmark-aims-to-advance-retrieval-augmented-question-answering/">2</a>, <a href="https://adasci.org/enhancing-retrieval-augmented-generation-in-nlp-with-crag/">3</a>). </p>
</div>
</div> -->

## 🌟 Introducing the Meta CRAG - MM: Comprehensive RAG Benchmark for Multi-modal, Multi-turn Challenge! 🌟

You're on vacation, strolling through ancient sites as your smart glasses share their history. Later, at a local restaurant, they translate the menu, helping you order with confidence. As the day winds down, you head back to the parking lot—no searching, no stress—your glasses pull up an image reminder of exactly where you parked.

Wearable devices are revolutionising how we communicate, work, and experience the world. But to be truly valuable in everyday life, they must provide relevant, accurate, and reliable information tailored to users' needs.

## 💬 Introduction

Vision Large Language Models (VLLMs) have undergone significant advancements in recent years, empowering multi-modal understanding and visual question-answering (VQA) capabilities behind smart glasses. Despite the progress, VLLMs still face a major challenge: generating hallucinated answers. Studies have shown that VLLMs encounter substantial difficulties in handling queries involving long-tail entities [1]; these models also encounter challenges in handling complex queries that require the integration of different capabilities: recognition, OCR, knowledge, and generation [2].

The Retrieval-Augmented Generation (RAG) paradigm has expanded to accommodate multi-modal (MM) input and demonstrated promise in addressing the knowledge limitation of VLLM. Given an image and a question, an MM-RAG system constructs a search query by synthesizing information from the image and the question, searches external sources to retrieve relevant information, and then provides grounded answers to address the question [3]

<img src="/images/MM-RAG.png"  width="600">

**Figure 1**: MM-RAG


Despite its potential, MM-RAG still faces many challenges, such as recognizing the correct subject and comprehending the visual context in the image to understand the question, performing effective searches to retrieve useful information, synthesizing information from different sources to generate coherent and informative answers, and engaging in smooth multi-turn conversations. A comprehensive benchmark that provides a standardized framework and clear metrics is in pressing need to enable reliable and informative assessment of MM-RAG systems to facilitate and advance innovations.

---

## 💻 What is CRAG - MM: Comprehensive RAG Benchmark for multi-modal multi-turn question answering?

CRAG-MM is a visual question-answering benchmark that focuses on factual questions, offering a unique collection of image and question-answering sets to enable comprehensive assessment of wearable devices. Specifically, CRAG-MM features a diverse collection of **5k images**, including **3k egocentric ones** captured by **RayBan Meta smart glasses**, covering **13 domains** and reflecting real-world challenges associated with handling egocentric images.

The benchmark includes **4 types of questions**, ranging from simple queries that can be answered by looking at the image only to complex ones that require retrieving information from multiple sources and performing reasoning.

Moreover, CRAG-MM encompasses both **single-turn and multi-turn conversations**, providing a more overarching evaluation of MM-RAG solutions.

---

## 📅 Timeline

There will be two phases in the challenge.

**Phase 1** will be open to all teams who sign up.
All teams that have at least one successful submission in Phase 1 can enter Phase 2.

### Phase 1: Open Competition

- **Website Open, Sample data available and Registration Begin**: March 6, 2025, 23:55 UTC
- **Data Available**: March 15, 2025, 23:55 UTC
- **Warm-up Round Start Date**: March 24, 2025, 23:55 UTC
- **Phase 1 Submission Start Date**: April 4, 2025, 23:55 UTC
- **Phase 1 Submission End Date**: May 17, 2025, 23:55 UTC

### Phase 2: Competition for Top Teams

- **Phase 2 Start Date**: May 26, 2025, 23:55 UTC
- **Registration and Team Freeze Deadline**: June 1, 2025, 23:55 UTC
- **Phase 2 End Date (Extended)**: Jun 17, 2025, 23:55 UTC

### Winners Announcement

- **Winner Notification**: July 1, 2025 (Tentative)
- **Winner Public Announcement**: August 5, 2025 (At KDD Cup Winners event)

---

## 🏆 Prizes

The challenge boasts a prize pool of **USD 33,000**. There are prizes for **all three tasks**.

### Grand Prize 💎

- **The top one team that gains the highest score for egocentric images**: $5000

### For Each Task

- 🥇 **First Place**: $4,000
- 🥈 **Second Place**: $2,500
- 🥉 **Third Place**: $1,500

### Special Awards 💐

- **First Place for each of the 4 question types**: $1000

*The first, second, and third prize winners are not eligible to win prizes for complex question types.*

---

## 💻 META CRAG - MM Challenge

An MM-RAG QA system takes as input an image 𝐼 and a question 𝑄, and outputs an answer 𝐴; the answer is generated by MM-LLMs according to information retrieved from external sources, combined with knowledge internalized in the model. A **Multi-turn MM-RAG QA system**, in addition, takes questions and answers from previous turns as context to answer new questions. The answer should provide useful information to answer the question without adding any hallucination.

We first define **four types of questions** in our benchmark:

- **Simple questions**: Questions asking for simple facts.
    - **Simple recognition**: This can be directly answered from the image (e.g., "What brand is the milk?" or "Who wrote this book?" where the brand name and the book author are shown on the image).
    - **Simple knowledge**: Requires external knowledge for the answers (e.g., "What’s the price of this sofa on Amazon?").
- **Multi-hop questions**: Questions that require **chaining multiple pieces of information** to compose the answer (e.g., "What other movies have the director of this movie directed in the past?").
- **Comparison and Aggregation questions**: Questions requiring **aggregating or comparing multiple pieces of information** (e.g., "Which drinks do not contain added sugar among these?" or "Is this cheaper on Amazon?").
- **Reasoning questions**: Questions about an entity that **cannot be directly looked up** and require **reasoning** to answer (e.g., "Can the dryer be used in Europe?" where the image shows a dryer).

We designed **three competition tasks**. As shown in Figure 2, **Task #1** and **Task #2** contain single-turn questions, where the former provides **image-KG-based retrieval**, and the latter additionally introduces **web retrieval**; Task #3 focuses on **multi-turn conversations**.

Here, we provide the content that can be leveraged in QA to ensure fair competition. We describe how we generated the data in the next section.

---

### 🏹 Challenge Tasks
This challenge comprises of three tasks designed to improve multimodal question-answering (QA) systems.

**TASK #1**: SINGLE-SOURCE AUGMENTATION

- **Goal**: To test the **basic answer generation capability** of MM-RAG systems.
- Provides an **image mock API** to access information from an underlying **image-based mock KG**. The **mock KG** is indexed by the image and stores structured data associated with the image. Answers to the questions **may or may not exist** in the mock KG. The **mock API** takes an image as input and returns similar images from the **mock KG**, along with **structured data** associated with each image to support answer generation.

**TASK #2**: MULTI-SOURCE AUGMENTATION

- **Goal**: To test how well the **MM-RAG system synthesizes information** from **different sources**.
- In addition to **Task #1**, this task provides a **web search mock API** as a **second retrieval source**. The **web pages** may provide **useful information** for answering the question but **also contain noise**.


**TASK #3**: MULTI-TURN QA

- **Goal**: To test **context understanding** for **smooth multi-turn conversations**.
- This task tests the system’s ability to conduct **multi-turn conversations**. Each conversation contains **2–6 turns**. Except for the first turn, **questions in later turns may or may not require the image** for answering.

The three tasks, each building upon the previous one, **guide competition teams to build end-to-end RAG systems** for **multi-modal, multi-turn QA**.

<img src="/images/tasks-mm.jpeg"  width="600">

**Figure 2**: CRAG - MM Tasks

---

### 💯 Evaluation Metrics

We adopt exactly the **same metrics and methods** used in the **CRAG competition** to assess the performance of **MM-RAG systems**. Below is a brief description of the evaluation criteria.

**SINGLE-TURN QA**

For each question in the evaluation set, the answer is scored as:

- ✅ **Perfect**(fully correct) → **Score: 1.0**
- ⚠️ **Acceptable** (useful but with minor non-harmful errors) → **Score: 0.5**
- ❓ **Missing**: (e.g., “I don’t know”, “I’m sorry I can’t find …”) → **Score: 0.0**
- ❌ **Incorrect**: (wrong or irrelevant answer) → **Score: -1.0**
- **Truthfulness Score**: The **average score** across all examples in the evaluation set for a given MM-RAG system.

**MULTI-TURN QA**

There is not a dominant way to evaluate answer quality for multi-turn conversations. We adapt the method in [5], which is closest to the information-seeking flavor of conversations (in contrast to task fulfilling). In particular, we stop a conversation when the answers in two consecutive turns are wrong and consider answers to all remaining questions in the same conversation as missing–mimicking the behavior of real users when they lose trust or feel frustrated after repeated failures. We then take the average score of all multi-turn conversations.

---

### 🖊 Evaluation Techniques

- **Auto-evaluation** is used to display scores on the **leaderboard**.
- In the **final round**, the **top-10 teams** are selected via auto-evaluation.
- **Manual annotations** determine the **final top teams** for each task.

**Performance Constraints:**

- **Only answer texts generated within 30 seconds are considered.**
- **10-second timeout per turn** is strictly enforced.
- **Human evaluation reviews** the full response for validity and hallucination.
- **Automatic evaluation** scores only the **first 75 BPE tokens.**
- **Full responses** are checked manually for **hallucination**.

---

### 📙 Evaluation Details

- **All missing answers** should return a standard response: `"I don't know."`
- Every query is associated with a **query time** (when the query was made).
- **Dynamic questions** may have different correct answers depending on query time.
- **Ground truth answers** are correct at the time the data was collected.

---

## 📊 CRAG-MM Dataset Description

CRAG-MM contains **three parts**:

- The Image Set
- The QA Set
- Retrieval Contents

#### 🖼️ Image Set

CRAG-MM contains **two types of images**:

- **Egocentric images**: Captured using **Ray-Ban Meta Smart Glasses**.
- **Normal images**: Collected from **public sources**.

#### 📝 Question Answer Pairs

- Covers **13 domains**, including **Books, Food, Math & Science, Shopping, Animal, Vehicles, and more**.
- Includes **4 types of questions: Simple-recognition and Simple-knowledge, Multi-hop, Comparison and Aggregation, Reasoning**.
- Contains **both single-turn and multi-turn conversations**.

#### 📁 Retrieval Contents

**Image Search**

- A **mock image search API** takes an image as input.
- Returns **similar images with structured metadata** from a **mock KG**.
- Example: Querying with a **landmark image** returns similar images **with metadata**.

**Text-Based Web Search**

- A **text search API** takes a text query as input.
- Returns **relevant web pages** (URLs, page titles, snippets, last updated time).

Both APIs include **hard negative data** to **simulate real-world challenges**.

---

## 📘 Submission and Participation

Participants must submit their code and model weights to run on the host's server for evaluation.

### 🧭 Model

This KDD Cup requires participants to use Llama models to build their RAG solution. Especially, participants can use or fine-tune the following Llama 3 models from https://llama.meta.com/llama-downloads:
- Llama 3.2 11B
- Llama 3.2 90B

Any other non-llama models used need to be under 1.5b parameter size limit.

### 🔨 Hardware and system configuration

We set a limit on the hardware available to each participant to run their solution. Specifically,

All submissions will be run on a single G6e instance with a NVIDIA L40s GPU with 48GB of GPU memory on AWS. Please note that:
- Llama 3.2 11B in full precision can run directly.
- Llama 3.2 90B in full precision cannot be directly run on this GPU instance. Quantization or other techniques need to be applied to make the model runnable.
- NVIDIA L40s is not using the latest architectures and hence might not be compatible with certain acceleration toolkits, so please make sure the submitted solution is compatible with the configuration.

Moreover, the following restrictions will also be imposed:
- The network connection will be disabled.
- Each turn in a submission has a strict 10-second timeout. If the model times out during any turn, the entire submission will be considered failed. For submissions made via the batch generation interface, the permitted time is calculated as batch size multiplied by 10 seconds per batch.
- In human evaluation, graders will assess the entire response to determine both answer validity and hallucination. In automatic evaluation, responses will be truncated to the first 75 BPE tokens for scoring purposes.
- Phase 2 submissions will be evaluated on low-resolution (960 width, 1280 height) egocentric images to mimic a real-world challenge. Resolution of normal images remains unchanged.
- To accommodate the expanded test set in Round 2, the maximum allowed evaluation time per submission has been increased from 4 hours to 7.5 hours. Submissions exceeding this limit will be terminated automatically.

### 🤝 Use of external resources

By only providing a small development set, we encourage participants to exploit public resources to build their solutions. However, participants should ensure that the used datasets or models are publicly available and equally accessible to use by all participants. Such a constraint rules out proprietary datasets and models by large corporations. Participants are allowed to re-formulate existing datasets (e.g., adding additional data/labels manually or with Llama models), but award winners are required to make them publicly available after the competition.

### 🔑 Baseline implementation

We provide users with three baseline models to help get started. Detailed implementations of these baseline models are accessible through the links provided below. Please refer to [this page](https://github.com/facebookresearch/CRAG/blob/main/docs/download_baseline_model_weights.md) for steps to download (and check in) the models weights required for the baseline models, and refer to the inline documentation for implementation guide and further details.

1. [**Vanilla Llama 3 Model**](https://github.com/facebookresearch/CRAG/blob/main/models/vanilla_llama_baseline.py).

2. [**RAG Baseline Model**](https://github.com/facebookresearch/CRAG/blob/main/models/rag_llama_baseline.py).

3. [**RAG Knowledge Graph Baseline Model**](https://github.com/facebookresearch/CRAG/blob/main/models/rag_knowledge_graph_baseline.py).

---

## 📘 Participation and Submission

### 🔑 Registration
- **Teams of 1–5 participants** can register on this page before submitting solutions.
- **Team freeze deadline**: June 1, 2025.

### 🤝 Solution Submission
- **Phase I**: Each team can make **6 submissions per week** across **all three tracks**.
- **Phase II**: Each team can make **10 total submissions** across each track per week.

### 💻 Technical Report Submission
Potential winners must submit a **technical report**.
- The report includes a **solution description** + **code for reproducibility**.
- **Compliance with challenge rules is required for winning teams**.

---

## 🏛️ KDD Cup Workshop

The **KDD Cup** is an annual **data mining and knowledge discovery competition** organized by **ACM SIGKDD**.

**KDD Cup 2025** will be held in **Toronto, Canada**.

**Dates**: August 3–7, 2025.

---

## ⛰ What Makes CRAG-MM Standout?

- **The first publicly released wearable benchmarks**: Includes **real-world** challenges from **wearable device QA**.
- **Rich and insightful benchmark**: Covers **diverse** images and questions (e.g., **low-quality images, long-tail entities**).
- **Reliable and fair evaluation**: Equal access to **retrieval resources** (image KG + web corpus).

---

## 📱 Contact

For inquiries, contact:
📧 **crag-kddcup-2025@meta.com**

Organizers of this KDD Cup consists of scientists and engineers from **Meta Reality Labs** and **Meta GenAI**. They are:

• Xiao Yang • Jiaqi Wang • Shervin Ghasemlou • Parth Suresh • Adam Czyzewski • Sanat Sharma • Surya Appini • Haidar Khan • Roy Luo • Ziqiang Guan • Juheon Lee • Prashan Wanigasekara • Lingkun Kong • Sajal Choudhary • Tammy Stark • Chen Zhou • Kai Sun • Shane Moon • Nicolas Scheffer • Zhaleh Feizollahi • Mangesh Pujari • Andrea Jessee • Rakesh Wanga • Rohit Patel • Anuj Kumar • Xin Luna Dong

---

## 🗂️ Related Work

To the best of our knowledge, the Meta CRAG-MM challenge is the first MM-RAG challenge for KDD Cups and broadly. CRAG-MM uniquely features natural uses cases for wearable devices based on egocentric images. Moreover, it encompasses a variety of domains and question types, effectively evaluating different capabilities of MM-RAG systems: entity recognition, OCR, query rewrite, answer generation, and so on. Furthermore, CRAG-MM extends beyond single-turn QA by including multi-turn conversations, a common and critical use case for smart assistant.

---

## 📕 References

[1] Qiu et al., "SnapNTell: Enhancing Entity-Centric Visual Question Answering with Retrieval Augmented Multimodal LLM". Available at: [https://aclanthology.org/2024.findings-emnlp.14/](https://aclanthology.org/2024.findings-emnlp.14/)

[2] Yu et al., "MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities". Available at: [https://arxiv.org/abs/2308.02490](https://arxiv.org/abs/2308.02490)

[3] Gao et al., "Retrieval-Augmented Generation for Large Language Models: A Survey". Available at: [https://arxiv.org/abs/2312.10997](https://arxiv.org/abs/2312.10997)

[4] Yang et al., "CRAG - Comprehensive RAG Benchmark". Available at: [https://proceedings.neurips.cc/paper_files/paper/2024/hash/1435d2d0fca85a84d83ddcb754f58c29-Abstract-Datasets_and_Benchmarks_Track.html](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1435d2d0fca85a84d83ddcb754f58c29-Abstract-Datasets_and_Benchmarks_Track.html)

[5] Bai et al., "MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues". Available at: [https://aclanthology.org/2024.acl-long.401/](https://aclanthology.org/2024.acl-long.401/)

<!-- <hr>
<a href="/pages/organizers.html">Contributors & Acknowledgements</a> -->
