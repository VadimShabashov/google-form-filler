# google-form-filler

## Description

Provided script allows quickly fill the google form of our english class.

Pass arguments in the format: `<bool> <presenter name> <presentation title>`

Where:
1) `<bool> = 1` - Firefox browser is called
2) `<bool> = 0` - Chrome browser is called

## Example:
`python3 main.py "Absract Student" "Abstract topic"`

## Requirements

* `sudo apt-get install chromedriver`
* `sudo apt-get install firefox-geckodriver`
* python 3
* selenium (python package)
