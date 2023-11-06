from Person import *
import flatbuffers
import sys
# Создайте объект Person
builder = flatbuffers.Builder(1024)
name = builder.CreateString("Alice")
PersonStart(builder)
PersonAddAge(builder, 30)
PersonAddName(builder, name)
my_data = PersonEnd(builder)

builder.Finish(my_data)
data = builder.Output()
print(data)
print(type(data))
print(type(bytes(data)))
print(bytes(data))
size = sys.getsizeof(data)
size1 = sys.getsizeof(bytes(data))
print(size)
print(size1)
# Десериализация данных
my_data = Person.GetRootAsPerson(data, 0)
id = my_data.Age()
name = my_data.Name().decode('utf-8')

print(f"ID: {id}, Name: {name}")
