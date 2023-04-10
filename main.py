from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ParserEngine import MCQsParser

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
<html>
<head>
    <title>QuizREST API</title>
    <style>
        h1 {
            color: rebeccapurple;
        }

        h1,
        p {
            text-align: center;
        }
        .container {
            width: 100%;
            height: 100vh;
            position: fixed;
            top: 0;
            z-index: 9999;
            background: var(--black-body);
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>

<body>
    <div class="container">
        <div>
            <h1>Welcome to Quiz REST API!</h1>
            <p>Enter the number of MCQS in the URL you want to fetch</p>
            <p>Example: <a href="http://127.0.0.1:8000/20">http://127.0.0.1:8000/20</a> </p>
        </div>
    </div>
</body>
</html>
    """

@app.get("/{number}",response_class=HTMLResponse)
def read_root(number: int):
    if number>20 :
        print("Not enough Questions")
        return """
    <html>
    <head>
        <title>QuizREST API</title>
        <style>
            h1 {
                color: rebeccapurple;
            }

            h1,
            p {
                text-align: center;
            }
            .container {
                width: 100%;
                height: 100vh;
                position: fixed;
                top: 0;
                z-index: 9999;
                background: var(--black-body);
                display: flex;
                justify-content: center;
                align-items: center;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div>
                <h1>Not enough Questions</h1>
                <p>Try a number between 1 and 20</p>
                <p>Return to homapage : <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> </p>
            </div>
        </div>
    </body>
    </html>
        """
    if number<0 :
        print("Number cannot be less than zero")
        return """
    <html>
    <head>
        <title>QuizREST API</title>
        <style>
            h1 {
                color: rebeccapurple;
            }

            h1,
            p {
                text-align: center;
            }
            .container {
                width: 100%;
                height: 100vh;
                position: fixed;
                top: 0;
                z-index: 9999;
                background: var(--black-body);
                display: flex;
                justify-content: center;
                align-items: center;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div>
                <h1>Number cannot be less than zero</h1>
                <p>Try a number between 1 and 20</p>
                <p>Return to homapage : <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> </p>
            </div>
        </div>
    </body>
    </html>
        """
    parser = MCQsParser("input_file.txt", number)
    response = parser.get_response()
    return f"""
    <html>
    <head>
        <title>QuizREST API</title>
        <style>
            h1 {{
                color: rebeccapurple;
                text-align: center;
            }}
            p{{
                margin-top:2rem;
            }}
            .container {{
                margin-left:1rem;
                margin-right:1rem;
            }}
        </style>
    </head>

    <body>
    <div class="container">
    <h1>Response Recieved</h1>
    {response}
    <p>Return to homapage : <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> </p>
    <div/>
    </body>
    </html>
    """



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
