import csv
from math import prod
from products import Product


listOfCategory = [
    'RELOJ SMARTWHATCH','FUENTE','IMPRESORA LASER','IMPRESORA TINTA','GABINETE', 'RELOJ SMARTWATCH',
    'NOTEBOOK','TABLET','TECLADO','MOUSE','PAD PARA MOUSE','CONECTIVIDAD','PARLANTE PORTATIL',
    'PARLANTE','AURICULAR','RAM','PENDRIVE','MSD/SD','PLACA DE AUDIO Y DATOS','PLACA DE VIDEO','MONITOR',
    'SEGURIDAD','MOTHERBOARD','COOLER','ACCESORIO GAMER',
    # 'CARTUCHO TONER', 'CABLE DE VIDEO'
]

def ReadAndSepare(array):
    file = open('Datos ADM Global.csv', 'r')

    with file as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            if row[7] in listOfCategory:
                stock = row[2].split(',')
                stock = int(stock[0]) / 10
                if stock >= int(1):
                    prod = Product(row[0], row[1], stock, row[3], row[4], row[5], row[6], row[7])
                    array.append(prod)
            else:
                continue
    csv_file.close()
    return array

def StoreDara(header, array):
    
    with open('Subir en TN.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        i = 0
        while i < len(array):
            writer.writerow(array[i].getData())
            i += 1
    
    print('Se ha guardado el archivo en la carpeta actual')
    file.close()

if __name__ == "__main__":
    Data = []
    Data2 = ReadAndSepare(Data)
    header = [
        'Identificador de URL',
        'Nombre',
        'Categorías',
        'Precio',
        'Precio promocional',
        'Peso (kg)',
        'Stock',
        'SKU',
        'Código de barras',
        'Mostrar en tienda',
        'Envío sin cargo',
        'Descripción',
        'Tags',
        'Título para SEO',
        'Descripción para SEO',
        'Marca',
        'Producto Físico',
        'MPN (Número de pieza del fabricante)',
        'Sexo',
        'Rango de edad'
    ]
    Data = []
    # for i in Data2:
    #     Data.append(i.getData())

    
    StoreDara(header, Data2)

    input()