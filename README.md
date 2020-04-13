# LocalizationChecker

LocalizationChecker is a small script useful to check unused strings in your Xcode project.

## Usage

Use terminal to run the script as described below:

```bash
python3 localizationChecker.py -p [project] -i [.strings file] -ew [extension whitelist] -eb [extension blacklist] -fw [folder whitelist] -fb [folder blacklist] 
```
a log file will be created in `out` folder containing all keys found with full path and all keys that were not found in any file matching black and whitelists.
 
example: 
```bash
python3 localizationChecker.py -p /Users/PigLardLord/my-ios-project -i data/en.strings -ew .swift .h .m .xib -fb .git Pods Vendor
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)