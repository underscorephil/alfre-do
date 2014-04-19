alfred-2do
==========
A simple [Alfred](http://www.alfredapp.com/) workflow for [2do](http://2doapp.com/)

## Installation
Download a [release](https://github.com/underscorephil/alfred-2do/releases) and [import](http://support.alfredapp.com/workflows:installing) the workflow.

## Syntax
Supports task title, tags, and a speified or default list.
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
