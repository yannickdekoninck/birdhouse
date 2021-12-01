from flask import Flask, render_template, Response
import birdhouse.birdcam

app = Flask(__name__)
camera = birdhouse.birdcam.BirdCam()
camera.setup()


@app.route("/")
def index():
    return render_template("index.html")


def gen():
    while True:
        frame = camera.save_frame_to_stream()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame.getvalue() + b"\r\n\r\n"
        )


@app.route("/video_feed")
def video_feed():
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
