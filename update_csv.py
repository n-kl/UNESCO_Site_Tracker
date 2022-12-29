import pandas as pd
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


df = pd.read_csv("visit_status_sites", index_col="name_en")


# Creating pop up box
ROOT = tk.Tk()
ROOT.withdraw()

# Requesting user to input site they have visited
location = simpledialog.askstring(title="Location Input",
                                  prompt="Enter UNESCO World Heritage Site You Visited")


# Error checking input
if location == "":
    messagebox.showinfo("NO INPUT", "No changes made")

elif location not in df.index:
    messagebox.showinfo("ERROR", "Visited site not recognised")


# Otherwise adjusting csv file to reflect visitation status,
else:
    df.at[str(location), "Visit_Status"] = 1

# f.loc[["Old and New Towns of Edinburgh"], ["Visit_Status"]] = 1
df.to_csv('visit_status_sites')
