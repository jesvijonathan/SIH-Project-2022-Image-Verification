from flask import Flask, redirect, url_for, request, render_template, make_response, send_from_directory
from flask_mail import * 
from flask import jsonify
import json
import datetime
import pickle 
import os
from werkzeug.utils import secure_filename
# from uritemplate.api import expand 

cwd = os.getcwd()
UPLOAD_FOLDER_1 = (cwd + '\\resource\\passport_size_photo\\')
UPLOAD_FOLDER_2 = (cwd + '\\resource\\signature_photo\\')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_1

data = {
   'log_no' : 0,
   'dic_log' : False,   
}

@app.route("/")
def index():
   log(request.environ)
   title = "Jesvi Jonathan"
   description = "Jesvi's Official Webpage"

   return render_template(
      'index.html',
      
      title = title,
      description = description
      )

@app.route('/upload', methods=['POST'])
def upload():
    try:
        imagefile = Flask.request.files.get('imagefile', '')
        ...
    except Exception as err:
       print(err)

@app.route('/upload2', methods=['POST'])
def upload2():
    print('___________________',request.files['file'])
    file = request.files['file']
    file2 = request.files['file2']
    filename = secure_filename(file.filename)
    filename2 = secure_filename(file2.filename)
    file.save(UPLOAD_FOLDER_1 + "\\" + filename)
    file.save(UPLOAD_FOLDER_2 + "\\" + filename2)
    return "DONE"

ip = []
l = "\n"

try:
   with open('data.pickle', 'rb') as handle:
      data = pickle.load(handle)
   l += "-Data Loaded\n"
except:
   l += "-Reset Data (Failed To Load Data)"
   with open('data.pickle', 'wb') as handle:
      pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

try:
   with open('ip.pickle', 'rb') as handle:
      ip = pickle.load(handle)
   l += "-IP List Loaded\n"
except : 
   with open('ip.pickle', 'wb') as handle:
      pickle.dump(ip, handle, protocol=pickle.HIGHEST_PROTOCOL)
   l+= "-Reset IP List (Failed To Load Ip List)\n"

print(l)

def save_ip_list():
   try:
      with open('ip.pickle', 'wb') as handle:
         pickle.dump(ip, handle, protocol=pickle.HIGHEST_PROTOCOL)
      return "-IP List Saved"
   except:
      return "-Failed To Save IP List"

def save_data():
   try:
      with open('data.pickle', 'wb') as handle:
         pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
      return "-Data Saved"
   except:
      return "-Failed To Save Data"


@app.route('/ltest')
def log(x=None):
   log_text =None
   
   if x == None:
      x = request.environ 
      
   msg = ""
   
   dl = data['dic_log']

   if dl == True:
      try:
         lfile = open("./static/dic_log.txt", "a+")
         lfile.write("\n\n")
      except:
         msg += "Failed To Open dic_log.txt\n"
         print(msg)
   
   try:
      slog = open("./static/log.txt", "a+")
   except: 
      slog = open("/home/jesvi/jesvijonathan/static/log.txt", "a+")
 
   
   try:
      data['log_no']+=1   
      log_id = str(data['log_no'])
      save_data()

      if request.headers.getlist("X-Forwarded-For"):
         uip = request.headers.getlist("X-Forwarded-For")[0]
      else:
         try:
            uip = request.remote_addr
         except:
            uip = x['REMOTE_ADDR']
      # print(request.headers['X-Real-IP'])
      
      ip_exists = False

      if uip in ip:
         ip_exists = True
         ip_text = ""
      else:
         ip.append(uip)
         print(save_ip_list())
         ip_text = " [New_IP] "

      

      
      log_time = str(datetime.datetime.now().strftime("%x %X"))
      
      hua_text = str(x['HTTP_USER_AGENT'])
      device = hua_text[(hua_text.find("(")+1):(hua_text.find(")"))]

      uip = str(uip)
      user_ip =  uip + " :" + str(x['REMOTE_PORT'])

      # req_str = str(x['werkzeug.request'])
      # ind1 = req_str.find(" ")
      # in1 = req_str[1:ind1]
      # in2 = req_str[ind1+1:] 
      # ind2 = in2.find(" ")
      # in2 = in2[:ind2 ]
      # in3 = str(x['REQUEST_METHOD'])

      # user_request = in2 + "; " + in1 + "; " + in3 
      user_request = str(x['werkzeug.request'])
      #server = str(x['HTTP_HOST'])

      log_text = (
         "\n[" + log_id  + "] " +
         "[" + log_time +  "] " + 
         "[" + user_ip + "]" + ip_text + " " +
         "[" + device + "] " + 
         "[" + user_request + "] " #+
         #"[" + server + "]"
      )      

      slog.write("")
      slog.write(log_text)
      print(log_text,"\n")

      if dl == True:
         x = { 
            'id':log_id,
            'time':log_time,
            'ip': uip,
            'ip_exists':ip_exists,
            'data' : x,
            }
         o = json.dumps(x, indent=4, default=str)

         lfile.write(o)
         lfile.close()
 
   except Exception as e:
      print(e)

   if x== None:
      return True
   else:
      return render_template('debug.html', here=log_text)



@app.route('/logger/<live>')
@app.route('/logger')
def logg(live=None):
   print(live)
   
   l = file = None

   try:
      with open('./static/log.txt', 'r') as file:
         l = file.read()
   except:
      with open('/home/jesvi/jesvijonathan/static/log.txt', 'r') as file:
         l = file.read()

   # print(l)
   meta = meta_time = ""
   if live!=None:
      meta = "refresh"
      meta_time = live

   return render_template('debug.html',n=l, script="1",style="body {font-size: 14px;}", meta=meta, meta_time=meta_time)

@app.errorhandler(404)  
def not_found(e):
  log(request.environ)
  return render_template("404.html")

if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)
