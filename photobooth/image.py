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
            camera.annotate_text_size = 160
            camera.start_preview(fullscreen=False, window=(0, 0, 800, 480), crop=(0, 195, 2592, 1556))
            for i in range(5):
                camera.annotate_text = "%d" % int(5-i)
                sleep(1)
            picam_path='static/photos/full/image_%s_%s.jpg' % (session_id,photo_id)
            camera.capture(picam_path)
            camera.stop_preview()

        return picam_path

    @staticmethod
    def snap_dlr(session_id, photo_id):
        """
        Snap an image and saves it to filename
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.annotate_text_size = 160
            camera.start_preview(fullscreen=False, window=(0, 0, 800, 480), crop=(180, 325, 2232, 1396))
            for i in range(5):
                camera.annotate_text = "%d" % int(5 - i)
                sleep(1)
            dlr_path = "/home/pi/photobooth/photobooth/static/photos/full/image_%s_%s.jpg" % (session_id, photo_id)
            dlr_path2 = "/home/pi/photobooth/photobooth/static/photos/print/image_%s_%s.jpg" % (session_id, photo_id)
            cmd = ["gphoto2", "--capture-image-and-download", "--filename", dlr_path]
            subprocess.call(cmd)
            camera.stop_preview()

            #imagemagic to cut the image
            cmd = ["convert", dlr_path, "-crop", "3888x2430+0+160", dlr_path2 ]
            print(cmd)
            subprocess.call(cmd)

        return dlr_path