import pkgutil
import importlib
from fastapi import FastAPI

app = FastAPI()

def include_all_routers(app: FastAPI, package_name: str):
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router)

include_all_routers(app, "app.routes.api")
