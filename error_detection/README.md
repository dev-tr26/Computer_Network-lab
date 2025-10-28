## 1. VRC (Vertical Redundancy Check)

- add parity bit according to even or odd
- Detects single-bit errors in each byte
- can't detect burst errors or even-no. bit errors (like flipping two bits)


## 2. LRC (Longitudinal Redundancy Check)

- arrange data in blocks 
- Adds one parity block calculated column-wise (parity across each bit position)
- Can detect some multi-bit and burst errors across rows and columns
- if even num bits inverted can't detect 

## 3. CRC (Cyclic Redundancy Check)

- data as a binary polynomial and divides it by a generator polynomial using mod-2 div
- remainder is the CRC code, appended to the message
- can detect burst errors, odd number of bit errors