from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    projects = [
        {
            "title": "Vance Finance",
            "description": "A cool project using Python and Flask.",
            "link": "https://github.com/caavme/Vance-Finance",
            "images": [
                "/static/projects/vancefinance1.png",
                "/static/projects/vancefinance2.png",
                "/static/projects/vancefinance3.png",
                "/static/projects/vancefinance4.png"
            ]
        },
        {
            "title": "Ellinox AI Guide",
            "description": "Another awesome project.",
            "link": "https://github.com/caavme/Ellinox-AI-Guide",
            "images": [
                "/static/projects/ellinoxaiguide1.png",
                "/static/projects/ellinoxaiguide2.png"
            ]
        },
        {
            "title": "Ellinox Bluesky Bot",
            "description": "Another awesome project.",
            "link": "https://github.com/yourusername/project-two",
            "images": [
                "/static/projects/project2-1.jpg",
                "/static/projects/project2-2.jpg"
            ]
        },
        {
            "title": "TPI Dispatch",
            "description": "Another awesome project.",
            "link": "https://github.com/caavme/techpulse-dispatch",
            "images": [
                "/static/projects/project2-1.jpg",
                "/static/projects/project2-2.jpg"
            ]
        }
    ]
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)