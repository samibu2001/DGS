import csv


def clean_lines(file):
    for line in file:
        if line.strip():  # This will skip empty lines
            yield line.replace('\x00', '')


vcf_path = 'C:\\Users\\usuario\\Desktop\\testAnn.vcf'
output_csv = 'location.csv'

with open(vcf_path, 'r', encoding='utf-8', errors='ignore') as vcf_file, open(output_csv, 'w', newline='') as csvfile:
    vcf_reader = csv.reader(clean_lines(vcf_file), delimiter='\t')
    csv_writer = csv.writer(csvfile)

    headers = ['POS', 'REF']  # Only include POS AND REF
    csv_writer.writerow(headers)

    for row in vcf_reader:
        # Add a check to make sure the row is not empty
        if not row or row[0].startswith('#'):
            continue
        pos = row[1]
        ref = row[3]
        csv_writer.writerow([pos,ref])

print(f'VCF file transformed and saved as {output_csv}')
