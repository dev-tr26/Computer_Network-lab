def xor(dividend, divisor):
    result = []
    for i in range(1, len(divisor)):
        result.append(dividend[i] ^ divisor[i])
    return result   


def division(msg, gen):
    n = len(gen)
    print(f"initial msg: {msg}")
    print(f"generator polynomial: {gen}")
    print(f"generator len n: {n}\n")
    temp = msg[:n]
    print(f"Initial segment: {temp}")

    # div
    for i in range(len(msg) - n + 1):
        print(f"Current temp: {temp}")
        
        if temp[0] == 1:
            print(f"  MSB is 1 => XOR with generator: {gen}")
            temp = xor(temp, gen)
        else:
            print(f"  MSB is 0 => XOR with zeros: {[0] * n}")
            temp = xor(temp, [0] * n)
        
        print(f"  after XOR: {temp}")
        if i + n < len(msg):
            next_bit = msg[i + n]
            temp.append(next_bit)
            print(f" append next msg bit ({next_bit}): {temp}")
        
        if len(temp) > n:
            temp = temp[1:]

    print(f"\nFinal remainder: {temp}")
    return temp



# Sender Side
print("At Senders Side")

n = int(input("Enter no of msg bits: "))
r = int(input("Enter no of generator bits: "))

print("Enter msg bits:")
msg = list(map(int, input().split()))
print("Enter generator bits:")
gen = list(map(int, input().split()))

# Append r-1 zeros to msg
crc_len = r - 1
appended_msg = msg + [0] * crc_len

# Get CRC
remainder = division(appended_msg, gen)
crc = remainder
print("CRC:", ' '.join(map(str, crc)))

transmitted = msg + crc
print("Transmitted Message:", ' '.join(map(str, transmitted)))

# Receiver Side
print("\nReceiver's End")
print("Enter received msg bits :")

received = list(map(int, input().split()))

# error checking 
remainder = division(received, gen)
if any(remainder):
    print("Error detected in received message.")
else:
    print("No error in received message.")
    print("Received Message:", ' '.join(map(str, received[:n])))