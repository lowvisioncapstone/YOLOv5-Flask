import roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="gFsD10VHDpjbPKdbU38R")
project = rf.workspace("yolo-hdurx").project("kitchen-i2lva")
version = project.version(2)
dataset = version.download("yolov5")
                