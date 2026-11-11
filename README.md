# Workforce and Organizational Effectiveness

Public-safe demonstrations of training transfer, change adoption, staffing analysis, organizational communication, and service experience.

## What this repository demonstrates

- Connecting workforce activity to measurable implementation indicators.
- Exploring staffing and contract-labor questions with synthetic data.
- Framing consultation adoption and closed-loop communication.
- Communicating limitations when baselines and denominators are incomplete.

## Projects

- [Competency and training transfer](projects/staff_competency.md)
- [Consultation follow-through and implementation adoption](projects/consultation_adoption.md)
- [Contract labor utilization](projects/contract_staffing.md)
- [Patient experience and closed-loop communication](projects/patient_experience.md)

## Data and reproducibility

The included datasets are synthetic demonstrations:

- [`data/contract_staffing_synthetic.csv`](data/contract_staffing_synthetic.csv)
- [`data/training_synthetic.csv`](data/training_synthetic.csv)
- [`data/patient_experience_synthetic.csv`](data/patient_experience_synthetic.csv)

Read the [data policy](DATA_POLICY.md), then run from this repository directory:

```powershell
python scripts/analyze_workforce.py
```

## Interpretation limits

Synthetic outputs do not describe a real employer or workforce. Do not infer organizational effectiveness, causal impact, or financial savings without a verified baseline, denominator, measurement period, and approved source.

## Repository map

```text
data/       Synthetic demonstration data
projects/   Workforce and organizational-effectiveness examples
scripts/    Reproducible analysis scripts
```
