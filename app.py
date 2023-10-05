from flask import Flask, request, render_template
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

app = Flask(__name__)

model = TFBertForSequenceClassification.from_pretrained('E:/dev/crypto-bert-web')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

class_labels = ["Negative", "Neutral", "Positive"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']

        inputs = tokenizer(input_text, padding=True, truncation=True, return_tensors='tf', max_length=512)

        outputs = model(inputs)
        logits = outputs.logits
        probabilities = tf.nn.softmax(logits, axis=-1).numpy()[0]
        predicted_class = tf.argmax(probabilities).numpy()
        confidence = probabilities[predicted_class]

        negative, neutral, positive = probabilities

        confidence = round(confidence*100)
        negative = round(negative*100)
        neutral = round(neutral*100)
        positive = round(positive*100)

        return render_template('result.html', input_text=input_text, 
                       negative=negative, neutral=neutral, positive=positive,
                       predicted_class=class_labels[predicted_class], confidence=confidence)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
