import pandas as pd

class DataCollectionModule:
    def __init__(self):
        self.physiological_data = []
        self.decision_logs = []
        self.communication_logs = []

    def collect_physiological_data(self, data):
        self.physiological_data.append(data)

    def log_decision(self, time, decision):
        self.decision_logs.append({"time": time, "decision": decision})

    def log_communication(self, time, message):
        self.communication_logs.append({"time": time, "message": message})

    def save_data(self, filename="collected_data.csv"):
        df = pd.DataFrame({
            "Physiological Data": self.physiological_data,
            "Decision Logs": self.decision_logs,
            "Communication Logs": self.communication_logs
        })
        df.to_csv(filename, index=False)

if __name__ == "__main__":
    data_module = DataCollectionModule()
    data_module.collect_physiological_data({"heart_rate": 80, "stress_level": 0.2})
    data_module.log_decision(5, "Evacuate area")
    data_module.log_communication(6, "Request backup")
    data_module.save_data()
    print("Data Collected and Saved.")
