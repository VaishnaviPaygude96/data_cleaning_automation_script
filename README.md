# ✨ Data Cleaning Automation Script 🧹

Automate your CSV data cleaning process with this simple and powerful Python script!  
Easily handle duplicates, missing values, and messy column names — all with one click.

---

## 🔥 Features
- 🗑️ **Remove duplicate rows automatically**
- 📝 **Standardize column names** (lowercase, underscores)
- 🧩 **Handle missing values smartly**  
  - 🗂️ Categorical ➔ Filled with **Mode**  
  - 🔢 Numerical ➔ Filled with **Mean** (less skewed) or **Median** (skewed)
- 🚫 **Drop remaining missing rows (if any)**
- 💾 **Save cleaned data in a dedicated `cleaned_data` folder**

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VaishnaviPaygude96/data_cleaning_automation_script.git
cd data_cleaning_automation_script
```

### 2️⃣ Install Required Packages
```bash
pip install pandas
```

### 3️⃣ Add Your CSV File  
Place your `.csv` file inside the project folder.

### 4️⃣ Update the File Path in the Script
```python
file_to_clean = "path/to/your/file.csv"
clean_data(file_to_clean)
```

### 5️⃣ Run the Script
```bash
python clean_data.py
```

### 6️⃣ Check the Output  
Your cleaned file will be saved in the `cleaned_data` folder with a **cleaned_** prefix.

---

## ✅ Sample Output
```
Original Shape: (500, 10)
Cleaned Data Saved to: cleaned_data/cleaned_academic.csv
Final Shape: (480, 10)
```

---

## 🛠️ Built With
- 🐍 [Python 3.x](https://www.python.org/)
- 📊 [Pandas](https://pandas.pydata.org/)

---

## 👩‍💻 Author

**Vaishnavi Paygude**  
🌐 [GitHub](https://github.com/VaishnaviPaygude96)

---

> ⭐ If you find this useful, don’t forget to star the repo!
