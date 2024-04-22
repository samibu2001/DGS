import requests
import os

# Obtenemos ruta
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# URL 
url = 'https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz'

# Realizamos la solicitud HTTP GET para descargar el archivo
response = requests.get(url)

# Nos aseguramos de que la solicitud es exitosa (código de estado 200)
if response.status_code == 200:
    # Construye la ruta completa donde se guardará el archivo
    file_path = os.path.join(desktop_path, 'clinvar.vcf.gz')

    # Escribe a un archivo en el escritorio
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'Descarga completada. El archivo se guardó en: {file_path}')
else:
    print('Error en la descarga:', response.status_code)
