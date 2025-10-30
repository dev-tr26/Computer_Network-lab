import time 

def sliding_window():
    w = int(input("Enter window size: "))
    f = int(input("Enter number of frames to transmit: "))
    
    print(f"Enter {f} frames: ", end="")
    frames = list(map(int, input().split()))

    print("Sliding-window protocol simulation")
    print("(assuming no corruption of frames)\n")
    print(f"Window size = {w}")
    print(f"Total Frames = {f}\n")
    
    for i in range(f):
        print(f"Frame {frames[i]} sent")
        time.sleep(1.5)
        if (i + 1) % w == 0:   
            print("\nAcknowledgement received for above frames\n")
            time.sleep(1)
    
    if f % w != 0:
        print("\nAcknowledgement of above frames sent is received by sender")

print("All frames transmitted successfully !!")

if __name__ == "__main__":
    sliding_window()
