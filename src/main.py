import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.preprocessing import LabelEncoder

class LogAnomalyDetector:
    def __init__(self, model_name="bert-base-uncased"):
        """
        Initializes the AI model. For a GitHub portfolio, using a 
        Transformer demonstrates modern NLP knowledge.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # We assume 2 classes: 0 = Normal, 1 = Anomaly (Security Threat/System Failure)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        
    def preprocess_logs(self, log_messages):
        """
        Converts raw log strings into tensors the AI can understand.
        """
        return self.tokenizer(
            log_messages, 
            padding=True, 
            truncation=True, 
            return_tensors="pt"
        )

    def predict(self, log_samples):
        """
        Runs inference to detect anomalies.
        """
        self.model.eval()
        inputs = self.preprocess_logs(log_samples)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=1)
        
        results = ["ANOMALY DETECTED" if pred == 1 else "Normal" for pred in predictions]
        return results

# Example Usage for your Portfolio:
if __name__ == "__main__":
    detector = LogAnomalyDetector()
    
    # Mock logs simulating your SRE experience at Harvard/IBM
    raw_logs = [
        "Jan 21 12:00:01 hms-prod-01 systemd: Started Session 123 of user root.",
        "Jan 21 12:05:42 hms-prod-452 sshd: Extreme failure: repeated login attempts from unauthorized IP 192.168.1.50",
        "Jan 21 12:10:10 hms-prod-01 kernel: CPU temperature above threshold, throttling initiated."
    ]
    
    print("Analyzing Infrastructure Logs...")
    analysis = detector.predict(raw_logs)
    
    for log, result in zip(raw_logs, analysis):
        print(f"[{result}] - {log}")
