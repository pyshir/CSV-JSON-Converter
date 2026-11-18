import src

if __name__ == '__main__':
    print(
        """
1. CSV to JSON
2. JSON to CSV
"""
    )

    choice = input('Enter choice: ')

    if choice == '1':
        success, failed = src.json_converter()
        src.conv_report(success, failed)
        src.summery(success, failed, 'CSV to JSON')
    elif choice == '2':
        success, failed = src.csv_converter()
        src.conv_report(success, failed)
        src.summery(success, failed, 'JSON to CSV')
        