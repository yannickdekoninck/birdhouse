import io
import picamera
import time
import numpy as np


class BirdCam:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.running = False

    def setup(self):
        try:
            self.camera.start_preview()
        except:
            return False
        time.sleep(2.0)
        self.running = True
        return True

    def save_frame_to_file(self, filename):
        if self.running:
            print(filename)
            self.camera.capture(filename)

    @property
    def camera_resolution(self):
        return self.camera.resolution

    @property
    def camera_framerate(self):
        return self.camera.framerate

    @property
    def camera_iso(self):
        return self.camera.iso

    @property
    def camera_exposure_mode(self):
        return self.camera.exposure_mode

    def save_frame_to_numpy(self):
        (res_x, res_y) = self.get_resolution()
        target = np.empty((736, 480, 3), dtype=np.uint8)
        self.camera.capture(target, "rgb")
        return target

    def save_frame_to_stream(self):
        out = io.BytesIO()
        self.camera.capture(out, "jpeg")
        return out

    def close(self):
        self.camera.stop_preview()
        self.running = False
