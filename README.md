# Pyblish Maya plugin

A Maya plugin wrapper for [pyblish-maya](https://github.com/pyblish/pyblish-maya)  

## Features

- register `pyblish-lite` as default gui
- run pyblish-maya setup
    - add Pyblish to menu `TODO/MENU`
      > TODO
    - register default plugins

## Install
### 1-click install with Plugget
> TODO

### Manual install
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
- plugget package
> TODO
