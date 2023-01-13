from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encrypt_text():
    if request.method == 'POST':
        text = request.form['text']
        shift = 3
        key = 'secretkey'
        encrypted_text = ""
        
        # Caesat Cipher encryption
        for char in text:
            if char.isalpha():
                char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_text += char

        # Vigenere Cipher encryption
        for i in range(len(encrypted_text)):
            if encrypted_text[i].isalpha():
                char = chr((ord(encrypted_text[i]) + ord(key[i % len(key)]) - 194) % 26 + 97)
                encrypted_text = encrypted_text[:i] + char + encrypted_text[i+1:]

        # ROT13 encryption
        encrypted_text = encrypted_text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))

        return render_template('index.html', text=text, encrypted_text=encrypted_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
