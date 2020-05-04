# pyGithubAvatar

## Main purpose
Use python to generate github avatar

Default github avatar is a 420x420 png image, with 35px as border, and left-right symmetrical color blocks.

This simple python code will help you to generate image file with two digit number, similar like github avatar style.

## Usage

Simply import `CharAvatar` class and run `avatar(twoChars, path='path')` like below:

```python
from pyGithubAvatar import CharAvatar

gca = CharAvatar()
gca.avatar(42, path='img/42.png')
```

## Options

You can also customize it with below options:

```python
gca_options = {
    'top_border': 10,
    'left_border': 20,
    'right_border': 20,
    'bottom_border': 10,
    'line_width': 20,
    'line_height': 10,
    'bg_rgba': [60, 60, 60, 255],
    'fg_rgba': [200, 60, 60, 255],
}

gca = CharAvatar(**gca_options)
gca.avatar('RS') # if no path specified, will plot in window or shown in jupyter notebook
```
![RS](./img/RS.png)

## License

Licensed under the [MIT](LICENSE.txt) license.