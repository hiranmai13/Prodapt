from typing import Union

def process_input(data: Union[str, bytes])->None:
    if isinstance(data,str):
        print("Processing Text:",data)
    elif isinstance(data, bytes):
        print("Processing Image/Audio Bytes: ",data)

print(process_input("Artificial Intelligence"))

print(process_input(b'\x89PNG\r\n'))
