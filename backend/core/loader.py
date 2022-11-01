from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

def load_frontend(api_inst: FastAPI) -> None:
    try:
        import frontend.build

        frontend_path = frontend.build.__path__[0]
        # Mount the base web app - Must be the last operation
        api_inst.mount("", StaticFiles(directory=frontend_path, html=True), name="webapp")
    except ImportError:
        print("Unable to find the application root resources - dependency tpds-application-root is missing")