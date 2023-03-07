from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", 'POST'])#decorator
def index():
  output = None
  gender = None
  color = None
  hobbies = None
  feedback = None
  if request.method == 'POST':
    name = request.form['name']
    gender = request.form['gender']
    color = request.form['color']
    hobbies = request.form.getlist('hobbies')
    feedback = request.form['feedback']
    
    output = f'Hello,{name}!'
    with open('else.txt','w') as file:
      file.write(name+'\n')
      file.write('98765'+ '\n')
    
  return render_template('index.html', output=output)



app.run(host='0.0.0.0', port=81)
