from osgeo import gdal
import os

def build_vrt(input_folder, vrt_path):

    tif_files = []

    for f in os.listdir(input_folder):

        if f.endswith(".tif") or f.endswith(".tiff"):

            full_path = os.path.join(input_folder, f)

            tif_files.append(full_path)

    gdal.BuildVRT(vrt_path, tif_files)

    return vrt_path