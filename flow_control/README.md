## FLOW CONTROL 

- prevents buffer overflow at receiver end maintain smooth data transfer
- operates at Data Link Layer 

# - algorithms : 

1. Stop and wait 

- sender sends one frame and waits for acknoeledgement before sending next 
- simple , reliable, inefficient for long-distance

2. Sliding window 

- sender can send muiltiple frames before needing acknoledgement , window_size (how many frames can be sent w/o waiting)
- receiver also maintain window size to accept frames 
- better link utilization, continuous data transmission 
