import signal
from typing import Any
from .api import ApiServer 

class Backend:
    """
    Manage backend services
    """
    __shared_state: dict[str, Any] = {}

    def __init__(self) -> None:
        if not self.__shared_state:
            self._api_server = None

    def start(self) -> None:
        # Start new API Server and usecase collector
        self._api_server = ApiServer(ports=range(5000, 5015))
        self._api_server.start()
        self._api_server.join()

    def stop(self) -> None:
        if self._api_server:
            self._api_server.stop()

    def run(self) -> None:
        """
        Run until an exit signal is encountered
        """
        self.start()
        signal.sigwait([signal.SIGINT])
        self.stop()

    def is_ready(self) -> bool:
        return self._api_server and self._api_server.up()

    def api_port(self) -> int:
        return self._api_server.port

def launch_app():
    """
    Launch all backend services used by Application
    """
    backend = Backend()
    backend.start()

    def handler(sig_id, frame):
        print("closing backend")
        backend.stop()

    # Allow SIGINT to stop the application
    signal.signal(signal.SIGINT, handler)