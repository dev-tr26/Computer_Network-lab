import time 

def stop_and_wait():
    n = int(input("Enter no of frames to send: "))
    print(f"Enter {n} frames: ", end=" ")
    frames = list(map(int, input().split()))
    
    print("Stop and wait protocol simulation ")
    print("assuming no loss of frames")
    
    for i in range(n):
        print(f"Sender :sending Frame {frames[i]}...")
        time.sleep(1.5)
        
        print(f"Receiver: Frame {frames[i]} received succesfully.")
        time.sleep(1)
        
        print(f"Receiver: Sending ack for frame {frames[i]}")
        time.sleep(1)
        print(f"Sender: ack for frame{frames[i]} received.\n")
        
    print("All frames received successfully")


if __name__ == "__main__":
    stop_and_wait()