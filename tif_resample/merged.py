import os
import rasterio

from rasterio.merge import merge
def merge_tif(input_folder, output_path):
    tif_files = [f for f in os.listdir(input_folder) if f.endswith('.tif') or f.endswith('.tiff')]
    src_files = [rasterio.open(os.path.join(input_folder, f)) for f in tif_files]
    merged, transform = merge(src_files)
    with rasterio.open(output_path, 'w', **src_files[0].meta) as output_file:
        output_file.write(merged)
    for src in src_files:
        src.close()
