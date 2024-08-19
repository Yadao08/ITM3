from fastapi import FastAPI

app = FastAPI()

name_list = []

@app.get("/")
def root():
    return {"Names": name_list}

@app.get("/insert/{name}")
def insert_name(name: str):
    name_list.append(name)
    return {"message": f"{name} is now added!"}

@app.get("/remove/{name}")
def remove_name(name: str):
    if name in name_list:
        name_list.remove(name)
        return {"message": f"{name} is now removed!"}
    else:
        return {"message": f"{name} sorry not found!"}