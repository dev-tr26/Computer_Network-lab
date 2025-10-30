## 1. Stop-and-Wait-ARQ 

- error control protocol
- purpose: to provide reliable data transfer over noisy channel 
- it is done by keeping a copy of sent frame and automatic retransmitting of frame when timer expires
- we use Seq_num to number frames based on mod 2

---
input n : total no of frames 
i = 1
while (true){
   send frame[i]
   start timer
   wait for ack or timeout
   if (ACK received before timeout)
      i = i + 1
      prtint(ACK  for frame[i] received)
   else 
      print(Timeout retransmit frame)

print(All frames ransmitted succesfully)
}
---

## 2. Go-Back-N

- the seq numbers are mod 2^m (m = size of seq num field in bits)
- Uses a sliding window; can send multiple frames before needing ACK. 
- If an error occurs, retransmits from that frame and all after it.
- high efficiency but more retransmissions 

---
total_frames = n
window_size = w
curr_frame =1 
next_frame = 1
ack[1..n] = False

while(not all ack received){
    // send frame within window
    while(next_frame < curr_frame + window_size && next_frame < n>){
        SEND frame[next_frame]
        START timer[next_frame]
        nrxt_ftame +=1
    }

    // wait for ACK

    if(ACK recived for frame i or timeout){
        ack[i] = true
        print(Ack for frame[i] received)

        while(ack[curr_frame]= True && curr_frame < n){
            curr_frame = curr_frame + 1
        }
    }
    // timeout occur for curr frame 
    else{
        print(Timeout occured for curr_frame)
        print(retransmitting frame)
        next_frame = next_frame - 1
        for(i=curr_frame to next_frame-1){
            send frame[i]
            RESTART timer[i]
        } 
    }
}

---


## 3. Selective-Repeat-ARQ 

- uses sliding window retransmits specific frame only which has error 
- size of sender and receiver window must be atmost half of 2^m 
- frames in transit upto window size w
- individual acks received 
