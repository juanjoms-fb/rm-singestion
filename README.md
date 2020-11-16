# Rights Manager Scaled Ingestion

This scripts allows partners to upload semi-automatically a big number of videos.

## Prerequisites

- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)

- Pip: [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

- Make sure you can install packages using pip:  [https://packaging.python.org/tutorials/installing-packages/]()

## Instructions

1. Make sure you have all the prerequisites installed and configured

2. Download and unzip the [script file](script.zip) containing the script and the configuration file

3. Open a terminal/console and use the command `cd path/to/files` to navigate to the directory where you have placed the script and the other files.

4. Run the following command to install the requirements for the script: `pip install -r requirements.txt`

5. Verify your default configuration in the [defaults.yaml](defaults.yaml) file.

6. Run the script from the terminal using the command `python3 batcher.py`.

7. When propmpt in the terminal, introduce the full path of the directory containing your videos.


## Default configurations

You can review and update your default configuration for the videos in the [defaults.yaml](defaults.yaml) file. This file must contain the following fields with the corresponding values

```YAML
territories: [ISOCountryCode1, ISOCountryCode2, ...]
description: General description for all the videos in the package
category: EPISODE | MOVIE | WEB
monitoring_type: VIDEO_AND_AUDIO | VIDEO_ONLY | AUDIO_ONLY
match_rule_id: id of existing match rule
reference_disabled: TRUE | FALSE
whitelisted_fb_ids: [FB_USER_ID_1, FB_USER_ID_2, ...]
whitelisted_ig_ids: [IG_USER_ID_1, IG_USER_ID_2, ...]
tags: [tag1, tag2, ...]
action: CREATE | UPDATE | DELETE
```
