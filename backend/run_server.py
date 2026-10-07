import sys
import uvicorn

# Fix for Windows asyncio ProactorEventLoop connection reset bug (WinError 10054)
if sys.platform == "win32":
    try:
        from asyncio.proactor_events import _ProactorBasePipeTransport
        _orig_call_connection_lost = _ProactorBasePipeTransport._call_connection_lost

        def _safe_call_connection_lost(self, exc=None):
            try:
                _orig_call_connection_lost(self, exc)
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                pass

        _ProactorBasePipeTransport._call_connection_lost = _safe_call_connection_lost
    except Exception:
        pass

if __name__ == "__main__":
    try:
        uvicorn.run("app.main:app", host="127.0.0.1", port=8001, log_level="info", access_log=True)
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
