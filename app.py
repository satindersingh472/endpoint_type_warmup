from dbhelpers import conn_exe_close
from flask import Flask, request
import json

app = Flask(__name__)

def get_display_results(statement,params_list):
    results = conn_exe_close(statement,params_list)
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        return results_json

@app.get('/api/restaurant')
def all_restaurants():
    results_json = get_display_results('call all_restaurants()',[])
    return results_json

@app.post('/api/restaurant')
def add_new_restaurant():
    name = request.json.get('name')
    address = request.json.get('address')
    phone_number = request.json.get('phone_number')
    image_url = request.json.get('image_url')
    results_json = get_display_results('call add_new_restaurant(?,?,?,?)',[name,address,phone_number,image_url])
    return results_json
    
@app.delete('/api/restaurant')
def delete_restaurant():
    id = request.json.get('id')
    results_json = get_display_results('call delete_restaurant(?)',[id])
    if(results_json[0][0] == 1):
        return 'Deleted successfully'
    else:
        return "Not deleted"


app.run(debug=True)

