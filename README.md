# CleanConvert

## Overview
**CleanConvert** is a user-friendly Streamlit app that allows users to effortlessly clean, convert, and visualize their data from CSV and Excel files. With built-in data processing and transformation tools, users can seamlessly refine their datasets and export them in their preferred format.

## Features
- 📂 **Upload Multiple Files**: Supports both CSV and Excel files.
- 🔍 **Data Preview**: Displays the first five rows of uploaded data.
- 📊 **Data Summary**: View basic statistical details about your dataset.
- 🔧 **Data Cleaning**:
  - Remove duplicate rows.
  - Fill missing values with column averages.
- 🎯 **Column Selection**: Choose specific columns to keep in your dataset.
- 📈 **Data Visualization**: Generate bar charts for numeric columns.
- 🔄 **File Conversion**: Convert and download files as CSV or Excel.

## Installation
Ensure you have Python installed on your system. Then, install the required dependencies:
```sh
pip install streamlit pandas openpyxl
```

## Usage
Run the following command to start the app:
```sh
streamlit run app.py
```

## How It Works
1. Upload one or more CSV/XLSX files.
2. View a preview of the data.
3. Use the provided tools to clean and transform your dataset.
4. Select specific columns if needed.
5. Visualize your data with interactive charts.
6. Convert and download your cleaned data.

## Dependencies
- [Streamlit](https://streamlit.io/) - UI for interactive web apps.
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis.
- [OS](https://docs.python.org/3/library/os.html) - File handling operations.
- [IO (BytesIO)](https://docs.python.org/3/library/io.html) - File input/output operations.
- [Datetime](https://docs.python.org/3/library/datetime.html) - Timestamping converted files.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this project and submit pull requests with improvements.

---

🎉 Happy Data Cleaning & Converting! 🚀

