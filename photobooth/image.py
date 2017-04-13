import picamera
from time import sleep

class Image:
    """ Image stuffs """

    @staticmethod
    def snap(filename):
        """
        Snap an image and saves it to filename
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview(fullscreen=False, window=(0,0,800,480))
            sleep(5)
            camera.capture(filename)
            camera.stop_preview()

        return filename