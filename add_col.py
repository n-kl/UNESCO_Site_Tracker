# Script initiates a new column in the CSV file to indicate if the location has been visited.
# 0 indicates no visit, 1 indicates a visit. No other use than initialisation of the
# Visit_Status column

import pandas as pd

csv_input = pd.read_csv("whc-sites-2019.csv")
csv_input["Visit_Status"] = 0
csv_input.to_csv('visit_status_sites', index=False)
