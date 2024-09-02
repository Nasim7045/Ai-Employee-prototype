Data Analysis Project
Overview
This project provides a Python-based data analysis tool with a user-friendly graphical interface using Tkinter. The tool supports various types of analyses on datasets, including summary statistics, correlation analysis, and regression analysis. The application allows users to select files, specify analysis types, and view results through an interactive interface.

Project Structure
bash
Copy code
Ai-employee PROJECT/
├── data/
│   └── AssignmentData.xlsx  # Example data file
├── scripts/
│   ├── analysis_engine.py    # Contains analysis functions
│   ├── main.py               # Main script for command-line interface
│   ├── user_interface.py     # GUI application for manual data processing
│   └── __init__.py           # Initializes the scripts module
├── tests/
│   ├── test_analysis_engine.py  # Unit tests for analysis functions
│   ├── __init__.py             # Initializes the tests module
├── README.md                 # This file
└── requirements.txt          # List of dependencies
Libraries
To run this project, you need to install the following Python libraries. These libraries can be installed using pip. The requirements.txt file contains a list of all dependencies.

Install Dependencies
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv myenv
Activate the virtual environment:

Windows:
bash
Copy code
myenv\Scripts\activate
macOS/Linux:
bash
Copy code
source myenv/bin/activate
Install required libraries:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should contain:

Copy code
pandas
numpy
scipy
openpyxl
xlrd
matplotlib
scikit-learn
Scripts
main.py
Purpose: Provides a command-line interface for running data analysis.
Usage:
bash
Copy code
python scripts/main.py --file path/to/your/file --analysis type_of_analysis [--target target_value]
Arguments:
--file: Path to the data file (CSV or Excel).
--analysis: Type of analysis to perform (e.g., summary, correlation, regression).
--target: Target column for regression analysis (optional).
user_interface.py
Purpose: Provides a graphical user interface (GUI) for selecting files and performing data analysis.
Usage:
bash
Copy code
python scripts/user_interface.py
Functionality:
Select a data file (CSV or Excel).
Specify the type of analysis.
Input a target column (required for regression analysis).
Run the analysis and view results in a popup window.
analysis_engine.py
Purpose: Contains functions for performing various types of data analysis.
Functions:
perform_summary_analysis(data): Returns summary statistics of the data.
perform_correlation_analysis(data): Returns correlation matrix of the data.
perform_regression_analysis(data, target): Performs regression analysis and returns coefficients and intercept.
tests/test_analysis_engine.py
Purpose: Contains unit tests for functions in analysis_engine.py.
Usage:
bash
Copy code
python -m unittest discover -s tests
Example Usage
Command-Line Interface
To perform a summary analysis on an Excel file, run:

bash
Copy code
python scripts/main.py --file data/AssignmentData.xlsx --analysis summary
To perform regression analysis with a target column:

bash
Copy code
python scripts/main.py --file data/AssignmentData.xlsx --analysis regression --target target_column_name
Graphical User Interface
Run the GUI application:

bash
Copy code
python scripts/user_interface.py
In the GUI:

Click "Select Data File" to choose your file.
Enter the analysis type (e.g., summary, correlation, regression).
For regression, enter the target column name.
Click "Run Analysis" to view results.
Troubleshooting
ModuleNotFoundError: Ensure that all necessary libraries are installed and correctly imported.
File Errors: Verify that the file path is correct and the file format is supported (CSV or Excel).
