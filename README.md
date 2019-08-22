# Rule34 Downloader
<div style="text-align: center; border-radius: 10px; background: linear-gradient(325deg, rgba(2, 0, 36, 1) 0%, rgba(185, 0, 255, 1) 0%, rgba(0, 255, 206, 1) 100%); webkit-box-shadow: 10px 10px 30px 0px rgba(0, 0, 0, 0.35); -moz-box-shadow: 10px 10px 30px 0px rgba(0, 0, 0, 0.35); box-shadow: 10px 10px 30px 0px rgba(0, 0, 0, 0.35);">
  <img src="https://rule34.xxx/images/header2.png"/>
</div>

### What does it do?
It downloads every image it can find matching the given tags from Rule34.

## Dependencies
- Python 3.6
- [LordOfPolls' Rule34 API wrapper](https://github.com/LordOfPolls/Rule34-API-Wrapper)

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
