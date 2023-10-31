from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import elevation

# Connect to the Copernicus Open Access Hub
api = SentinelAPI('dpuhar', 'Satie279', 'https://apihub.copernicus.eu/apihub')

# Search for Sentinel-2 products
footprint = geojson_to_wkt(read_geojson('/home/dule/Desktop/NSKvart.geojson'))
products = api.query(footprint,
                     date=('20230925', '20231025'),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 10))

# Download Sentinel-2 data
api.download_all(products)

# Download a 10m resolution DEM
elevation.clip(bounds=(19.7335, 45.1671, 20.0335, 45.3671), output='/home/dule/Desktop/Za_IVI.tif', product='SRTM')
