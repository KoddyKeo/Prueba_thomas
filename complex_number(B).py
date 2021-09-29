import cmath


class ComplexNumber:
    def __init__(self, number_a, complex_a, number_b, complex_b):
        self.number_a = complex(float(number_a), float(complex_a))
        self.number_b = complex(float(number_b), float(complex_b))

    def process_number(self):
        try:
            vals = {}
            sum = vals['sum'] = self.number_a + self.number_b
            subtraction = vals['subtraction'] = self.number_a - self.number_b
            multiplication = vals['multiplication'] = self.number_a * self.number_b
            division = vals['division'] = self.number_a / self.number_b
            module_a = vals['module_a'] = cmath.sqrt((self.number_a.real) ** 2 + (self.number_b.imag) ** 2)
            module_b = vals['module_b'] = cmath.sqrt((self.number_a.real) ** 2 + (self.number_b.imag) ** 2)

            print(
                f" \n Resultado: \n Suma: {sum} \n Resta: {subtraction} \n Multiplicación: {multiplication} \n División: {division} \n Mod A: {module_a} \n Mod B: {module_b}")

        except:
            print("Error")


def main():
    number_a = input("Primer Número Real: ")
    complex_a = input("Primer Número Imaginario: ")
    number_b = input("Segundo Número Real : ")
    complex_b = input("Segundo Número Imaginario: ")

    complex_number = ComplexNumber(number_a, complex_a, number_b, complex_b)
    complex_number.process_number()


if __name__ == '__main__':
    main()
