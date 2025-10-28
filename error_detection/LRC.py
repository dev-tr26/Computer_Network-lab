def lrc_generate(message, block_size, parity_type='even'):
    print(f"\nOriginal Message: {message}")
    print(f"Block size: {block_size}, Parity type: {parity_type}")

    # Split message into rows 
    
    rows = [] 
    for i in range(0, len(message), block_size):
        row = message[i:i + block_size]
        rows.append(row)
        
    print("\nDividing message into rows:")
    
    for idx, row in enumerate(rows, start=1):
        print(f"Row {idx}: {row}")

    # padding with 0 if needed 
    
    if len(rows[-1]) < block_size:
        padding = [0] * (block_size - len(rows[-1]))
        rows[-1].extend(padding)
        print(f"Padding last row with zeros: {rows[-1]}")


    # convert each block to int
    block_values = []
    for row in rows:
        block_val = int("".join(map(str,row)),2)
        block_values.append(block_val)
    
    print(f"Block intger values",block_values)
    
    # adding all blocks 
    total= sum(block_values)
    print(f"Sum of all blocks", total) 

    # finding remainder after dividing by 2^block_Size 
    
    mod_value = 2 ** block_size
    remainder = total%mod_value
    print(f"Remainder after mod {mod_value}:", remainder)
    
    # taking 1s compliment 
    lrc_Value =  mod_value -1 -remainder
    print(f"LRC after 1s comp.",lrc_Value)
    lrc_bits = [int(bit) for bit in f"{lrc_Value:0{block_size}b}"]

    final_msg = message + lrc_bits
    print(f"Final msg with LRC", final_msg)

    return final_msg




def lrc_checksum(received_message, block_size, parity_type='even'):
   
    print(f"Received Message: {received_message}")
    print(f"Block size: {block_size}, Parity type: {parity_type}")


    rows = []
    for i in range(0, len(received_message), block_size):
        row = received_message[i:i + block_size]
        rows.append(row)
    

    print("\nBlocks (including LRC):")
    for i, row in enumerate(rows, 1):
        print(f" Block {i}: {row}")
        
        
    block_values = []
    for row in rows:
        binary_string = "".join(str(bit) for bit in row)
        block_value = int(binary_string, 2)
        block_values.append(block_value)
    
    
    print("\nBlock values:", block_values)

    # Add all blocks
    total = sum(block_values)
    mod_value = 2 ** block_size
    remainder = total % mod_value
    print(f"Total sum mod {mod_value}: {remainder} ({bin(remainder)[2:].zfill(block_size)})")


    if remainder == mod_value - 1:
        print("msg is valid ")
    else:
        print("msg is invalid")
  
  

message = [1, 0, 1,1,0,0,1,1,1,0,1,0]
block_size = 4

# sender side 

sent_message = lrc_generate(message, block_size)

# Receiver side (correct message)
lrc_checksum(sent_message, block_size)

# Receiver side (simulate error)
corrupted = sent_message.copy()
corrupted[5] = 1  # flip a bit
lrc_checksum(corrupted, block_size)