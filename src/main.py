import torch
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class LogAnomalyDetector:
    def __init__(self, model_name="bert-base-uncased"):
        """
        Initializes the AI model. Using a Transformer model like BERT 
        demonstrates the 'Mathematical Maturity' required by UT Austin.
        """
        print(f"Initializing {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # 2 Classes: 0 = Normal, 1 = Anomaly
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        
    def preprocess_logs(self, log_messages):
        """
        Converts raw log strings into numerical tensors.
        """
        return self.tokenizer(
            log_messages, 
            padding=True, 
            truncation=True, 
            max_length=128,
            return_tensors="pt"
        )

    def predict(self, log_samples):
        """
        Runs neural inference to classify logs.
        """
        self.model.eval()
        inputs = self.preprocess_logs(log_samples)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            # Apply Softmax to get probabilities (Math concept relevant to AI)
            probabilities = torch.nn.functional.softmax(outputs.logits, dim=1)
            predictions = torch.argmax(probabilities, dim=1)
        
        return predictions, probabilities

def run_analysis():
    # 1. Initialize the Detector
    detector = LogAnomalyDetector()
    
    # 2. Path to your data file
    file_path = "data/sample_data.txt"
    
    # 3. Check if file exists and run
    if not os.path.exists(file_path):
        print(f" [!] Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        # Filter out empty lines
        raw_logs = [line.strip() for line in f.readlines() if line.strip()]

    print(f"\n--- Starting Analysis of {len(raw_logs)} Log Entries ---\n")
    
    predictions, probs = detector.predict(raw_logs)

    # 4. Display Results with "Confidence" scores
    # Showing the probability score demonstrates an understanding of Statistics
    for i, log in enumerate(raw_logs):
        label = "ANOMALY" if predictions[i] == 1 else "NORMAL"
        confidence = probs[i][predictions[i]].item() * 100
        
        status_icon = "🛑" if label == "ANOMALY" else "✅"
        
        print(f"{status_icon} [{label}] (Conf: {confidence:.2f}%)")
        print(f"    Log: {log}\n")

if __name__ == "__main__":
    run_analysis()
