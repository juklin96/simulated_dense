# Dependencies

This project uses R for data cleaning, statistical analysis, and visualisation.

## Software

- R (version 4.6.1)
- Positron (optional; used as the development environment)
- Git (for version control)

## R packages

The following R packages are required:

| Package | Purpose |
|---|---|
| `dplyr` | Data manipulation and preparation |
| `gtsummary` | Creating summary statistics tables |
| `gt` | Formatting and exporting tables |

Base R is used for importing CSV files and performing data cleaning. No additional packages are required for the data-cleaning script.

## Installation

To install the required packages, run the following command in R:

```r
install.packages(c("dplyr", "gtsummary", "gt"))
```

## Notes

- The project uses simulated data.
- Raw data files are excluded from the GitHub repository using `.gitignore`.