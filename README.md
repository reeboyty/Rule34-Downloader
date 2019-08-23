# Rule34 Downloader
<div style="text-align: center">
  <img src="https://rule34.xxx/images/header2.png"/>
</div>

### What does it do?
It downloads every image it can find matching the given tags from Rule34.

## Dependencies
- Python 3.6
- [LordOfPolls' Rule34 API wrapper](https://github.com/LordOfPolls/Rule34-API-Wrapper)

### Installation
> While in the program directory, type `pip3 install -r requirements.txt`  
> Then just execute the script with `python3 *scriptname* --help` to see the help page

**WITH WINDOWS EXECUTABLE**  
> There's also a windows executable compiled inside the `releases` tab. Just download it and 
> start it with the `command prompt`.

## FAQ
**Can I search for more than one tag at once?**
> Yes, you can. The script treats each word as a single tag.  
> For example you can search for `pokemon serena` and it will
> search for `pokemon` and for `serena`

**Can I download a specific amount of images?**
> Yes, among the parameters you can specify a limit for the amount
> of downloaded images

**Can I skip videos and download images only?**
> Yes, you can there's a parameter to specify to do that.

**Why doesn't it have a GUI?**
> There's no need to implement a GUI, since the script only
> takes inputs from command line arguments

## Changelog
**v1.1-alpha**
- Fixed a bug where searching for some tags gave errors and crashed the program.

**v1.0-alpha**
- Project created
