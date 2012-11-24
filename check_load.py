import subprocess
print("enter number of clicks to make")
hits=input();
for i in range(int(hits)):
    subprocess.Popen(['python3','/home/mihir/site-hits/site_hit_script.py']) #execute the script as a new process
