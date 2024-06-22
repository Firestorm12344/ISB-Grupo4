# Lab 11 - Edge Impulse -  Ana Lucía Espinoza

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Resultados](#resultados)



##  Objetivos
- Crear tres proyectos correspondientes a EMG, ECG y EEG en Edge Impulse y subir las señales trabajadas en clase con sus correspondientes etiquetas

## Materiales
| Material | Cantidad |
|:--------------:|:--------------:|
| Lenguaje de programación *Python* | N.A | 
| Plataforma *Edge Impulse* | N.A | 

## Resultados
# EMG

# ECG
![Uploading image.png…]()

# EEG


## Código en Python
# EMG
``` python

```

# ECG
``` python
# Install requests via: pip3 install requests
import requests
import os
import json
import csv

api_key = 'ei_fd64f0381709ef292f6078925c67324cc2d95a8e9fb4c065'

# Add the files you want to upload to Edge Impulse

files = [
    'Señal_ECG02.csv'
]
# # Replace the label with your own.
label = 'ECG - señal cruda fibrilación ventricular severa'

# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'image/png')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
```

# EEG
``` python

```




