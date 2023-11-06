# PROTOBUF

1. Install protobuf compiler `sudo apt install protobuf-compiler`
2. Create a file with extension `.proto`
3. Fill file with example 
>syntax = "proto3";
>
>message Person {
>  string name = 1;
>  int32 age = 2;
>}

4. Environment variable should be set `export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python  `
5. Compile proto file into python `protoc --python_out=. {file_name}.proto`
6. For serialization follow code below:
> person = person_pb2.Person()\
> person.name = "Alice"\
> person.age = 30\
> serialized_data = person.SerializeToString()
7. For deserialization follow code below:
> person = person_pb2.Person()\
> person.ParseFromString(serialized_data)