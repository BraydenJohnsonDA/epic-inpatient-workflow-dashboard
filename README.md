# Epic Inpatient Clinical Workflow Dashboard

This project was developed by Brayden Johnson as a technical demonstration for the Epic Inpatient Clinical System Analyst position at Freeman Health System. It simulates how an analyst would support inpatient workflow improvements by identifying clinical delays and system inefficiencies using mock Epic data.

---

## Project Purpose

The goal of this project is to show how Epic inpatient data can be used to uncover workflow bottlenecks, documentation lags, and discharge delays. As a systems analyst, my focus is on supporting providers and clinical staff by using real-time insights to guide improvements that reduce inefficiency, enhance patient care, and streamline documentation and discharge workflows.

---

## Key Insights

- **Avg. Time to First Provider Order**: 4.6 hours, with the longest delays seen in Telemetry and Stepdown units
- **Avg. Discharge Delay (Order to Execution)**: 5.6 hours
- **MD & RN Documentation Lag**: Averaged 3.6 and 3.3 hours after discharge, highest in Neuro and Telemetry
- **Unit Transfer Delays**: Average of 89.1 minutes
- **Order Set Usage**: 65% of inpatient encounters used standard order sets, showing room for improvement

---

## Recommendations

- Add alerts in Epic for first-order delays beyond 4 hours
- Improve discharge coordination in high-delay units like Ortho and Telemetry
- Reduce post-discharge documentation lag with optimized templates and Epic-integrated reminders
- Increase order set adoption through workflow audits and targeted provider training

---

## Files Included

| File Name                                  | Description |
|-------------------------------------------|-------------|
| `epic_inpatient_dashboard.pbix`           | Power BI dashboard |
| `epic_inpatient_mock_data.csv`            | Mock dataset used in analysis |
| `generate_epic_inpatient_mock_data.py`    | Python script to generate the data |
| `epic_inpatient_dashboard_screenshot.png` | Visual preview of the dashboard |
| `BraydenJohnson_EpicInpatient_WorkflowSummary.pdf` | One-page summary of project insights |

---

## Tools Used

- Power BI
- Python (for mock data generation)
- DAX (calculated columns and measures)
- GitHub (portfolio hosting)

---

## About the Author

I'm Brayden Johnson, a data-driven problem solver with a background in healthcare operations and a growing portfolio of Epic and BI-focused analytics projects. This simulation was built to demonstrate how I approach workflow design, cross-team collaboration, and systems thinking within Epic environments.

