from flask import Flask, render_template, url_for
import subprocess
import os
import datetime
import time
app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/omx/")
def omx():
   #subprocess.call(['./omxlive.sh'], shell=True)
   cmd = ["/usr/bin/testami_commit"]
   p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
   out,err = p.communicate()
   return out




#@app.route("/omxstop/")
#def omxstop():
#subprocess.call(['./omxstop.sh'], shell=True)


if __name__ == "__main__":
   app.run(host='157.27.6.90', port=80, debug=True)


