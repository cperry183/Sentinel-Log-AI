# Sentinel-Log-AI: Neural Anomaly Detection for SRE

### Project Overview
As an SRE with 12+ years of experience, I’ve managed clusters of 450+ hosts. This project 
replaces static, rule-based log monitoring with a **Transformer-based (BERT)** Natural Language Processing model to identify system anomalies.

### Why This Matters
Traditional tools use regex for "known" errors. This tool uses **Masked Language Modeling** to understand the *semantic* meaning of logs, catching "unknown-unknowns" that indicate 
security breaches or hardware failures.

### Key AI Concepts Used
* **Tokenization:** Processing raw syslog strings into numerical tensors.
* **Inference:** Utilizing a pre-trained BERT model for sequence classification.
* **Softmax Activation:** Determining the probability of a log being "Normal" vs. "Anomaly."

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run analysis: `python src/main.py`
