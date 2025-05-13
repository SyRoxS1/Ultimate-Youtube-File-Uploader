def file_to_binary_string(file_path):
    with open(file_path, 'rb') as file:
        while True:
            binary_code = file.read(28000)
            binary_string = ''.join(format(byte, '08b') for byte in binary_code)
            if not binary_code:
                break
        






def binary_string_to_file(binary_string, file_path):
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)





def append_binary_chunk_to_file(binary_chunk, file_path):
    # If input is a list of ints, convert it to a string of '0' and '1'
    if isinstance(binary_chunk, list):
        binary_chunk = ''.join(str(bit) for bit in binary_chunk)
    

    with open(file_path, 'ab') as file:  # 'ab' = append in binary mode
        bytes_list = [int(binary_chunk[i:i+8], 2) for i in range(0, len(binary_chunk), 8)]
        file.write(bytearray(bytes_list))

