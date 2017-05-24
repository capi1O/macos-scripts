Set of scripts for mac power users.

- add cut/paste functionality to macOS Finder with standard keyboard shortcuts (cmd-X cmd-V).
- add launch terminal here.


Those applescripts are made to be used with FastScripts, by assigning cmd-C cmd-X and cmd-V keyboard shortcuts :

- cmd-C -> cmd-c.applescript
- cmd-X -> cmd-x.applescript 
- cmd-V -> cmd-v.applescript
- maj-cmd-T -> open-iterm-here.applescript 

## Instructions for FastScripts 

- create subdir Applications/Finder.
- place the 3 applescripts there
- set shortcuts in FastScripts Preferences.

## dependancies

### cmd-v.applescript

	- developper tools for xcode.



## Useful ressources

- https://stackoverflow.com/questions/37105734/run-applescript-application-on-any-left-click-mouse-listener-or-third-party-ext
- https://stackoverflow.com/questions/1770312/is-there-a-sendkey-for-mac-in-python

## TODO

### cut/paste

should not cmd-cut when selecting text and cuting/copying.


### mouse-watcher.py
	- replace NSEventMask constants by type properties https://developer.apple.com/reference/appkit/nseventmask
	- disable paste on defined areas : in Finder folder view, text fields... For example in Finder it should not paste inactive directory if middle-clicking a favourite folder in sidebar
	
### duplicate real

- support directories

### make symlink

- support directories