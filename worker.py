import requests

def download_image(path, body):
	with open(path, 'wb') as handle:
		response = requests.get(body, stream=True)
		for block in response.iter_content(1024):
			handle.write(block)