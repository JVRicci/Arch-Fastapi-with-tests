import uvicorn


def main():
    print("Hello from fastapi-arch-project!")


if __name__ == "__main__":
    main()
    uvicorn.run("src.server.server:app", host="0.0.0.0", port=8000, reload=True)
