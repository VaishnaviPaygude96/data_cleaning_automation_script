# Data Cleaning Automation Script 🧹

A simple Python script to automate basic data cleaning tasks using **Pandas**. It helps you preprocess CSV files by performing common cleaning operations with minimal manual effort.

## Features
- ✅ Remove duplicate rows
- ✅ Clean and standardize column names (lowercase, underscores)
- ✅ Handle missing values:
  - Categorical columns ➔ Filled with mode
  - Numerical columns ➔ Filled with mean (if less skewed) or median (if skewed)
- ✅ Drop remaining rows with missing values
- ✅ Save the cleaned data into a `cleaned_data` folder

## How to Use

1. **Clone the Repository**
```bash
git clone https://github.com/VaishnaviPaygude96/data_cleaning_automation_script.git
cd data_cleaning_automation_script
```

2. **Install Dependencies**
```bash
pip install pandas
```

3. **Add Your CSV File**

Place your CSV file inside the project folder.

4. **Update the File Path in the Script**
```python
file_to_clean = "path/to/your/file.csv"
clean_data(file_to_clean)
```

5. **Run the Script**
```bash
python clean_data.py
```

6. **Check the Output**

The cleaned CSV file will be saved in the `cleaned_data` folder.

## Example Output
```
Original Shape: (500, 10)
Cleaned Data Saved to: cleaned_data/cleaned_academic.csv
Final Shape: (480, 10)
```

## Built With
- Python 3.x
- Pandas

## Author
**Vaishnavi Paygude**  
[GitHub Profile](https://github.com/VaishnaviPaygude96)

## License
This project is licensed under the MIT License.
