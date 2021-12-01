import pytest
import birdhouse.birdcam as birdcam


@pytest.fixture(scope="module")
def running_camera():
    cam = birdcam.BirdCam()
    cam.setup()
    yield cam
    cam.close()


def test_capture_jpeg(running_camera, tmp_path):
    target_image = tmp_path / "test.jpg"
    running_camera.save_frame_to_file(str(target_image))
    assert target_image.exists()


def test_capture_png(running_camera, tmp_path):
    target_image = tmp_path / "test.png"
    running_camera.save_frame_to_file(str(target_image))
    assert target_image.exists()


def test_resolution(running_camera):
    assert running_camera.camera_resolution == (720, 480)


def test_framerate(running_camera):
    assert int(running_camera.camera_framerate) == 30


def test_iso(running_camera):
    assert running_camera.camera_iso == 0


def test_exposure_mode(running_camera):
    assert running_camera.camera_exposure_mode == "auto"
