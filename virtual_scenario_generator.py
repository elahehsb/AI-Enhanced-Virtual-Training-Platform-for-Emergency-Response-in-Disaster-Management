import random

class VirtualScenarioGenerator:
    def __init__(self):
        self.scenarios = ["Earthquake", "Flood", "Terrorist Attack", "Chemical Spill"]

    def generate_scenario(self):
        scenario = random.choice(self.scenarios)
        events = self.generate_events(scenario)
        return {"scenario": scenario, "events": events}

    def generate_events(self, scenario):
        events = []
        if scenario == "Earthquake":
            events = [
                {"time": 0, "description": "Massive earthquake hits the city."},
                {"time": 5, "description": "Buildings collapse, people are trapped."},
                {"time": 10, "description": "Aftershock tremors, risk of fires."}
            ]
        # Add more scenarios here
        return events

if __name__ == "__main__":
    generator = VirtualScenarioGenerator()
    scenario = generator.generate_scenario()
    print("Generated Scenario:", scenario)
