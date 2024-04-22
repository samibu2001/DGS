import csv


def clean_lines(file):
    for line in file:
        if line.strip():  # This will skip empty lines
            yield line.replace('\x00', '')


vcf_path = 'C:\\Users\\usuario\\Desktop\\testAnn.vcf'
output_csv = 'varianttype.csv'

with open(vcf_path, 'r', encoding='utf-8', errors='ignore') as vcf_file, open(output_csv, 'w', newline='') as csvfile:
    vcf_reader = csv.reader(clean_lines(vcf_file), delimiter='\t')
    csv_writer = csv.writer(csvfile)

    headers = ['VariantType', 'ID', 'ALT']  # Only include VariantType, ID, and ALT headers
    csv_writer.writerow(headers)

    for row in vcf_reader:
        # Add a check to make sure the row is not empty
        if not row or row[0].startswith('#'):
            continue
        variant_type = row[2]
        variant_id = row[2]
        alt = row[4]
        csv_writer.writerow([variant_type, variant_id, alt])

print(f'VCF file transformed and saved as {output_csv}')

