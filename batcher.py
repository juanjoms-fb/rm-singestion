import os
import csv
import yaml
from pathlib import Path
import time
import constants

def is_video_file(file_name):
    f = os.path.splitext(file_name)
    return f[-1] in constants.VALID_VIDEO_FORMATS


def get_video_title(filename):
    f = os.path.splitext(filename)
    name = f[-2].replace("_", " ")
    return name

def convert_list_to_string(elements_list):
    list_string = ""
    for element in elements_list:
        list_string += element+","
    return list_string[:-1]


def validate_default_params(params):
    print(params["territories"])
    for country in params["territories"]:
        if country not in constants.ISO_ALPHA_2_CODES.values():
            raise Exception("The country code {} is not valid, please make sure this is an ISO Alpha 2 code".format(country))


def get_default_config():
    config = open("./defaults.yaml")
    params = yaml.load(config, Loader=yaml.FullLoader)
    validate_default_params(params)
    params['territories'] = convert_list_to_string(params['territories'])
    params['whitelisted_fb_ids'] = convert_list_to_string(params['whitelisted_fb_ids'])
    params['whitelisted_ig_ids'] = convert_list_to_string(params['whitelisted_ig_ids'])
    params['tags'] = convert_list_to_string(params['tags'])
    return params

def rename_directory(directory):
    print(directory)
    dest = list(directory.parts)
    dest[-1] = str(int(time.time()) )
    directory = directory.rename(os.path.join(*dest))
    print(directory)
    return directory

def generate_csv(directory):

    print("Generating CSV file in ", directory)

    output_file_name = directory.joinpath('video_ingest.csv')
    csvfile = open(output_file_name, 'w+')

    writer = csv.DictWriter(csvfile, fieldnames=constants.CSV_FIELDNAMES, delimiter=',')
    writer.writeheader()

    default_params = get_default_config()

    for filename in os.listdir(directory):
        if is_video_file(filename):
            writer.writerow({
                'Filename': filename,
                'Territories': default_params['territories'],
                'Title': get_video_title(filename),
                'Description': default_params['description'],
                'Category': default_params['category'],
                'Monitoring Type': default_params['monitoring_type'],
                'Match Rule ID': default_params['match_rule_id'],
                'Reference Disabled': default_params['reference_disabled'],
                'Whitelisted FB IDs': default_params['whitelisted_fb_ids'],
                'Whitelisted IG IDs': default_params['whitelisted_ig_ids'],
                'Tags': default_params['tags'],
                'Action': default_params['action'],
            })

    csvfile.close()

    print("CSV file generated in ", output_file_name)


def main():
    videos_directory = Path(input("Please introduce the full path to the directory that contains your videos: "))
    while not videos_directory.exists():
        videos_directory = Path(input("Invalid path, please try again: "))
    generate_csv(videos_directory)
    rename_directory(videos_directory)

main()
