from flask import Flask, render_template, url_for, request, redirect
import text2emotion as te

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])## get is to get data from user into the database
def hello_world():
    if request.method == 'POST':
        text = request.form['content']
        emotion = te.get_emotion(text)
        emotion_list = []
        for key, value in emotion.items():
            emotion_list.append(float(value))
        
        print(emotion_list)
        
        return render_template('index.html', results=emotion_list)
        
    else:
        return render_template('index.html', results=[])


if __name__ == '__main__':
    app.run(debug=True)
