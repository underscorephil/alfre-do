# alfre-do 
A simple [Alfred](http://www.alfredapp.com/) workflow for [2do](http://2doapp.com/)

## Installation
Download a [release](https://github.com/underscorephil/alfred-2do/releases) and [import](http://support.alfredapp.com/workflows:installing) the workflow.

## Syntax
Supports task title, tags, and a speified or default list.
### Creating a task
```
twodo [Task title] [#tags...] [:list]
```
### Setting a default list
```
twodo default list [list name]
```
## Examples
### Specifying a list and tags
```
twodo Create a 2do workflow for Alfred #alfred #2do :Projects
```
### Using default list
```
twodo Restring ye old guitar #guitar #chore
```
## Thanks
[Dean Jackson](https://github.com/deanishe) and the https://github.com/deanishe/alfred-workflow

[Caleb Grove](http://calebgrove.com/) for the [idea](http://www.alfredforum.com/topic/3811-2do-workflow/?p=22721)
