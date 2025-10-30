import random , time

def selective_repeat_arq():
    total_frames = int(input("Enter total number of frames to send: "))
    window_size = int(input("Enter window size: "))
    
    frames = [ i + 1 for i in range(total_frames)]
    acknoledged_frames = [False] * total_frames 
    
    i = 0
    while (i < total_frames):
        print(f"Transmitting frames in window: {frames[i:i+window_size]}")
        
        for j in range(min(i + window_size, total_frames)):
            if not acknoledged_frames[j]:
                print(f"Sender: Sending Frame {frames[j]}")
                time.sleep(0.5)
                
                # Random if frame is received or lost
                
                if random.choice([True, True, False]):  
                    print(f"Receiver: Frame {frames[j]} received .")
                    print(f"Receiver: Sending ACK {frames[j]}")
                    acknoledged_frames[j] = True
                else:
                    print(f"Frame {frames[j]} lost.")
            time.sleep(0.5)
        
        print("\nChecking acknowledgments...")
        time.sleep(1)
        
        # Slide the window to the next unacknowledged frame
        while(i < total_frames and acknoledged_frames[i]):
            i += 1
        
        print(f"Next window starts from frame {i + 1}\n")
        time.sleep(1)
        
    print("all frames transmitted")
    


if __name__ == "__main__":
    selective_repeat_arq()
    