import random
import time

def stop_and_wait_arq():
    n = int(input("Enter the number of frames to send: "))
    i = 1
    while i <= n:
        print(f"Sender: Sending Frame {i}.")
        time.sleep(1)

        success = random.choice([True, True, False])

        if success:
            print(f"Receiver: Frame {i} received.")
            print(f"Receiver: Sending ACK {i}")
            time.sleep(1)
            print(f"Sender: ACK {i} received.\n")
            i += 1
        else:
            print(f"Frame {i} lost / timeout retransmitting.")
            time.sleep(1)

    print("all frames transmitted. ")


if __name__ == "__main__":
    stop_and_wait_arq()
