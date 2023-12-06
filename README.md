# Pyblish Maya plugin

A Maya plugin wrapper for [pyblish-maya](https://github.com/pyblish/pyblish-maya)  
Easily enable and disable Pyblish in Maya

![image](https://github.com/hannesdelbeke/pyblish-maya-plugin/assets/3758308/d95250f5-2c94-4f8f-8015-f3f56ff83546)

## Features
When plugin is enabled:
- register `pyblish-lite` as default gui
- run pyblish-maya setup
    - add Pyblish to menu `File/Publish`
    - register default plugins
    
Plugin cleans up menu when disabled

## Install
### 1-click install with Plugget
1. install [plugget for maya](https://github.com/plugget/plugget-qt-maya-plugin)
2. search and install the `pyblish` plugget package 

### Manual install
- manually pip install the requirements in the maya scripts folder
- copy the pyblish-maya-plugin in the plug-ins folder
- enable the plugin in maya from the menu  `window` > `settings/preferences` > `Plug-in Manager`
 
<details>
<summary>Manual install isntructions </summary>
1. install dependencies to `Documents/Maya/scripts`
    
```
python -m pip install pyblish-lite, pyblish-maya --target "C:/Users/%username%/Documents/Maya/scripts"
```
(To install for a specific Maya version only, e.g. 2022, replace `Maya/scripts` with `Maya/2022/scripts`)

2. install plugin  
  - manually copy the python file in your maya plugi-ins directory, 
<!--
  - or install (from repo) without dependencies to `Documents/Maya/plug-ins`

```
python -m pip --no-dependencies install https://github.com/hannesdelbeke/pyblish-maya-plugin/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins"
```
-->

3. Open the plugin manager, and load the plugin.
4. A new menu should show `Tools`, open the window from here.
</details>


## other
- plugget package https://github.com/plugget/plugget-pkgs/tree/main/maya/pyblish
