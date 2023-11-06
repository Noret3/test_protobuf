import person_pb2
import json
import base64
import bson
import sys
import pickle
from Person import *
import flatbuffers
import time
from functools import wraps


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} execute {execution_time}")
        return result

    return wrapper

    # PROTOBUF


person = person_pb2.Person()
person.name = "Alice"
person.age = 30
serialized_data = person.SerializeToString()

# FLATBUFFER
builder = flatbuffers.Builder(1024)
name = builder.CreateString("Alice")
PersonStart(builder)
PersonAddAge(builder, 30)
PersonAddName(builder, name)
my_data = PersonEnd(builder)
builder.Finish(my_data)
flatbuffers_data = builder.Output()

data_for_serialization = {"name": "Alice", "age": 30}

json_data = json.dumps(data_for_serialization)
clear_dict_size = sys.getsizeof(data_for_serialization)
dict_str_size = sys.getsizeof(str(data_for_serialization))
pickle_size = sys.getsizeof(pickle.dumps(data_for_serialization))
json_size = sys.getsizeof(json.dumps(data_for_serialization))
json_bytes_size = sys.getsizeof(json.dumps(data_for_serialization).encode('utf-8'))
b64_pickle_size = sys.getsizeof(base64.b64encode(pickle.dumps(data_for_serialization)))
b64_json_bytes_size = sys.getsizeof(base64.b64encode(json.dumps(data_for_serialization).encode('utf-8')))
bson_size = sys.getsizeof(bson.BSON.encode(data_for_serialization))
protobuf_size = sys.getsizeof(serialized_data)
flatbuffers_size = sys.getsizeof(flatbuffers_data)
flatbuffers_size_bytes = sys.getsizeof(bytes(flatbuffers_data))

data_for_output = {
    "Dict": clear_dict_size,
    "Str dict": dict_str_size,
    "Pickle": pickle_size,
    "Json": json_size,
    "Json bytes": json_bytes_size,
    "Base64 pickle": b64_pickle_size,
    "Base64 json bytes": b64_json_bytes_size,
    "Bson": bson_size,
    "Protobuf": protobuf_size,
    "Flatbuffer": flatbuffers_size,
    "Flatbuffer bytes": flatbuffers_size_bytes,
}
max_len = max(len(key) for key in data_for_output.keys())
for key, value in data_for_output.items():
    print(f"{key.ljust(max_len)}: {value} bytes")
print(f"Dict: {clear_dict_size}")
print(f"Str dict: {dict_str_size}")
print(f"Pickle: {pickle_size}")
print(f"Json: {json_size}")
print(f"Json bytes: {json_bytes_size}")
print(f"Base64 pickle: {b64_pickle_size}")
print(f"Base64 json bytes: {b64_json_bytes_size}")
print(f"Bson: {bson_size}")
print(f"Protobuf: {protobuf_size}")
print(f"Flatbuffer: {flatbuffers_size}")
print(f"Flatbuffer bytes: {flatbuffers_size_bytes}")

pik_dat = pickle.dumps(data_for_serialization)
bson_dat = bson.BSON.encode(data_for_serialization)


@profile
def serialize_protobuf():
    result = person.SerializeToString()


@profile
def deserialize_protobuf():
    person = person_pb2.Person()
    person.ParseFromString(serialized_data)


@profile
def jsonalize():
    result = json.dumps(data_for_serialization)
    result_b = result.encode("utf-8")


@profile
def dejsonalize():
    result = json.loads(json_data)


@profile
def picklalize():
    result = pickle.dumps(data_for_serialization)


@profile
def depicklalize():
    result = pickle.loads(pik_dat)


@profile
def bsonalize():
    result = bson.BSON.encode(data_for_serialization)


@profile
def debsonalize():
    result = bson.BSON.decode(bson_dat)


serialize_protobuf()
deserialize_protobuf()
jsonalize()
dejsonalize()
picklalize()
depicklalize()
bsonalize()
debsonalize()
