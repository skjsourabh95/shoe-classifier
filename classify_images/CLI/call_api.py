import json
import requests
import click
import os
import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_tags(image_paths):
    '''Does a POST request to API with a list of image_path or URLs'''
        try:
            base_url = 'http://localhost:8050/'
            response = requests.post(base_url, json={'image_paths': image_paths},verify=False)
            return json.loads(response.text)
        except Exception as e:
            return str(e)

@click.command()
@click.option('--filepath', default=None, help="Text File Path Containing images")
def cli(filepath):
    '''
        Input : Takes a txt file containing imagepaths or URLs in each line
        Output :  return a list of predicted lables
    '''
    if filepath:
        image_paths = open(filepath).readlines()
        image_paths = [image_path.strip('\n') for image_path in image_paths]
        results = get_tags(image_paths)
        pp.pprint(results)
    else:
        pp.pprint('Provide File Path')

if __name__ == '__main__':
    cli()

