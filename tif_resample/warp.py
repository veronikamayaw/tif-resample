from osgeo import gdal


def warp_vrt(vrt_path, output_path, resolution=None):

    if resolution is None:

        gdal.Warp(output_path,
                  vrt_path)

    else:

        gdal.Warp(output_path,
                  vrt_path,
                  xRes=resolution,
                  yRes=resolution)

    return output_path