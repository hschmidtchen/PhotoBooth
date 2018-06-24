import picamera
from time import sleep
import subprocess
import signal

class Image:
    """ Image stuffs """

    @staticmethod
    def snap(session_id,photo_id):
        """
        Snap an image and saves it to filename
        """
        with picamera.PiCamera() as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview(fullscreen=False, window=(0, 0, 800, 480), crop=(0, 195, 2592, 1556))
            for i in range(5):
                im_path="/home/pi/photobooth/photobooth/static/icons/%d.png" % (5-i)
                cmd=["/home/pi/raspidmx/pngview/pngview", "-b", "0", "-l", "3", im_path]
                subprocess.Popen(cmd)
                sleep(1)
                cmd = ["killall", "pngview"]
                subprocess.call(cmd)

            picam_path='static/photos/full/image_%s_%s.jpg' % (session_id,photo_id)
            camera.capture(picam_path)
            camera.stop_preview()

        return picam_path

    @staticmethod
    def snap_dlr(session_id, photo_id):
        """
        Snap an image and saves it to filename
        """
        dlr_path = "/home/pi/photobooth/photobooth/static/photos/full/image_%s_%s.jpg" % (session_id, photo_id)
        
        #start preview
        cmd = ["/home/pi/photobooth/photobooth/preview.sh",dlr_path]
        prev_prc = subprocess.Popen(cmd)
        
        sleep(3)

        #countdown
        for i in range(5):
            im_path = "/home/pi/photobooth/photobooth/static/icons/%d.png" % (5 - i)
            cmd = ["/home/pi/raspidmx/pngview/pngview", "-b", "0", "-l", "3", im_path]
            subprocess.Popen(cmd)
            sleep(1)
            cmd = ["killall", "pngview"]
            subprocess.call(cmd)

        prev_prc.wait()
        
        #imagemagic to cut the image
        dlr_path2 = "/home/pi/photobooth/photobooth/static/photos/print/image_%s_%s.jpg" % (session_id, photo_id)
        cmd = ["convert", dlr_path, "-crop", "3888x2430+0+160", dlr_path2 ]
        print(cmd)
        subprocess.call(cmd)

        return dlr_path
