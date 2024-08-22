import streamlit as st
from virtual_scenario_generator import VirtualScenarioGenerator
from data_collection_module import DataCollectionModule
from temporal_analysis import TemporalAnalysis
from explainable_ai_module import ExplainableAIModule

st.title("AI-Enhanced Disaster Management Training Platform")

generator = VirtualScenarioGenerator()
data_module = DataCollectionModule()
analyzer = TemporalAnalysis()
ai_module = ExplainableAIModule()

if st.button("Generate Scenario"):
    scenario = generator.generate_scenario()
    st.write("Scenario:", scenario)

    # Placeholder for user interaction and data collection
    data_module.log_decision(5, "Evacuate area")
    data_module.log_communication(6, "Request backup")

    st.write("Data Collected")

if st.button("Analyze Decisions"):
    decision_timeline = analyzer.analyze_decisions_over_time(data_module.decision_logs)
    st.write("Decision Timeline:", decision_timeline)

if st.button("Generate AI Explanation"):
    outcomes = [1, 0]  # Placeholder outcomes
    model = ai_module.train_model(data_module.decision_logs, outcomes)
    explanation = ai_module.generate_explanation(model)
    st.write("AI Explanation:", explanation)
