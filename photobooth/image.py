import picamera
from time import sleep
import subprocess

class Image:
    """ Image stuffs """

    @staticmethod
    def snap(filename):
        """
        Snap an image and saves it to filename
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview(fullscreen=False, window=(0,0,800,480), crop=(0,195,2592,1556))
            sleep(5)
            camera.capture(filename)
            cmd = "gphoto2 --capture-image-and-download --filename /home/pi/photobooth/photobooth/static/photos/full/dlr_image2.jpg"
            print(cmd)
            subprocess.call(cmd)
            camera.stop_preview()

        return filename