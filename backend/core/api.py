import time
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from .router import api_router
from .loader import load_frontend


def _initializeApiInstance(port) -> FastAPI: 
    # Global fastapi instance that will host frontends and apis
    api_inst = FastAPI(
        title="Bill Manager Api",
        description="",
        version=1.0,
        servers=[{"url": f"http://localhost:{port}", "description": "Default"}],
    )
    api_inst.include_router(api_router)

    # Setup CORS for local access from other servers we'll be running
    origins = [
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
        f"http://127.0.0.1:{port}",
        "http://localhost",
        "http://localhost:3000",
        f"http://localhost:{port}",
    ]
    api_inst.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Attach the Frontend application
    load_frontend(api_inst)

    return api_inst

class ApiServer:
    def __init__(self, host_ip="127.0.0.1", ports=[5001], port=None) -> None:
        """
        Init function to get Uvicorn server parameters
        """
        self._thread = None
        self._server = None
        self._result = 0
        self._host_ip = host_ip
        self._ports = [port] if port else ports
        self._port = 0

    @property
    def host_ip(self):
        return self._host_ip

    @property
    def port(self):
        return self._ports[self._port]

    def _config_server(self):
        if self._port < len(self._ports):
            api_inst = _initializeApiInstance(self.port)
            config = Config(api_inst, host=self.host_ip, port=self.port, log_level="info")
            self._server = Server(config=config)
        else:
            raise ValueError(f"Unable to find an open port in {self._ports}")

    def _can_start_server(self):
        if self._server is None:
            return True
        else:
            return not self._server.started

    def _run_api(self) -> None:
        self._server.run()

    def _wait_for_server_to_start(self) -> bool:
        while self._thread.is_alive():
            if self._server and self._server.started:
                return True
            time.sleep(1)
        return False

    def start(self) -> None:
        """
        Start Uvicorn server
        """
        while self._can_start_server():
            self._config_server()
            self._thread = threading.Thread(target=self._run_api)
            self._thread.daemon = True
            self._thread.start()
            if self._wait_for_server_to_start():
                return
            else:
                self._port += 1

    def up(self) -> bool:
        return self._server.started if self._server else False

    def stop(self) -> int:
        """
        Stop Uvicorn server
        """
        self._result = 0
        if self._server and self._thread.is_alive():
            # Try gracefull first
            self._server.should_exit = True
            self._thread.join(timeout=10)
            # Try to force exit
            if self._thread.is_alive():
                self._server.force_exit = True
                self._thread.join(timeout=10)
            # Note that the force exit failed as well
            if self._thread.is_alive():
                self._result = -1

        return self._result

    def join(self) -> None:
        """
        Join Uvicorn server process

        Join used to give chance for the background tasks to update the status
        of the object to reflect the termination of the process
        """
        if self._thread and self._thread.is_alive():
            try:
                self._thread.join()
                return self._result
            except:
                return self.stop()

    def is_alive(self) -> bool:
        """
        Returns process status, True if it is alive and False if it is closed
        """
        self._thread.is_alive()

