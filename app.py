from bottle import route, post, request, run
import subprocess, os, json, sys

CONFIG_FILE = 'config.json'

"""
Open and load a file at the json format
"""

def open_and_load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            return json.loads(config_file.read())
    else:
        print("File [%s] doesn't exist, aborting." % (CONFIG_FILE))
        sys.exit(1)


@route('/')
def hello():
    return "Reboot API"

@route('/load')
def load():
    return "%s, %s, %s" % os.getloadavg()

@route('/<key>/reboot')
def pull(key):
    if (key != config["key"]):
        return "ko"
    postdata = request.json
    status = postdata['heartbeat']['status']
    print("STATUS: %s" % status)
    if (status == 0):
        os.chdir(config["path"]);
        subprocess.call(config["cmd"])
    return "ok"

@post('/<key>/test')
def pull(key):
    if (key != config["key"]):
        return "ko"
    postdata = request.json
    status = postdata['heartbeat']['status']
    print("STATUS: %s" % status)
    if (status == 0):
        print("Reboot needed")
    return "ok"

if __name__ == "__main__":
    config = open_and_load_config()
    run(host=config["host"], port=config["port"], debug=config["debug"])
