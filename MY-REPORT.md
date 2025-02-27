# Comparative Analysis of Prompt Engineering Techniques for Software Requirement Extraction

![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

Project Summary

This research explores the effectiveness of various prompt engineering techniques—such as Zero-Shot, Few-Shot, Chain-of-Thought, Meta-Prompting, Retrieval-Augmented Generation (RAG), Prompt Chaining, Self-Consistency, and Knowledge Generation—in improving the accuracy, completeness, and efficiency of software requirement extraction using Large Language Models (LLMs). We analyze how different prompting strategies impact requirement structuring and explore optimizations to enhance AI-driven requirement analysis.

Authors: [Sai Nikhith Atmakuri,Siva Satya Sai Ram Toleti, Venkata Ganesh Padavala ]
Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

---

# Research Question

How can different prompt engineering techniques improve the completeness, accuracy, and efficiency of extracting software requirements using LLMs?

This research investigates whether structured prompting methods can generate high-quality software requirements with minimal human intervention. 🚀

---

Arguments

What is already known about this topic

Traditional software requirement gathering relies on manual effort, which is time-consuming and prone to misinterpretation.
LLMs have been explored for requirement analysis, but prompt design significantly affects the quality of the extracted information.
Different prompt engineering techniques exist**, including Zero-Shot, Few-Shot, Chain-of-Thought, Meta-Prompting, Self-Consistency, RAG, Prompt Chaining, and Knowledge Generation, each with strengths and weaknesses.
Challenges include hallucination, inconsistency in responses, and the need for domain-specific fine-tuning.

What this research is exploring

We experiment with various prompting strategies to assess their effectiveness in structured requirement extraction.
We are building a benchmarking framework to compare prompt performance using accuracy, completeness, and response consistency as evaluation metrics.
We are exploring how model parameters like temperature, token limits, and instruction format impact requirement generation.

Implications for practice

Automating software requirement documentation** to reduce manual workload.
Improving accuracy and completeness** of AI-generated requirements, minimizing ambiguities in software development.
Optimizing LLM response efficiency** to balance quality and processing time.

---

Research Method

1. Experimental Setup

Datasets: Using real-world software requirement documents and generating synthetic test cases.
Prompt Engineering Techniques:
  Zero-Shot: Directly asking the LLM to generate requirements without examples.
  Few-Shot: Providing sample requirements as references before prompting.
  Chain-of-Thought: Guiding the model through a step-by-step reasoning process to refine requirement extraction.
  Meta-Prompting: Creating prompts that instruct the model on how to generate effective responses.
  Self-Consistency: Running multiple LLM queries and aggregating the most consistent responses.
  Retrieval-Augmented Generation (RAG): Enhancing requirement extraction by incorporating external knowledge retrieval.
  Prompt Chaining: Using intermediate steps to structure multi-step requirement extraction workflows.
  Knowledge Generation: Enabling LLMs to iteratively build structured requirement knowledge through multi-turn reasoning.

2. Metrics for Evaluation

Accuracy: How well the generated requirements align with predefined correct requirements.
Completeness: Whether all critical aspects of a software requirement are covered.
Consistency: Measuring variation in responses for the same prompt over multiple trials.
Efficiency: Response time and computational resource usage.

3. Implementation Approach

Jupyter Notebooks in the `prompt-eng` repository will document all experiments.
Comparing model outputs across various LLM configurations (temperature, token length, and prompt format variations).
Logging results in structured tables and visualizing differences using charts and graphs.


Results

Key Findings from Experiments

| Technique             | Accuracy   | Completeness | Consistency | Efficiency |
|----------------------|-----------|-------------|-------------|------------|
| **Zero-Shot**       | Medium    | Low         | High        | High       |
| **Few-Shot**        | High      | Medium      | Medium      | Medium     |
| **Chain-of-Thought**| High      | High        | Medium      | Low        |
| **Meta-Prompting**  | High      | High        | High        | Medium     |
| **Self-Consistency**| Very High | Very High   | High        | Low        |
| **RAG**            | Very High | High        | High        | Medium     |
| **Prompt Chaining** | High      | Very High   | High        | Medium     |
| **Knowledge Generation** | Very High | Very High | High | Medium |

Observations

Zero-Shot Prompting is efficient but struggles with completeness.
Few-Shot Prompting improves contextual accuracy but requires curated examples.
Chain-of-Thought enhances logical reasoning, leading to better-structured requirements.
Meta-Prompting and Self-Consistency provide the highest accuracy but demand additional processing time.
Retrieval-Augmented Generation (RAG) improves completeness by integrating external knowledge sources.
Prompt Chaining optimizes multi-step requirement extraction workflows for structured outputs.
Knowledge Generation builds a more refined and detailed requirement set over iterative reasoning.

---

Future Research Directions
Automated prompt optimization using AI-based prompt tuning strategies.
Hybrid models combining multiple prompting techniques to achieve the best trade-off between accuracy and efficiency.
Domain-specific adaptations for requirement extraction in finance, healthcare, and IoT systems.
Integration with Retrieval-Augmented Generation (RAG) for knowledge-enhanced requirement analysis.
Comparative analysis with human-written requirements to validate real-world usability.


