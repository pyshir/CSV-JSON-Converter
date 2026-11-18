import os, glob, csv, json
from pathlib import Path

abs_path = Path(os.path.abspath('Main_folder')) / 'CSV_JSON_Converter'

def is_empty(file_path):
    if not Path.exists(file_path) or os.stat(file_path).st_size == 0:
        return True
    else:
        return False

def json_converter():
    #load csv files
    success = []
    failed = {}

    input_path = Path(abs_path) / 'input' / 'csv'
    files = glob.glob(f'{input_path}/*.csv')
    for i in files:
        try:        
            temp_json = []
            name = os.path.split(i)[1]
            name = os.path.splitext(name)[0]
            name = name + '.json'
            with open(i, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for x in reader:
                    temp_json.append(x)
                output_path = Path(abs_path) / 'output' / 'json' / name
                with open(output_path, 'w') as g:
                    json.dump(
                        temp_json,
                        g,
                        ensure_ascii=False,
                        indent=4
                    )
            success.append(i)
                
        except (csv.Error, OSError):
            failed[i] = 'Invalid CSV File'

    return success, failed

def csv_converter():
    success = []
    failed = {}
    input_path = Path(abs_path) / 'input' / 'json'
    
    files = glob.glob(f'{input_path}/*.json')
    for i in files:
        try:        
            fieldnames = []
            name = os.path.split(i)[1]
            name = os.path.splitext(name)[0] + '.csv'
            with open(i, 'r') as f:
                reader = json.load(f)
                for p1 in reader:
                    for p, q in p1.items():
                        fieldnames.append(p)
                    break
                for x in reader:
                    output_path = Path(abs_path) / 'output' / 'csv' / name
                    with open(output_path, 'a+', newline='', encoding='utf-8') as g:
                        writer = csv.DictWriter(
                            g,
                            fieldnames=fieldnames
                        )
                        if is_empty(output_path):
                            writer.writeheader()
                            writer.writerow(x)
                        else:
                            writer.writerow(x)
            success.append(i)

        except (json.JSONDecodeError, OSError):
            failed[i] = 'Invalid JSON File'

    return success, failed

def conv_report(success, failed):
    file_path = Path(abs_path) / 'reports' / 'conversion_report.txt'
    with open(file_path, 'w') as f:
        f.write(f'{'='*30}\nCSV & JSON CONVERTER\n{'='*30}\n\n')
        f.write(f'[INFO] Starting Conversion...\n\n')
        extension = Path(success[0]).suffix
        if extension == '.csv':
            f.write(f'[INFO] Found {len(success)} CSV Files\n\n')
        elif extension == '.json':
            f.write(f'[INFO] Found {len(success)} JSON Files\n\n')
        for i in success:
            pre = Path(i).name
            if Path(pre).suffix == '.csv':
                post = Path(pre).stem + '.json'                
            elif Path(pre).suffix == '.json':
                post = Path(pre).stem + '.csv'                
            f.write(f'[Success] {pre} -> {post}\n')
        f.write('\n')
        for x, y in failed.items():
            file_name = Path(x).name
            f.write(f'[ERROR] {file_name} - {y}\n')
        f.write(f'\n{'='*10} End {'='*10}')

def summery(success, failed, type):
    file_path = Path(abs_path) / 'reports' / 'summary_report.txt'
    total_success = len(success)
    key_list = [key for key, value in failed.items()]
    total_failed = len(key_list)
    with open(file_path, 'w') as f:
        f.write(f'{'='*30}\nCONVERSION SUMMARY REPORT\n{'='*30}\n\nTotal Files Found: {total_success+total_failed}\n\nSuccessful Conversions: {total_success}\n\nFailed Conversions: {total_failed}\n\nConversion Type: {type}\n\n\n{'='*10} End {'='*10}')









