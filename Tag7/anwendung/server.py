import flask
import service

adder = service.Adder()

@route("/load")
def load_data():
    adder.load()
    
