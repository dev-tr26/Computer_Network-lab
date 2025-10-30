import random
import time

def go_back_n_arq():
    total_frames = int(input("Enter total number of frames to send: "))
    window_size = int(input("Enter window size: "))


    curr = 0      
    next_frame = 0   
    frames = [i + 1 for i in range(total_frames)]
    acknowledged = [False] * total_frames

    while curr < total_frames:
        # Send frames within the window
        while next_frame < curr + window_size and next_frame < total_frames:
            print(f"Sender: Sending Frame {frames[next_frame]}")
            time.sleep(0.5)
            next_frame += 1

        # Random frame loss
        lost_frame = random.choice(range(curr, min(next_frame, total_frames)))
        print(f" Frame {frames[lost_frame]} lost")
        time.sleep(1)

        # retransmiting lost frame
        print(f"Sender: Timeout. Retransmitting from Frame {frames[lost_frame]}.")
        next_frame = lost_frame

        for i in range(next_frame, min(next_frame + window_size, total_frames)):
            print(f"Sender: Resending Frame {frames[i]}")
            time.sleep(0.5)
            print(f"Receiver: Frame {frames[i]} received .")
            print(f"Receiver: Sending ACK {frames[i]}")
            acknowledged[i] = True
            time.sleep(0.5)

        # Slide window
        while curr < total_frames and acknowledged[curr]:
            curr += 1
        print(f"Sliding window, Next frame to send: {curr + 1}\n")
        time.sleep(1)

    print("All frames transmitted.")

if __name__ == "__main__":
    go_back_n_arq()
