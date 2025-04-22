from fastapi import FastAPI

app = FastAPI()
@app.get('/test')
def testMethod():
  return "sb"
