# Data Science Snippets 🧰

Welcome to the **Data Science Snippets** repository! This collection of functions is designed to accelerate exploratory data analysis (EDA), quickly surface data quality issues, and offer high-level insights into the structure and content of your dataset. You can download and execute the latest releases [here](https://github.com/VitinDM/data-science-snippets/releases).

![Data Science Snippets](https://img.shields.io/badge/Data%20Science%20Snippets-Ready%20to%20Use-brightgreen)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In today's data-driven world, the ability to quickly analyze and clean data is essential. This repository provides a set of snippets that simplify common tasks in data science, especially for those working with Python and pandas. Whether you're an experienced data scientist or just starting, these tools will help you save time and improve your workflow.

## Features

- **Exploratory Data Analysis (EDA)**: Functions to summarize and visualize your data.
- **Data Cleaning**: Tools to identify and handle missing values, duplicates, and outliers.
- **Feature Engineering**: Snippets to create new features from existing data.
- **Model Evaluation**: Functions to assess the performance of your models.
- **Time Series Analysis**: Tools for handling and analyzing time series data.
- **Text Processing**: Functions for cleaning and analyzing text data.

## Installation

To use the snippets in this repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/VitinDM/data-science-snippets.git
   ```

2. Navigate to the project directory:

   ```bash
   cd data-science-snippets
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. You can now use the snippets in your projects.

## Usage

To use the functions in this repository, simply import them into your Python script or Jupyter notebook. Here’s a basic example:

```python
from data_science_snippets import eda_helpers

# Load your DataFrame
import pandas as pd
df = pd.read_csv('your_data.csv')

# Use EDA function
eda_helpers.summarize_data(df)
```

Feel free to explore the functions available and adapt them to your specific needs.

## Functions Overview

### EDA Helpers

- **summarize_data(df)**: Provides a summary of the DataFrame, including statistics and data types.
- **visualize_missing_values(df)**: Displays a heatmap of missing values in the DataFrame.

### Data Cleaning Helpers

- **remove_duplicates(df)**: Removes duplicate rows from the DataFrame.
- **fill_missing_values(df, method)**: Fills missing values using specified methods (mean, median, mode).

### Feature Engineering Helpers

- **create_feature(df, feature_name, func)**: Creates a new feature based on a specified function.

### Model Evaluation Helpers

- **evaluate_model(y_true, y_pred)**: Calculates and returns common evaluation metrics.

### Time Series Helpers

- **resample_time_series(df, freq)**: Resamples a time series DataFrame to a specified frequency.

### Text Processing Helpers

- **clean_text(text)**: Cleans and preprocesses text data for analysis.

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests for any new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue or contact the repository owner.

You can download and execute the latest releases [here](https://github.com/VitinDM/data-science-snippets/releases). If you need more information, check the "Releases" section for updates and changes.

![Explore Data Science](https://img.shields.io/badge/Explore%20Data%20Science-Join%20Us-blue)

## Conclusion

Thank you for visiting the Data Science Snippets repository. We hope you find these tools useful for your data analysis and modeling tasks. Your feedback and contributions are valuable to us as we continue to improve this collection of functions. Happy coding!