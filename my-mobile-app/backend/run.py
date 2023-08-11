from .app import create_app

# Create the Flask app instance
app = create_app()

# Run the development server
def run():
    app.run(debug=True)
