# crypto-web-classifier
This repository contains the code and resources for my undergraduate thesis project on Sentiment Analysis of Cryptocurrency News Headlines using Transfer Learning with Bidirectional Encoder Representations from Transformers (BERT). The model used in this project was fine-tuned with hyperparameters, including a learning rate of 2e-5 and a batch size of 8. To prevent overfitting and improve training efficiency, early stopping callbacks were implemented, monitoring the validation loss, with a patience of 100 epochs.
## Introduction
Cryptocurrency is a peer-to-peer digital exchange system based on blockchain technology and utilizes cryptography to generate and distribute units of cryptocurrency. As for its utility, cryptocurrency can be used as a payment tool in buying and selling transactions as well as investments. There is an interaction between media sentiment and the price of cryptocurrencies, accompanied by tendencies for investors to react. Sentiment analysis is a crucial task in understanding public opinion and market sentiment. With the rise of cryptocurrencies, analyzing sentiment in cryptocurrency news headlines has become increasingly important for traders, investors, and analysts. This project leverages the power of BERT, a state-of-the-art natural language processing model, to perform sentiment analysis on cryptocurrency news headlines.
## Project Structure
- static/
  - index.css
  - placeholder.js
  - result.css
- templates/
  - index.html
  - result.html
- README.md
- app.py
- config.json
- tf_model.h5
## Getting Started
1. Download tf_model.h5 from this link https://drive.google.com/file/d/1faW7hnXUjY8lYO8wYWNFJAzpXGhwBaqC/view?usp=sharing
2. Place the downloaded tf_model.h5 file into the project directory.
3. Open terminal and navigate to the project directory. Execute the following command: ```python app.py```
4. Navigate to the web page
## Usage
Enter the text you want to analyze for sentiment in the text box at the web page. The model will process your input text and display the sentiment analysis result as output text in the next page. The result will indicate whether the input text is classified as positive, negative, or neutral sentiment.
## Demo
https://www.youtube.com/watch?v=4a5HWFQpBYI
