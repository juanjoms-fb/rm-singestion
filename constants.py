import csv

VALID_VIDEO_FORMATS = [
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


CSV_FIELDNAMES = [
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

VALID_ACTIONS = [
    'CREATE',
    'UPDATE',
    'DELETE',
]

VALID_MONITORING_TYPES = [
    'VIDEO_AND_AUDIO',
    'VIDEO',
    'AUDIO',
]

VALID_CATEGORIES = [
    'EPISODE', 
    'MOVIE', 
    'WEB'
]

def load_iso_codes():
    codes = {}
    with open('Territories ISO Alpha 2.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            k = rows[0]
            v = rows[1]
            codes[k] = v
    return codes


ISO_ALPHA_2_CODES = load_iso_codes()


load_iso_codes()