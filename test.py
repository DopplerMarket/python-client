import os
os.environ["DOPPLER_API_KEY"] = "vSNdjLhatIkD8w6F1W0IEDvKfflbTUkRh8AvghaA"
os.environ["DOPPLER_PIPELINE"] = "31"
os.environ["DOPPLER_ENVIRONMENT"] = "development_python"


from doppler_client import Doppler
Doppler()

print(os.getenv("TESTER"))