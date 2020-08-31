from multiprocessing import Process,Manager
from flask import Flask,request
from led_control import LedControl

LED_COUNT = 256

app = Flask(__name__)
cmd_queue = Manager().Queue()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/led')
def led():
    mod = request.args.get('m', '0')
    function = request.args.get('f','0')
    led_row = request.args.get('r','0')
    led_column = request.args.get('c','0')
    cycle = request.args.get('k','0')
    delay = request.args.get('d','0')
    data = {"mod":int(mod),"function":int(function),"led_row":int(led_row),
            "led_column":int(led_column),"cycle":int(cycle),"delay":int(delay)}
    cmd_queue.put(data)
    return "recieve"

def _light(cmd_queue):
    led_control = LedControl(32,8,2)
    while(True):
        led_control.light()
        try:
            data = cmd_queue.get(True,0.01)
        except:
            pass
        else:
            led_control.del_cmd(data)
            

if __name__ == '__main__':

    data = {"mod":1,"function":7, "cycle":1,"delay":1}
    cmd_queue.put(data)
#    data = {"mod":1,"function":6, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":5, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":4, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":3, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":2, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":1, "cycle":1,"delay":1}
#    cmd_queue.put(data)
#    data = {"mod":1,"function":0, "cycle":1,"delay":1}
#    cmd_queue.put(data)

    process = Process(target=_light,args=(cmd_queue,))
    process.daemon = True
    process.start()
    app.run(host='0.0.0.0')