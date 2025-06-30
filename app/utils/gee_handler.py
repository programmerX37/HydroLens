"""Google Earth Engine helper utilities."""

import os
import ee

# Authenticate using service account credentials provided via environment
# variables and initialize the Earth Engine API.
service_account = os.getenv("GEE_SERVICE_ACCOUNT")
key_path = os.getenv("GEE_PRIVATE_KEY_PATH")

if service_account and key_path:
    credentials = ee.ServiceAccountCredentials(service_account, key_path)
    ee.Initialize(credentials)
else:
    # Fall back to default authentication if variables aren't set
    ee.Initialize()

# Additional helper functions will be added here in the future.
