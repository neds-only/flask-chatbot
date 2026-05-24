#the name of the file is web1.py
import requests
#requests--from Flask to the api
#request--from the browser or from the form to flask
from flask import Flask,request,render_template
#imported the tool from the toolbox so that i dont need to use flask.Flask in every line
web=Flask(__name__)
#flask needs to know where the files are located in system
#flask takes the help of __name__ to find .py file and then checks near tht location to find template folder and statics folder
#giving Flask your ID, and Flask uses that ID to look up your home address
@web.route('/',methods=['GET','POST'])
def home():
#“Globals persist, locals reset”
    a=None
    if request.method=='POST':#request.method is a way for flask to understand what http request did the browser make to get a page or send info
       a=request.form['user_input']#request.form is a dictionary---the envelop is the dictionary where the variable is the keys and the value entered by user is its values
       apikey='fa4fa100a3d6a428492ea4c7b0c84c49'
       url=f'https://api.themoviedb.org/3/search/movie?query={a}&api_key={apikey}'
       response=requests.get(url)
       print(response.json())
    return render_template('index.html',user_input=a)
#flask runs the user defined fnc(on request of the browser) which has rendertemplate to fill in the placeholder and makes it the final html string and return gives the final html to flask which it automatically makes it an http response and sends to the browser(also automatically)?
#note:when i say tht return gives the html string to flask i mean it passes that back to flask,i mean flask assigns the task and the user definition converts it to a value passes it back to flask and that value is converted into an http response which is sent to the browser
#Just remember: return is not “sending to Flask”, it is “output of function”
#my routes name is /
if __name__=='__main__':
    web.run(debug=True)
#__name__ == "__main__" → “I am running directly”
#__name__ == "filename" → “I was imported”
