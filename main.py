from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files (CSS, JS, images, etc.) from the "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    """Landing page — serves index.html"""
    return FileResponse("templates/index.html")


@app.get("/level")
async def level():
    """Level page — serves level.html"""
    return FileResponse("templates/level.html")

@app.get("/tree")
async def tree():
    """Tree level page — serves tree.html"""
    return FileResponse("templates/tree.html")

@app.get("/linked")
async def linked():
    return FileResponse("templates/linked.html")

@app.get("/arrays")
async def arrays():
    return FileResponse("templates/arrays.html")

@app.get("/stacks")
async def stacks():
    return FileResponse("templates/stacks.html")

@app.get("/queue")
async def queue():
    return FileResponse("templates/queue.html")

@app.get("/heaps")
async def heaps():
    return FileResponse("templates/heaps.html")

@app.get("/hashmaps")
async def hashmaps():
    return FileResponse("templates/hashmaps.html")

@app.get("/graphs")
async def graphs():
    return FileResponse("templates/graphs.html")

@app.get("/go-to-level")
async def go_to_level():
    """Redirect endpoint triggered by the Enter button"""
    return RedirectResponse(url="/level")
