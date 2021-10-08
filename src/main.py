from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {
        'result': 'This is a FastAPI server'
    }
