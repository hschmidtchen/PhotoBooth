import picamera
from time import sleep
import subprocess

class Image:
    """ Image stuffs """

    @staticmethod
    def snap(session_id,photo_id):
        """
        Snap an image and saves it to filename
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.annotate_text_size = 40
            for i in range(5):
                camera.annotate_text = '%s', 5-i
                camera.start_preview(fullscreen=False, window=(0,0,800,480), crop=(0,195,2592,1556))
                sleep(1)
                camera.stop_preview()
            picam_path='static/photos/full/image_%s_%s.jpg' % (session_id,photo_id)
            camera.capture(picam_path)
            dlr_path="/home/pi/photobooth/photobooth/static/photos/full/dlr_image_%s_%s.jpg" % (session_id,photo_id)
            cmd = ["gphoto2", "--capture-image-and-download", "--filename", dlr_path]
            subprocess.call(cmd)

        return picam_path