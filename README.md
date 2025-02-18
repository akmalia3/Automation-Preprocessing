# Data Analysis and Anomaly Handling Web App 🚀

This is a simple web application built with **Streamlit** for handling missing values and anomalies (outliers) in sales data. The app provides tools to upload, clean, visualize, and analyze sales data by performing operations like handling missing values, detecting and handling outliers, and calculating daily delta (sales difference).

## Features
- Upload an Excel file with sales data (two columns: Date and Total Sales).
- Handle missing values using forward filling (`ffill`).
- Detect outliers using Z-score and provide an option to handle them by replacing with the median value.
- Visualize data with outliers marked in a plot.
- Calculate and display the daily delta (difference between consecutive days' total sales).
  
## Requirements

To run the app, you need to install the following Python libraries:

- **Streamlit** - for creating the interactive web app
- **Pandas** - for data manipulation
- **Matplotlib** - for data visualization
- **Openpyxl** - for reading Excel files

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload an Excel file with **two columns**: 
   - **Date** (the sales date)
   - **Total Sales** (the amount of sales for each date)

3. The app will automatically handle missing values, detect outliers, and calculate daily delta. You can choose to replace the outliers with the median sales value if needed.

4. Once the data is processed, the results will be displayed, including the cleaned data and a plot showing the outliers.

## Example Usage

- **Handle Missing Values**: If there are missing sales data points, the app will fill them using the forward-fill method.
- **Handle Anomalies**: The app detects anomalies using Z-score and provides an option to replace them with the median sales value.
- **Daily Delta**: The app calculates the daily delta, which is the difference between the total sales of each day compared to the previous day.

## Files in this Repository

- `app.py`: The main application code that runs the web interface.
- `requirements.txt`: The list of required Python packages.
- `README.md`: This file with setup and usage instructions.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, submit issues, and create pull requests. I would be happy to collaborate on any improvements or bug fixes!

## License

This project is open source and available under the [MIT License](LICENSE).

