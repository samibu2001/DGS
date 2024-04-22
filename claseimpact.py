import csv

def clean_lines(file):
    for line in file:
        if line.strip():  # Skip empty lines
            yield line.replace('\x00', '')

def extract_impact(info_field):
    fields = info_field.split('|')
    for field in fields:
        if 'IMPACT' in field:
            return field
    return 'IMPACT_NOT_FOUND'  # Return not found

vcf_path = 'C:\\Users\\usuario\\Desktop\\testAnn.vcf'
output_csv = 'impactimpact.csv'

with open(vcf_path, 'r', encoding='utf-8', errors='ignore') as vcf_file, open(output_csv, 'w', newline='') as csvfile:
    vcf_reader = csv.reader(clean_lines(vcf_file), delimiter='\t')
    csv_writer = csv.writer(csvfile)

    headers = ['Allele', 'Consequence', 'Impact']
    csv_writer.writerow(headers)

    for row in vcf_reader:
        if row and not row[0].startswith('#'):
            if len(row) >= 8:
                info_field = row[7]  # INFO is the 8th column in VCF
                # Extract the impact
                impact = extract_impact(info_field)
                # allele is the 4th column
                allele = row[3]
                consequence = info_field.split('|')[1]
                csv_writer.writerow([allele, consequence, impact])

print(f'VCF file transformed and saved as {output_csv}')
