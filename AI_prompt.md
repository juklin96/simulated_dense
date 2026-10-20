# Creation of the simulated dataset (detailed version)

The dataset used for this mini-project was created using the free version of ChatGPT-6 on October 13, 2026.

## Prompt 1 

> "This is a simulated dataset for my class on open science practices. I wish to simulate a dataset based on my real-world dataset that I am analyzing for my PhD studies. Based on the characteristics from this simulated dataset from the class, that I am uploading, can you create a new simulated dataset based on questionnaires and study design descriptors that I provide you based on my own study?"

Together with this prompt, I attached the 2 files from the simulated dataset #1 from the course's github page.

## Prompt 2 

> Details of my study: 1. 20 healthy controls and 20 participants with fibromyalgia. All participants are women, age 25-55. Participants undergo behavioral testing and cognitive testing once a week for 8 weeks. All participants do the same tests every week. 2. Questionnaires: ISI (insomnia severity index), PHQ-9, pain catastrophizing scale (PCS), and a homemade scale of current pain (0-10), least pain the past week (0-10), and worst pain past week (0-10). Tests: stroop, go/no-go (include variables of reaction times and correct/incorrect responses). 3. Demographics (age, education level (1 = did not complete high school, 2 = completed high school, 3 = completed short tertiary education, 4 = completed long tertiary education), duration of pain in years (for the FM patients), diagnosed FM (yes for FM patients, no for HC). 4. Suspected correlations based on the existing literature. 5. I DO want some slight data quality problems like in the simulated dataset, as well as some missing data and missed visits.
>
> Please do simulate both intra- and interindividual variations.

Resulting script for simulated data generation can be found in /code/generate_data.py
