from linkkit import linkkit
import time
from pi_info import *



def on_device_dynamic_register(rc, value, userdata):
    if rc == 0:
        print("dynamic register device success, rc:%d, value:%s" % (rc, value))
    else:
        print("dynamic register device fail,rc:%d, value:%s" % (rc, value))
# lk.on_device_dynamic_register = on_device_dynamic_register

def on_connect(session_flag, rc, userdata):
    print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))
    pass
def on_disconnect(rc, userdata):
    print("on_disconnect:rc:%d,userdata:" % rc)


lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="",
    device_name="",
    device_secret="",
    product_secret="")

lk.thing_setup("model.json") #配置文件 

lk.on_connect = on_connect
lk.on_disconnect = on_disconnect

lk.connect_async()
lk.start_worker_loop()
time.sleep(5)

while(1):
    pass

