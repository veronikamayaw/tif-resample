from tif_resample import build_vrt, warp_vrt
import os


def test_workflow():

    input_folder = "tests/test_data"

    vrt_path = "tests/test_output/test.vrt"

    output_path = "tests/test_output/test_output.tif"

    build_vrt(input_folder,
              vrt_path)

    assert os.path.exists(vrt_path), "VRT file was not created!"

    warp_vrt(vrt_path,
             output_path,
             resolution=10)

    assert os.path.exists(output_path), "Warped GeoTIFF was not created!"