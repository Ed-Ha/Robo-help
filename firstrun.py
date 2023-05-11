from routes import *
from flask import Flask, render_template, request, jsonify, redirect, url_for


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

