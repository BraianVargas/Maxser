import csv
from classes.productClass import tnProduct

def readProducts(filename):
    # Read products from file
    products = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            prod = tnProduct(
                    row[0],row[1],
                    row[2],row[3],
                    row[4],row[5],
                    row[6],row[7],
                    row[8],row[9],
                    row[10],row[11],
                    row[12],row[13],
                    row[14],row[15],
                    row[16],row[17],
                    row[18],row[19],
                    row[20],row[21],
                    row[22], row[23],
                    row[24], row[25],
                    row[26], row[27],
                    row[28]
                )
            products.append(prod)

    return products

def updateProducts(admProducts, tnProducts):
    i = 0
    while i < len(admProducts):
        j=0
        while j < len(tnProducts):
            # Update stock and prices of products
            if admProducts[i].getBarcode() == tnProducts[j].getBarcode():
                tnProducts[j].setStock(admProducts[i].getStock())
                price = int(admProducts[i].getPrice()) * 1.15
                price = round(price,0)
                tnProducts[j].setPrice(price)
            j += 1
        i += 1
    print("Actualizado")
    return tnProducts

def saveRestProducts(tnProds, admProds):
    i = 0
    while i < len(tnProds):
        j = 0 
        while j < len(admProds):
            if admProds[j].getBarcode() == tnProds[i].getBarcode():
                admProds.pop(j)
                j += 1    
            else:
                j += 1
        i += 1
    
    i = 0
    for i in range(len(admProds)):
        tnProds.append(admProds[i])

    return tnProds


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



if __name__=='__main__':
    admProducts = readProducts('csv/AdmProducts.csv')
    tnProducts = readProducts('csv/TnProducts.csv')
    header = [
        'Identificador de URL',
        'Nombre',
        'Categorías',
        'Nombre de propiedad 1',
        'Valor de propiedad 1',
        'Nombre de propiedad 2',
        'Valor de propiedad 2',
        'Nombre de propiedad 3',
        'Valor de propiedad 3',
        'Precio',
        'Precio promocional',
        'Peso (kg)',
        'Alto (cm)',
        'Ancho (cm)',
        'Profundidad (cm)',
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
    updated = updateProducts(admProducts, tnProducts)
    var1 = saveRestProducts(updated, admProducts)

    StoreDara(header, var1)    