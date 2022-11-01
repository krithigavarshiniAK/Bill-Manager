from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import frontend.build


def load_frontend(api_inst: FastAPI) -> None:
    frontend_path = frontend.build.__path__[0]
    # Mount the base web app - Must be the last operation
    api_inst.mount("", StaticFiles(directory=frontend_path, html=True), name="webapp")
