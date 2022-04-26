class Product:
    # COD. ARTIC.	NOMBRE	STOCK	LISTA 1	LISTA 2	LISTA 3	LISTA 4	CATEGORIA
    __codArtic = None
    __name = None
    __stock = None
    __price1 = None
    __price2 = None
    __price3 = None
    __price4 = None
    __category = None

    def __init__(self, cod, name, stock, list1, list2, list3, list4, category):
        self.__codArtic = cod
        self.__name = name
        self.__stock = stock
        self.__price1 = list1
        self.__price2 = list2
        self.__price3 = list3
        self.__price4 = list4
        self.__category = category
        
    # Getters
    def getCodArtic(self):
        return self.__codArtic

    def getName(self):
        return self.__name

    def getStock(self):
        return self.__stock

    def getPrice1(self):
        return self.__price1

    def getPrice2(self):
        return self.__price2

    def getPrice3(self):
        return self.__price3

    def getPrice4(self):
        return self.__price4

    def getCategory(self):
        return self.__category

    # Setters
    def setCodArtic(self, cod):
        self.__codArtic = cod

    def setName(self, name):
        self.__name = name

    def setStock(self, stock):
        self.__stock = stock

    def setPrice1(self, price1):
        self.__price1 = price1

    def setPrice2(self, price2):
        self.__price2 = price2

    def setPrice3(self, price3):
        self.__price3 = price3

    def setPrice4(self, price4):
        self.__price4 = price4

    def setCategory(self, category):
        self.__category = category

    
    def getData(self):
        #Identificador de URL	Nombre	Categorías	Precio	Precio promocional	Peso (kg)	Stock	SKU	Código de barras	Mostrar en tienda	Envío sin cargo	Descripción	Tags	Título para SEO	Descripción para SEO	Marca	Producto Físico	MPN (Número de pieza del fabricante)	Sexo	Rango de edad
        #Computadoras, Accesorios, Accesorios, Auriculares	0		0	1			SI	SI						SI		Unisex	Adulto
        urlName = self.getName().lower()
        for i in urlName:
            if(i == " "):
                urlName = urlName.replace(i, "-")
        price = 0
        for i in self.getPrice3():
            if(i == ","):
                price = self.getPrice3().split(",")

        price = int(price[0]) * 1.15           # 15% de impuestos
        price = round(price, 0)
        price = str(price)
        
        #promotionalPrice = price - (price * 0.5)
        promotionalPrice = '0'

        weight = '0'
        sku = self.getCodArtic()
        barcode = self.getCodArtic()
        showInStore = "SI"
        freeShipping = ""
        description = """
            <p><span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">Somos MAXSER. Empresa Sanjuanina dedicada a la venta y reparaci&oacute;n de equipos inform&aacute;ticos, m&aacute;s de 15 a&ntilde;os nos avalan en nuestra trayectoria, contando con personal especializado en cada sector nos centramos en brindar siempre el MAXimo SERvicio a nuestros clientes.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Contamos con amplia variedad de marcas y modelos.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Realizamos env&iacute;o a todo el pa&iacute;s.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Disponemos de factura A.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Precios acorde a lo que necesites.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- La mejor atenci&oacute;n.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- El mejor asesoramiento.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">HORARIOS DE ATENCI&Oacute;N:</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">* LUNES A VIERNES DE 09 A 21HS</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">* S&Aacute;BADOS DE 10 A 14HS</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">******* B&uacute;scanos y conoce m&aacute;s de nosotros en nuestras redes. *******</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">Consultar disponibilidad de stock, colores disponible y demas detalles por cada producto.</span></p>
        """
        tags = self.getName()
        title = self.getName()

        metaDescription = self.getName() + " - " + self.getCategory()
        brand = ""
        physicalProduct = "SI"
        mpn = ""
        sex = "Unisex"
        ageRange = ""

        return (
            urlName,
            self.__name,
            self.__category,
            price,
            promotionalPrice,
            weight,
            self.__stock,
            sku,
            barcode,
            showInStore,
            freeShipping,
            description,
            tags,
            title,
            metaDescription,
            brand,
            physicalProduct,
            mpn,
            sex,
            ageRange
        )