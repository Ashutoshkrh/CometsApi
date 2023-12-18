import pyrebase

#  For Firebase JS SDK v7.20.0 and later, measurementId is optional
config = {
  "apiKey": "AIzaSyDhVvMAYKrj2wrdHfpJtlT4yo51uWQVv-s",
  "authDomain": "comets-8fbbe.firebaseapp.com",
  "projectId": "comets-8fbbe",
  "storageBucket": "comets-8fbbe.appspot.com",
  "messagingSenderId": "335154408572",
  "appId": "1:335154408572:web:0c2910aa511a92adf9adf9",
  "measurementId": "G-C0JYLDZWQ6",
  "databaseURL" : "https://comets-8fbbe-default-rtdb.firebaseio.com"  
}

def initialize():
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()
  return db

