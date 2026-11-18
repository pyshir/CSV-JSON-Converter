# CSV & JSON Converter
## Author
**jahid, whatsapp: 8801309495010**

A simple Python-based file converter that allows you to convert multiple CSV files into JSON files and JSON files into CSV files. The project also generates conversion reports and summary reports to keep track of successful and failed conversions.

## Features

- **CSV to JSON:** Convert multiple CSV files into JSON format.
- **JSON to CSV:** Convert multiple JSON files into CSV format.
- **Batch Processing:** Process multiple files automatically.
- **Error Handling:** Identify invalid CSV and JSON files.
- **Conversion Report:** Generate a detailed report of successful and failed conversions.
- **Summary Report:** Get an overview of total, successful, and failed conversions.
- **UTF-8 Support:** Handle Unicode characters and non-English text.

## Project Structure

```text
CSV_JSON_Converter/
│
├── Main_folder/
│   └── CSV_JSON_Converter/
│       │
│       ├── input/
│       │   ├── csv/
│       │   └── json/
│       │
│       ├── output/
│       │   ├── json/
│       │   └── csv/
│       │
│       └── reports/
│           ├── conversion_report.txt
│           └── summary_report.txt
│
├── src/
│   ├── __init__.py
│   └── functions.py
│
├── main.py
└── README.md
```

## Requirements

- Python 3.8 or higher
- No external libraries required.

The project uses Python's built-in modules:

- `os`
- `glob`
- `csv`
- `json`
- `pathlib`

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/CSV-JSON-Converter.git
```

**2. Navigate to the project directory**

```bash
cd CSV-JSON-Converter
```

**3. Prepare the input and output directories**

Create the following directories if they do not already exist:

```text
Main_folder/CSV_JSON_Converter/
├── input/
│   ├── csv/
│   └── json/
├── output/
│   ├── csv/
│   └── json/
└── reports/
```

## Usage

**1. Add your files**

- For CSV to JSON conversion, place your `.csv` files inside:

  `Main_folder/CSV_JSON_Converter/input/csv/`

- For JSON to CSV conversion, place your `.json` files inside:

  `Main_folder/CSV_JSON_Converter/input/json/`

**2. Run the program**

```bash
python main.py
```

**3. Select a conversion option**

```text
1. CSV to JSON
2. JSON to CSV

Enter choice:
```

**Option 1: CSV to JSON**

Enter `1` to convert all CSV files into JSON format.

**Option 2: JSON to CSV**

Enter `2` to convert all JSON files into CSV format.

## Output

Converted files are automatically saved in their respective output directories.

| Conversion | Input Directory | Output Directory |
|---|---|---|
| CSV to JSON | `input/csv/` | `output/json/` |
| JSON to CSV | `input/json/` | `output/csv/` |

## Reports

After conversion, the program generates two report files inside the `reports/` directory.

**1. Conversion Report (`conversion_report.txt`)**

Contains details about individual file conversions, including:

- Successfully converted files.
- Original and converted filenames.
- Failed conversions and error messages.

Example:

```text
==============================
CSV & JSON CONVERTER
==============================

[INFO] Starting Conversion...

[INFO] Found 2 CSV Files

[Success] users.csv -> users.json
[Success] products.csv -> products.json

========== End ==========
```

**2. Summary Report (`summary_report.txt`)**

Provides an overview of the conversion process.

Example:

```text
==============================
CONVERSION SUMMARY REPORT
==============================

Total Files Found: 2

Successful Conversions: 2

Failed Conversions: 0

Conversion Type: CSV to JSON


========== End ==========
```

## Error Handling

The program handles common file-related errors, including:

- Invalid CSV files.
- Invalid JSON files.
- File reading and writing errors.

Failed files are recorded in the conversion and summary reports.

## Technologies Used

- **Language:** Python
- **Data Formats:** CSV, JSON
- **Modules:** os, glob, csv, json, pathlib

## Future Improvements

- [ ] Add support for Excel files (`.xlsx`).
- [ ] Add command-line arguments for conversion.
- [ ] Improve validation of JSON structures.
- [ ] Add logging with timestamps.
- [ ] Prevent overwriting existing output files.
- [ ] Add a graphical user interface (GUI).



If you find this project useful, consider giving it a ⭐ on GitHub!

## License

This project is open-source. You can modify and use it for personal or educational purposes.
