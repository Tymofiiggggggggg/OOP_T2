from abc import ABC, abstractmethod

# Принцип відкритості/закритості: ми можемо додавати нові типи працівників, не змінюючи існуючий код.
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Принцип єдиної відповідальності: окремий клас відповідає тільки за друк зарплати
class SalaryPrinter:
    def print_salary(self, employee: Employee):
        print(f"Зарплата: {employee.calculate_salary()} грн")

# Основна частина програми
if __name__ == "__main__":
    emp1 = FullTimeEmployee(15000)
    emp2 = HourlyEmployee(100, 80)

    printer = SalaryPrinter()
    printer.print_salary(emp1)
    printer.print_salary(emp2)
