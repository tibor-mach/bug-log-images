from dvclive import Live
import dvc.api
import glob
import os

params = dvc.api.params_show()

with Live() as live:
    for pth in glob.glob("test_img/*.jpg"):
        live.log_image(params["name_prefix"]+os.path.basename(pth), pth)