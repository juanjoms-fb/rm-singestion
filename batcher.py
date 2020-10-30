import os
import csv
import yaml
from pathlib import Path
import time



csv_fieldnames = [
    'Filename',
    'Territories',
    'Title',
    'Description',
    'Category',
    'Monitoring Type',
    'Match Rule ID',
    'Reference Disabled',
    'Whitelisted FB IDs',
    'Whitelisted IG IDs',
    'Tags',
    'Action',
]

valid_video_formats = [
    ".3g2", ".3gp", ".3gpp",
    ".asf", ".avi",
    ".dat", ".divx", ".dv",
    ".f4v", ".flv",
    ".gif",
    ".m2ts", ".m4v", ".mkv", ".mod",
    ".mov", ".mp4", ".mpe", ".mpeg",
    ".mpeg4", ".mpg", ".mts",
    ".nsv",
    ".ogm", ".ogv",
    ".qt",
    ".tod", ".ts",
    ".vob",
    ".wmv",
]

valid_actions = [
    'CREATE',
    'UPDATE',
    'DELETE',
]

valid_monitoring_types = [
    'VIDEO_AND_AUDIO',
    'VIDEO',
    'AUDIO',
]

valid_categories = [
    'WEB',
]

def is_video_file(file_name):
    f = os.path.splitext(file_name)
    return f[-1] in valid_video_formats


def get_video_title(filename):
    f = os.path.splitext(filename)
    name = f[-2].replace("_", " ")
    return name

def convert_list_to_string(elements_list):
    list_string = ""
    for element in elements_list:
        list_string += element+","
    return list_string[:-1]


def get_default_config():
    config = open("./defaults.yaml")
    params = yaml.load(config, Loader=yaml.FullLoader)
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

    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames, delimiter=',')
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
    renamed_videos_directory = rename_directory(videos_directory)
    generate_csv(renamed_videos_directory)

main()
