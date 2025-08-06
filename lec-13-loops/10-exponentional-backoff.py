import time

wait_time=1 
retries=5

for attepmt in range(1,retries+1):
    print(f"Attepmt: {attepmt}, waiting {wait_time}seconds ")
    time.sleep(wait_time)
    wait_time*=2