# Biomedical Decision Support System

## Overview

This project simulates a biomedical decision system for wound infection detection using physiological signals such as pH, SpO2, and symptoms.

It combines:
- rule-based scoring
- decision engine
- time-series analysis
- visualization
- automated clinical reporting

---

## Features

- Patient risk classification (Healthy / Risk / Critical)
- Biomedical scoring system
- Time-series analysis over multiple days
- Infection progression visualization
- Automated PDF clinical report generation
- Unit testing for validation

---

## Project Structure


engine/ → scoring + decision logic
analysis/ → dataset processing
visualizations/ → graphs (pH, SpO2)
tests/ → validation tests
report/ → PDF generator
data/ → patient dataset
output/ → generated results


---

## How It Works

1. Load patient dataset
2. Convert signals into risk scores
3. Apply decision engine
4. Analyze progression over time
5. Generate plots and report

---

## Output

- Risk classification per day
- pH trend graph
- SpO2 trend graph
- Risk evolution graph
- Clinical PDF report

---

## Goal

To simulate early detection of wound infection using multi-signal biomedical analysis.

---

## Author

Rabeh Mohamed Mehdi