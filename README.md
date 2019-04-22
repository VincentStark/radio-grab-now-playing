## radio-grab-now-playing

Python script to grab "Now Playing" info from radio stations.

radio-grab-now-playing uses server-based webpage rendering to get this information.

## Required Libraries

* [spynner](https://github.com/makinacorpus/spynner) (Server-based HTML5/JavaScript renderer)
* [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/#Download) (HTML DOM Parser)
* [Jinja2](https://github.com/mitsuhiko/jinja2) (Template Engine)

## Installation

The installation might be a little bit tricky on some platforms, especially on OS X. The reason for that is simple - this script requires [spynner](https://github.com/makinacorpus/spynner) library, which is responsible for server-based HTML5/JavaScript rendering. It has numerous dependencies, which can be difficult to install properly.

If you're interested in detailed installation instructions or have problems with required libs on any platform - please let me know and I will help you.

## Usage

Add URLs to ```etc/radio-grab-now-playing.conf``` file and launch ```radio-grab-now-playing.py``` script.

```output/now-playing.csv``` file will be generated.

```
usage: radio-grab-now-playing.py [-h] [--version]

Grabs Now Playing from radio stations
    
optional arguments:
  -h, --help  show this help message and exit
    --version   show program's version number and exit
```

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

Copyright (c) 2013 vst42
