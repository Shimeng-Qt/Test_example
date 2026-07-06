# -*- coding: utf-8 -*-

import os
import os.path
import subprocess
import sys
import objectmaphelper

from remotesystem import RemoteSystem

def main():
    startApplication("addressbook")
    
    # get an object
    widget = waitForObject({"type": "MainWindow"})
    vp_name = "svp"
    create_screenshot_vp(widget, vp_name)
    test.vp(vp_name)
    
def create_screenshot_vp(widget, vp_name):
    obj_name = objectMap.symbolicName(widget)
    
    img = object.grabScreenshot(widget)

    img_filename = 'cssvp' + vp_name + '.png'
    img_filename2 = 'cssvp' + vp_name + '.2.png'
    
    try:
        os.remove(img_filename)
    except:
        pass
    try:
        os.remove(img_filename2)
    except:
        pass
    
    img.save(img_filename)
    
    #testData.get(img_filename)
    
    vp_dir = os.path.join(squishinfo.testCase,'verificationPoints')
    if not os.path.exists(vp_dir):
        os.makedirs(vp_dir)
        
    vp_filename = os.path.join(vp_dir,vp_name)
    
    # Create verification point file:
    subprocess.call(
            [
                os.path.join(os.environ['SQUISH_PREFIX'], 'bin', 'convertvp'),
                "--tovp",
                vp_filename,
                img_filename2,
                obj_name
            ]
        )
    
    