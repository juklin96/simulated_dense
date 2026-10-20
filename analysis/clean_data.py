from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#defining paths and .csv files
script_dir = Path(__file__).resolve().parent

path_demo = script_dir.parent / "data" / "synthetic_fibromyalgia_participant_demographics.csv" #demographics path
path_data = script_dir.parent / "data" / "synthetic_fibromyalgia_weekly_dataset.csv"           #dataset path

figures_dir = script_dir / "figures"                    #locates figure directory
figures_dir.mkdir(exist_ok=True)                        #make figures directory (if it does not already exist)

path_report = script_dir / "data_quality_report.md"     #path for data quality report


##BEGINNING DATA EXPLORATION AND CLEANING
demo = pd.read_csv(path_demo)  #load demographics
data = pd.read_csv(path_data)  #load dataset

#Explore demographics
print(f"Age range: {demo['age_years'].min()}–{demo['age_years'].max()} years")
print("Distribution of education:", demo["education_level"].value_counts(dropna=False))

#Explore weekly results


#Plotting data (used to also find outliers)
#defining groups
fm = data[data["group"] == "FM"]
hc = data[data["group"] == "HC"]


#Plotting line plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

#for current pain
for ax, df, group_name in zip(
    axes,
    [fm, hc],
    ["Fibromyalgia (FM)", "Healthy controls (HC)"] 
):
    # each line in the line plot = one subject
    for participant_id, participant in df.groupby("participant_id"):
        participant = participant.sort_values("week")

        ax.plot(
            participant["week"],
            participant["current_pain_0_10"],
            marker="o",
            alpha=0.5,
            label=participant_id
        )

    #plot labels
    ax.set_title(group_name)
    ax.set_xlabel("Week")
    ax.set_xticks(range(1, 9))
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3)

axes[0].set_ylabel("Current pain (0–10)")

fig.savefig(
    figures_dir / "raw_current_pain.png",
    dpi=150,
    bbox_inches="tight"
)

plt.tight_layout()
plt.show()    #printing the plot

#checks which participant(s) has impossible current pain score, as seen in plot
data[
    (data["current_pain_0_10"] > 10) |
    (data["current_pain_0_10"] < 0)
]

#removes participant FM012's erroneous current pain score on week 3
data.loc[
    (data["participant_id"] == "FM012") & (data["week"] == 3),
    "current_pain_0_10"
] = np.nan


#Plots continued: looks at stroop response time
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

#for stroop reaction times
for ax, df, group_name in zip(
    axes,
    [fm, hc],
    ["Fibromyalgia (FM)", "Healthy controls (HC)"] 
):
    # one line per subject
    for participant_id, participant in df.groupby("participant_id"):
        participant = participant.sort_values("week")

        ax.plot(
            participant["week"],
            participant["stroop_mean_rt_ms"],
            marker="o",
            alpha=0.5,
            label=participant_id
        )

    ax.set_title(group_name)
    ax.set_xlabel("Week")
    ax.set_xticks(range(1, 9))
    ax.grid(True, alpha=0.3)

axes[0].set_ylabel("Stroop mean reaction time (ms) before data cleaning")

#save png of raw stroop data plot
fig.savefig(
    figures_dir / "raw_stroop_rt.png",
    dpi=150,
    bbox_inches="tight"
)

plt.tight_layout()
plt.show()

#Checking which participant has an impossibly low stroop reaction time
data[data["stroop_mean_rt_ms"] < 100]

#Changing impossible score to nan
data.loc[
    (data["participant_id"] == "FM004") & (data["week"] == 6),
    "stroop_mean_rt_ms"
] = np.nan



#Changes made:
# FM012's impossible pain score (11, supposed to be 0-10) set to NaN.
# FM004's impossible Stroop reaction time (<100 ms) set to NaN.

def dataframe_to_markdown(df):
    """Convert a DataFrame to a Markdown table without extra packages."""
    if df.empty:
        return "_No observations flagged._"

    columns = list(df.columns)
    rows = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |"
    ]

    for _, row in df.iterrows():
        values = [
            "" if pd.isna(value) else str(value)
            for value in row
        ]
        rows.append("| " + " | ".join(values) + " |")

    return "\n".join(rows)


report = f"""# Data Quality Report: Simulated Fibromyalgia Dataset

## 1. Purpose

This report (drafted using ChatGPT and edited by the repo owner, JK, 
for accuracy) documents the initial exploration of the simulated
longitudinal dataset, the identification of potentially invalid
observations, and the corrections made during data cleaning.

The simulated dataset contains weekly observations from participants 
in the fibromyalgia (FM) and healthy control (HC) groups.

## 2. Demographic overview

- **Age range:** {demo['age_years'].min()}–{demo['age_years'].max()} years

### Education distribution

{dataframe_to_markdown(
    demo['education_level'].value_counts(dropna=False)
    .rename_axis('Education level')
    .reset_index(name='Number of participants')
)}

## 3. Current pain scores

Current pain was expected to range from 0 to 10. Values outside this
range were flagged as invalid.

### Plot before cleaning

![Current pain scores before cleaning](figures/current_pain_before_cleaning.png)

### Flagged observations

{dataframe_to_markdown(invalid_pain)}

### Correction

The current pain score for participant FM012 in week 3 was set to
`NaN` (missing), because the score was outside the permitted 0–10 range.

## 4. Stroop reaction times

Stroop mean reaction times were plotted across the eight weeks for
both participant groups. Values that fell significantly outside the
expected range based on a visual expection (<100ms) were excluded.

### Plot before cleaning

![Stroop reaction times before cleaning](figures/stroop_rt_before_cleaning.png)

### Flagged observations

{dataframe_to_markdown(invalid_stroop)}

### Correction

The Stroop mean reaction time for participant FM004 in week 6 was
set to `NaN` (missing), following the data-quality review.

## 5. Summary of changes

| Variable | Participant | Week | Action | Reason |
| --- | --- | --- | --- | --- |
| Current pain | FM012 | 3 | Set to NaN | Score outside the 0–10 range |
| Stroop mean reaction time | FM004 | 6 | Set to NaN | Flagged as an implausibly low reaction time |

## 6. Notes

- The plots show the data before the corrections were applied.
- `NaN` represents a missing value; the original value is not retained
  in the in-memory cleaned DataFrame.
- Cleaned datasets are available in clean_data_demo.csv and clean_data_testscores.csv.
- Raw datasets remain available in data_demo.csv and data_testscores.csv.
  original CSV file.
"""

path_report.write_text(report, encoding="utf-8")

print(f"Markdown report saved to: {path_report}")
print(f"Plot images saved in: {figures_dir}")

