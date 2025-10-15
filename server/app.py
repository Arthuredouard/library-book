from server import create_app

# Crée l'application Flask
app = create_app()

if __name__ == "__main__":
    # Lance l'application sur le port 5555
    app.run(host="0.0.0.0", port=5555, debug=True)


