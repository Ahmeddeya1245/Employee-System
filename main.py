class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        return f"ID : {self.emp_id}, Name : {self.name}, Position : {self.position}, Salary : {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, position, salary):
        new_employee = Employee(emp_id, name, position, salary)
        self.employees.append(new_employee)

    def remove_emp(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                return f"Employee {emp.name} has been removed"
        return "Employee not found"

    def list_employees(self):
        return [emp.get_details() for emp in self.employees]

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if name == emp.name:
                return f"Employee {emp.name} is found. Information: {emp.get_details()}"
        return "Employee not found"

    def update_salary_by_name(self, name, salary):
        for emp in self.employees:
            if name == emp.name:
                emp.salary = salary
                return f"Salary for {name} has been updated!"
        return "Employee not found"


class Frontend:
    def __init__(self):
        self.manager = EmployeeManager()

    def menu(self):
        print("1) Add new employee")
        print("2) Remove employee")
        print("3) List all employees")
        print("4) Find employee by name")
        print("5) Update salary by name")
        print("0) Exit")

    def run(self):
        while True:
            self.menu()
            option = int(input("Enter a number between 0 to 5: "))
            if option == 1:
                emp_id = int(input("Enter employee ID: "))
                name = input("Enter employee name: ")
                position = input("Enter employee position: ")
                salary = float(input("Enter employee salary: "))
                self.manager.add_employee(emp_id, name, position, salary)
                print("Employee added successfully!")
            elif option == 2:
                emp_id = int(input("Enter employee ID to remove: "))
                print(self.manager.remove_emp(emp_id))
            elif option == 3:
                employees = self.manager.list_employees()
                print("\n".join(employees) if employees else "No employees found")
            elif option == 4:
                name = input("Enter the name of the employee to find: ")
                print(self.manager.find_employee_by_name(name))
            elif option == 5:
                name = input("Enter the name of the employee to update salary: ")
                salary = float(input("Enter new salary: "))
                print(self.manager.update_salary_by_name(name, salary))
            elif option == 0:
                print("Exiting...")
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    app = Frontend()
    app.run()
