from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # For local development only; Gunicorn handles this in production
