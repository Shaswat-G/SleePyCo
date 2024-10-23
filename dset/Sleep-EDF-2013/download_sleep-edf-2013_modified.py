import os
import requests

# Ensure the destination directory exists
os.makedirs('./edf', exist_ok=True)

# List of URLs to download
urls = [
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4001E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4001EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4002E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4002EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4011E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4011EH-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4012E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4012EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4021E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4021EH-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4022E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4022EJ-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4031E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4031EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4032E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4032EP-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4041E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4041EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4042E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4042EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4051E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4051EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4052E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4052EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4061E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4061EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4062E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4062EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4071E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4071EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4072E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4072EH-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4081E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4081EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4082E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4082EP-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4091E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4091EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4092E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4092EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4101E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4101EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4102E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4102EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4111E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4111EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4112E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4112EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4121E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4121EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4122E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4122EV-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4131E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4131EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4141E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4141EU-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4142E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4142EU-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4151E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4151EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4152E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4152EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4161E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4161EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4162E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4162EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4171E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4171EU-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4172E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4172EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4181E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4181EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4182E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4182EC-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4191E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4191EP-Hypnogram.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4192E0-PSG.edf',
    'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4192EV-Hypnogram.edf'
]

# Function to download files using requests
def download_file(url, destination_folder):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(destination_folder, local_filename)

    # Make the request to download the file
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()  # Check for HTTP errors
            # Write the content to a local file in chunks
            with open(local_filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive chunks
                        f.write(chunk)
        print(f"Downloaded {local_filename} to {destination_folder}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh} - {url}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc} - {url}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt} - {url}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err} - {url}")

# Download each file
i = 0
for url in urls:
    i = i+1
    print(f"{i} of {len(urls)}")
    download_file(url, './edf')