import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of mock patient records
num_records = 200

# Generate patient IDs
patient_ids = [f"PAT{str(i).zfill(4)}" for i in range(1, num_records + 1)]

# Generate admission times over a 2-week period
start_date = datetime(2024, 7, 1)
admit_times = [start_date + timedelta(hours=np.random.randint(0, 24*14)) for _ in range(num_records)]

# Generate first order times (1 to 8 hours after admission)
first_order_times = [admit + timedelta(hours=np.random.randint(1, 9)) for admit in admit_times]

# Generate discharge order times (2 to 5 days after admission)
discharge_order_times = [admit + timedelta(days=np.random.randint(2, 6), hours=np.random.randint(0, 6)) for admit in admit_times]

# Generate actual discharge times (0 to 12 hours after discharge order)
discharge_times = [order + timedelta(hours=np.random.randint(0, 13)) for order in discharge_order_times]

# MD and RN documentation completion times (0–6 hours after discharge)
md_note_complete = [discharge + timedelta(hours=np.random.randint(1, 7)) for discharge in discharge_times]
rn_note_complete = [discharge + timedelta(hours=np.random.randint(1, 7)) for discharge in discharge_times]

# Unit transfers and delays
units = ['Med/Surg', 'ICU', 'Telemetry', 'Stepdown', 'Ortho', 'Neuro']
transfer_from = [random.choice(units) for _ in range(num_records)]
transfer_to = [random.choice([u for u in units if u != from_unit]) for from_unit in transfer_from]
transfer_delays = np.random.randint(10, 180, size=num_records)  # in minutes

# Order set usage
order_set_used = np.random.choice(['Yes', 'No'], size=num_records, p=[0.7, 0.3])

# Create DataFrame
df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Admit_Time': admit_times,
    'First_Order_Time': first_order_times,
    'Discharge_Order_Time': discharge_order_times,
    'Discharge_Time': discharge_times,
    'MD_Note_Complete': md_note_complete,
    'RN_Note_Complete': rn_note_complete,
    'Unit_Transfer_From': transfer_from,
    'Unit_Transfer_To': transfer_to,
    'Transfer_Delay_Min': transfer_delays,
    'Order_Set_Used': order_set_used
})

# Export to CSV
df.to_csv('epic_inpatient_mock_data.csv', index=False)
print("Mock inpatient clinical data generated and saved as 'epic_inpatient_mock_data.csv'.")
