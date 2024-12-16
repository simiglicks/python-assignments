import argparse
from Bio import Entrez
import csv
from datetime import datetime

def search_db_records(database, term, number):
    """
    Connect to NCBI, return `number` items based on `term` from `database`.
    """
    Entrez.email = "gabor@szabgab.com"
    handle = Entrez.esearch(db=database, retmax=number, term=term, idtype="acc")
    data = Entrez.read(handle)
    handle.close()
    return data

def fetch_and_save_record(record_id, database):
    """
    Connects to NCBI, and retrieves the file `record_id` from the database `database`.
    Saves the file to a file names `<record_id.txt>`
    """
    print(f'Fetching and saving {record_id} from {database}')
    try:
        record_data = Entrez.efetch(db=database, id=record_id, rettype="gb", retmode="text")
    except:  # failsafe, if incorrect datatype, then just take plaintext
        record_data = Entrez.efetch(db=database, id=record_id, retmode="text")
    data = record_data.read()
    record_data.close()
    filename = f'{record_id}.txt'
    with open(filename, 'w') as f:
        f.write(data)
    return filename

def main():
    """
    Main script. Collects command line arguments, and uses them to retreive data from NCBI.
    """
    output_csv = 'total_records.csv'
    ap = argparse.ArgumentParser()
    ap.add_argument('--term', required=True)
    ap.add_argument('--database', default='nucleotide', required=False)
    ap.add_argument('--number', default=10, type=int, required=False)
    args = ap.parse_args()  # get options from the command line

    # get search results
    db_data = search_db_records(args.database, args.term, args.number)

    # header row for the csv
    header = ['date', 'database', 'term', 'max', 'total']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # format today's date to be human-readable
    row_data = [time, args.database, args.term, db_data['RetMax'], db_data['Count']]

    # save data in csv
    with open(output_csv, 'a+') as f:
        writer = csv.writer(f, lineterminator='\n')
        # if new file, write header row
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow(row_data)

    filenames = []
    # for every ID/filename from search result, fetch the page
    for record in db_data['IdList']:
        try:
            filename = fetch_and_save_record(record, args.database)
            filenames.append(filename)
        except Exception as e:
            print(f'[ERROR] Could not retrieve {record}: {str(e)}')
    print(filenames)
if __name__ == '__main__':
    main()