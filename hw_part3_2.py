# Create a class to convert temperature from Celsius to
# Fahrenheit, and vice versa. The class must have two static
# methods: to convert from Celsius to Fahrenheit and from
# Fahrenheit to Celsius. The class should also count how many
# times the temperature was calculated and return this value
# using a static method.

class TemperatureConversion:
    conversion_counter = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConversion.conversion_counter += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConversion.conversion_counter += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConversion.conversion_counter


print(TemperatureConversion.celsius_to_fahrenheit(0))
print(TemperatureConversion.celsius_to_fahrenheit(100))
print(TemperatureConversion.fahrenheit_to_celsius(212))
print(TemperatureConversion.fahrenheit_to_celsius(100))
print()
print(f"Number of conversions: {TemperatureConversion.get_conversion_count()}")

