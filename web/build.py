import os
import pathlib

# Delete the "../deploy" directory if it exists

d = pathlib.Path(__file__).parent.resolve()
deploy_dir = f'{d}/deploy'
if os.path.exists(deploy_dir):
    os.rmdir(deploy_dir)

os.mkdir(deploy_dir)
