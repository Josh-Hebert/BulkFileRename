import csv
import os



def get_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        filenames.append(filename)
    return filenames

def write_filenames_to_csv(filenames, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Old Filename'])
        for filename in filenames:
            writer.writerow([filename])



#Trying to create a file with old and new filenames
def add_column_to_csv(old_filenames_csv, new_filenames_csv):
    with open(old_filenames_csv, 'r') as f_old:
        reader = csv.reader(f_old)
        old_data = [row[0] for row in reader]

    new_data = []
    with open(new_filenames_csv, 'r') as f_new:
        reader = csv.reader(f_new)
        #header = next(reader)
        for row in reader:
            new_data.append([old_data[0]] + row)
            old_data = old_data[1:]

    with open(new_filenames_csv, 'w', newline='') as f_new:
        writer = csv.writer(f_new)
        #writer.writerow(['Old Filename'] + header)
        for row in new_data:
            writer.writerow(row)
        for val in old_data:
            writer.writerow([val, ''])


def bulk_rename(old_filenames_csv, new_filenames_csv, directory):
    old_filenames = {}
    with open(old_filenames_csv, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # skip header
        for row in reader:
            old_filename = row[0]
            old_filenames[old_filename] = None
    with open(new_filenames_csv, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # skip header
        for row in reader:
            old_filename = row[0]
            new_filename = row[1]
            if old_filename in old_filenames:
                old_file_path = os.path.join(directory, old_filename)
                new_file_path = os.path.join(directory, new_filename)
                os.rename(old_file_path, new_file_path)

directory = "C:\\Users\\TheLAB\\Documents\\TestFileRename"
filenames = get_filenames(directory)
old_filenames_csv = 'old_filenames.csv'
write_filenames_to_csv(filenames, old_filenames_csv)
new_filenames_csv = 'new_filenames.csv'

add_column_to_csv(old_filenames_csv, new_filenames_csv)
bulk_rename(old_filenames_csv, new_filenames_csv, directory)
