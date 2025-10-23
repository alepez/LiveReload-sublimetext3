## ⚠️ Repository Archived

This repository is no longer maintained and has been archived.

I originally forked this project after it was abandoned over 10 years ago, but I have not used or updated it in many years. See https://github.com/alepez/LiveReload-sublimetext3/issues/10

**No further updates, bug fixes, or support will be provided.**

If you are interested in continuing development, feel free to fork the repository.

Thank you for your understanding.

# LiveReload for Sublime Text 3

A web browser page reloading plugin for the [Sublime Text 3](http://sublimetext.com "Sublime Text 3") editor.

## Installing

With [Package Control](http://wbond.net/sublime_packages/package_control):

1. Run “Package Control: Install Package” command, find and install `LiveReload` plugin.
2. Restart ST editor (if required)

### Manual install, Linux users

```
cd ~/.config/sublime-text-3/Packages
rm -rf LiveReload
git clone https://github.com/alepez/LiveReload-sublimetext3 LiveReload
```

### Manual install, OSX users

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
rm -rf LiveReload
git clone https://github.com/alepez/LiveReload-sublimetext3 LiveReload
```

# Using

Enable desired plug-ins via Command Palette (Ctrl+Shift+P) add livereload.js to you html document.

```
<script>document.write('<script src="http://' + (location.host || '${1:localhost}').split(':')[0] + ':${2:35729}/livereload.js?snipver=1"></' + 'script>')</script>
```

You can also use one of the extensions listed here http://livereload.com/extensions/

## Available plug-ins:

 - Compass Preprocessor, compiles .scss, .sass and refreshes page when file is compiled
 - Less Preprocessor, compiles .less and refreshes page when file is compiled
 - Sass Preprocessor, compiles .scss, .sass with the latest installed sass version and refreshes page when file is compiled
 - CoffeeScript Preprocessor, compiles .coffee and refreshes page when file is compiled
 - Simple Reload, refresh page when file is saved
 - Simple Reload with delay(400ms), wait 400ms then refresh page, when file is saved

## Examples

 - Simple Reload from http GET request, reloads page on visit to http://localhost:35729/callback/simplereloadplugincallback/on_post_compile
 - Send content on change, sends file content to browser console

## Sass Preprocessor usage

First, install latest version of sass
```bash
sudo gem install sass
```
Activate the plugin in SublimeText3 via the `package settings -> livereload -> plugins -> enable/disable plugins` menu

By default, the plugin save the compiled css in same dir of sources.
You can change this by creating a `sass_config.json` file near your sources:
```json
{
    "destination_dir": "../../webroot/css"
}
```

# Plug-in api

https://livereload-for-sublime-text.readthedocs.org/en/latest/

# Thanks

The original plugin was written by [Janez Troha](https://github.com/dz0ny)

