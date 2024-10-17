from app import create_app
from waitress import serve

app = create_app()

# change value to prod if ready to deploy
mode = "prod"

if __name__ == "__main__":
    # run dev mode if mode == dev, 
    # else run production mode with waitress ASGI (Asynchronous Server Gateway Interface) server
    if mode == "dev":
        app.run(debug=True)
    else:
        try:
            # Start the Waitress server
            print("Server started successfully! Listening on localhost:50100")
            serve(app, host='0.0.0.0', port="50100", threads=4)
            print("Server terminated")
        except Exception as e:
            # Print an error message if the server fails to start
            print(f"Failed to start the server: {e}")


