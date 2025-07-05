import ee

# Your Google Earth Engine Project ID
PROJECT_ID = 'articulate-ion-460609-f6'

print("Attempting Earth Engine authentication...")
# Keep this commented out unless you need to re-authenticate via browser.
# ee.Authenticate()

print(f"Attempting to initialize Earth Engine with project: {PROJECT_ID}...")
try:
    ee.Initialize(project=PROJECT_ID)
    print("Earth Engine initialized successfully!")
    print("✅ Auth OK")
except ee.ee_exception.EEException as e:
    print(f"❌ Error initializing Earth Engine: {e}")
    print("Please ensure your Project ID is correct and the Earth Engine API is enabled for it.")
    print("Visit https://console.cloud.google.com/apis/library/earthengine.googleapis.com to enable the API.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")