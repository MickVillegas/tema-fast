from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def hola():
    return {"Salida":"¡Hola!"}

from starlette import status
@app.get('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=None)
def hola2(id:int,parametro:str='hola_por_defecto') -> dict[str,any]:
    return {'path':id, 'parameter': parametro}

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app = 'main:app', host='0.0.0.0', port=8000, reload=True)