from app import create_app

app = create_app()

# change value to prod if ready to deploy


if __name__ == "__main__":
    app.run()


