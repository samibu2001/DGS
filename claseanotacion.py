import csv

def clean_lines(file):
    for line in file:
        if line.strip():  # This will skip empty lines
            yield line.replace('\x00', '')

vcf_path = 'C:\\Users\\usuario\\Desktop\\testAnn.vcf'
output_csv = 'impact.csv'

with open(vcf_path, 'r', encoding='utf-8', errors='ignore') as vcf_file, open(output_csv, 'w', newline='') as csvfile:
    vcf_reader = csv.reader(clean_lines(vcf_file), delimiter='\t')
    csv_writer = csv.writer(csvfile)

    # Write only the INFO header
    headers = ['INFO']
    csv_writer.writerow(headers)

    for row in vcf_reader:
        if row and not row[0].startswith('#'):
            if len(row) >= 8:  # Make sure there are enough elements in the row
                info_field = row[7]  # INFO is the 8th column in VCF
                csv_writer.writerow([info_field])  # Write only the INFO field to CSV

print(f'VCF file transformed and saved as {output_csv}')

