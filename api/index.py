from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

class BootConfig():
    def __init__(self):
        self._tokoen = 'AIzaSyB9b3WkouyhF_kyhXBZwP3yZPN-M0ilzBI'
        self._model = genai.GenerativeModel('gemini-1.5-flash')
    
    def get_response(self, promt):
        genai.configure(api_key=self._tokoen)
        response = self._model.generate_content(promt)
        response = response.text
        return response

# chat_config = BootConfig()
# response = chat_config.get_response('hallo kamu siapa?')
# print(f'jawaban   {response}')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    promt = request.args.get('promt')
    new_promt = f'''
    ini adalah sebuah chat yang dikirimakn oleh user : {promt} 

    dimana kamu adalah sebuah chatboot yang dikembangkan oleh orang yang beranma : sodikin.
    
    noted : 
    *  Jawab seolah kamu sedang berbicara dengan sesama manusia 
    '''
    chat_config = BootConfig()
    response = chat_config.get_response(new_promt)
    data = {
        'payload':{
            'response':response
        }
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)