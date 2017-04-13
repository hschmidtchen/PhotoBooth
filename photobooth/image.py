import picamera
from time import sleep

class Image:
    """ Image stuffs """

    @staticmethod
    def snap(filename):
        """
        Snap an image and saves it to /static/images/image-**timestamp**.jpg
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview()
            sleep(5)
            camera.capture(filename)
            camera.stop_preview()

        return filename