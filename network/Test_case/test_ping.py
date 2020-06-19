import os
sub=os.popen("ping 192.126.0.119")
result=sub.read()
if "100%" in result:
    print("111")