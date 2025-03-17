from PySide6.QtWidgets import QApplication
import sys
from pathlib import Path
from caliscope.controller import Controller
from caliscope.gui.vizualize.calibration.capture_volume_widget import CaptureVolumeWidget

app = QApplication(sys.argv)
workspace_dir = Path(r"C:\Users\Mac Prible\repos\caliscope\dev\key_error_11")
                     

controller = Controller(workspace_dir)
controller.load_camera_array()
controller.load_estimated_capture_volume()
window = CaptureVolumeWidget(controller)


window.show()

app.exec()
