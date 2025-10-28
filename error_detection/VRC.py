def vrc_generate(msg, parity_type='even'):
    
    print(f"\nOriginal msg: {msg}")
    print(f"Selected parity type: {parity_type}")

    # no. of 1's in msg
    count_ones = msg.count(1)
    print(f"No of 1's in message: {count_ones}")

    # Generate parity bit 
    if parity_type == 'even':
        parity_bit = 0 if count_ones % 2 == 0 else 1
    elif parity_type == 'odd':
        parity_bit = 1 if count_ones % 2 == 0 else 0
    else:
        raise ValueError("Invalid parity type. Use 'even' or 'odd'.")

    print(f"Generated parity bit: {parity_bit}")


    msg_with_parity = msg + [parity_bit]
    print(f"Msg with parity bit appended: {msg_with_parity}\n")

    return msg_with_parity


def vrc_check(received_msg, parity_type='even'):
    print(f"\nReceived message: {received_msg}")
    print(f"Selected parity type: {parity_type}")

    count_ones = received_msg.count(1)
    print(f"Number of 1's (including parity bit): {count_ones}")

    # Check parity
    if parity_type == 'even':
        valid = count_ones % 2 == 0
    elif parity_type == 'odd':
        valid = count_ones % 2 != 0
    else:
        raise ValueError("Invalid parity type. Use 'even' or 'odd'.")

    if valid:
        print("msg is Valid")
    else:
        print("Msg is Invalid")

    return valid


msg = [1, 0, 1, 1, 0, 1]
sent_msg = vrc_generate(msg, parity_type='even')
vrc_check(sent_msg, parity_type='even')
corrupted_msg = sent_msg.copy()
corrupted_msg[2] = 0  
vrc_check(corrupted_msg, parity_type='even')
