# System Design

## Overview
This system is a Biomedical Decision Support Pipeline designed to simulate and analyze wound infection progression using physiological signals.

## Architecture

The system is divided into four main layers:

### 1. Data Layer
- Input: patient.csv
- Contains:
  - pH values
  - SpO2 values
  - symptoms (fever, pain)
  - time (days)

### 2. Scoring Layer (Engine)
Located in `engine/`

- Converts raw clinical values into risk scores
- Modules:
  - pH scoring
  - SpO2 scoring
  - symptom scoring

### 3. Decision Layer
Located in `engine/decision_engine.py`

- Combines all scores
- Applies clinical rules
- Outputs:
  - Healthy
  - Risk
  - Critical

### 4. Analysis & Visualization Layer
- Runs system over time
- Generates:
  - trends
  - plots
  - infection progression graphs

### 5. Reporting Layer
- Produces final clinical report (PDF)
- Summarizes:
  - patient condition
  - risk evolution
  - visual evidence

## Flow

Data → Scoring → Decision Engine → Analysis → Visualization → Report