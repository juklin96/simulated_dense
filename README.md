# Repository overview
A simulated repeated-measures cognitive and behavioral dataset based on my doctoral project ("Dense").
The dataset contains data from 20 participants with fibromyalgia (FM) and 20 healthy controls (HC).

## Repo contents
### Data
All simulated data used for this project. Contains demographic information and test scores.
"clean_" prefix indicates the data has been cleaned.

### Analysis
All analysis code. For dependencies, see dependencies.md.

Code should be run in the following order:
1. generate_data.py : for generating the simulated data
2. clean_data.py    : for cleaning the simulated data
3. analysis.py      : analyzing the data; automatically generate figures and report

The flowchart below shows a full overview of outputs from each part of the code.

<img width="1866" height="1215" alt="Flowchart" src="https://github.com/user-attachments/assets/1f6e27e2-0c4c-43a0-ba6e-36de9c6d9a99" />
