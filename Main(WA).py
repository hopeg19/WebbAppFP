from flask import Flask, render_template
import Util(WA)

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
   # record = util.run_and_fetch_sql(cursor, "CREATE TABLE public."TestTable"
#(
#    "First Name" character varying(225),
#    "Last Name" character varying(225),
#   "Phone Number" character varying(225),
 #   "Email" character varying(225),
 #   "Preferred Contact" character varying(225),
 #   PRIMARY KEY ("Last Name")
#);

#ALTER TABLE IF EXISTS public."TestTable"
 #   OWNER to raywu1990;")
  #  return render_template('index.html', log_html = log)

@app.route()

#INSERT INTO TestTable
#VALUES (value1, value2, value3, ...);


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
