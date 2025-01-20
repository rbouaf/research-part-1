import csv
csv_file_path = "db/users.csv"

def if_in_user_db(uploader):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['UPLOADER'] == uploader:
                return True
    return False