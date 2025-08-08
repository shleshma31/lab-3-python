# 1
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_user("Aaryan")

# 2
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# 3
def book_info(title, author, year):
    print(f"Title: {title}, Author: {author}, Year: {year}")

book_info(author="George Orwell", title="1984", year=1949)
book_info(year=2005, author="Dan Brown", title="The Da Vinci Code")

# 4
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(2, 3))
print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20, 30))

# 5
def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_profile(name="Alice", age=20, grade="A")

# 6
square = lambda x: x ** 2
print(square(5))
print(square(12))

# 7
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# 8
nums2 = [10, 15, 20, 25, 30]
divisible_by_10 = list(filter(lambda x: x % 10 == 0, nums2))
print(divisible_by_10)

# 9
temps_c = [36.5, 37.0, 39.2, 35.6, 38.7]
temps_f = list(map(lambda c: c * 9/5 + 32, temps_c))
below_100 = list(filter(lambda f: f <= 100, temps_f))
print(temps_f)
print(below_100)

# Mini Project
def add_task(task_list, task_name):
    task_list.append({"name": task_name, "completed": False})
    return task_list

list_pending = lambda tasks: list(filter(lambda t: not t["completed"], tasks))
complete_all = lambda tasks: list(map(lambda t: {**t, "completed": True}, tasks))
search_tasks = lambda tasks, keyword: list(filter(lambda t: keyword.lower() in t["name"].lower(), tasks))

tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
print("Pending Tasks:", list_pending(tasks))
tasks = complete_all(tasks)
print("Search Result:", search_tasks(tasks, "call"))
