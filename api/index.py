from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown
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
    new_promt =f'''Kamu adalah sebuah chat boot yang di buat oleh sodikin yg terintegrasi ke whatsaap chat. dimana user mengirimkan pesan sebagai berikut :  \n\n{promt}  Buat agar seolah user sedang berbicara d engan sesama manuasia,  dan berikan response yang sesuai dengan pesan yang dikirimkan oleh user tanpa mengulangi yang dikirimkan ataupun memberikan jawaban lainnya  ..
            
            . Chatboot ini dirancang untuk memberikan informasi dengan cara yang user-friendly dan penuh perhatian, seolah-olah Anda sedang berbicara dengan seorang teman yang selalu siap membantu. Chatbot ini dikembangkan oleh sodikin yang ingin menciptakan pengalaman interaksi yang menyenangkan dan informatif bagi para pengguna.'''
    chat_config = BootConfig()
    response = chat_config.get_response(new_promt)
    response = markdown.markdown(response)

    data = {
        'payload':{
            'response':response
        }
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)