import json #Use esta libreria para indentar la información y que fuera de facil entendimiento
from os import getcwd


class Product:
    def __init__(self, name, barcode, manufacturer, category, gender, id):
        self.name = name
        self.bar_code = barcode
        self.manufacturer = manufacturer
        self.category = category
        self.gender = gender
        self.id = id


class SorterProducts:
    def __init__(self, products):
        self.products = products

    def process_sorter(self):
        try:
            vals = {}
            manufacturers = []

            for product in self.products:
                manufacturers.append(product.manufacturer)

            for manufacturer in manufacturers:
                vals.update(self.manufacturer(manufacturer))

            sorter_products = json.dumps(vals, indent=4)

            document = open('sorter_products.txt', 'w')

            document.write(sorter_products)
            document.close()
            path = getcwd()
            print(f"Ubicación del archivo {path}/{document.name}")

        except:
            print('Error')

    def manufacturer(self, manufacturer):
        vals = {}
        categories = []

        products = list(filter(lambda product: product.manufacturer == manufacturer, self.products))

        for product in products:
            if product.category not in categories:
                categories.append(product.category)

        for category in categories:
            vals.update(self.category(products, category))
        return {manufacturer: vals}

    def category(self, products, category):
        vals = {}
        genders = []

        products = list(filter(lambda product: product.category == category, products))
        for product in products:
            if product.gender not in genders:
                genders.append(product.gender)

        for gender in genders:
            vals.update(self.gender(products, gender))

        return {category: vals}

    def gender(self, products, gender):
        list = []
        for product in products:
            if product.gender == gender:
                list.append(product.id)
        return {gender: list}


class main():
    products = []

    product_1 = Product('Zapatos XYZ', '8569741233658', 'Deportes XYZ', 'Zapatos', 'Masculino', 'Producto 1')
    products.append(product_1)
    product_2 = Product('Zapatos ABC', '7452136985471', 'Deportes XYZ', 'Zapatos', 'Femenino', 'Producto 2')
    products.append(product_2)
    product_3 = Product('Camisa DEF', '5236412896324', 'Deportes XYZ', 'Camisas', 'Masculino', 'producto 3')
    products.append(product_3)
    product_4 = Product('Bolso KLM', '5863219635478', 'Carteras Hi-Fashion', 'Bolsos', 'Femenino', 'producto 4')
    products.append(product_4)

    sorter_products = SorterProducts(products)
    sorter_products.process_sorter()


if __name__ == '__main__':
    main()
