<div align='center'>
    <h1>Engine</h1>
</div>

Engine - is a simple and not very user-friendly tool for creating a graphical user interface (GUI) in Python.

+ [Installation](#installation)
+ [Usage](#usage)
+ [License](#usage)

## Installation

To install the Engine you can use git:

```bash
git clone https://github.com/crelgd/engine
cd engine
```

## Usage
An example of creating a window with text:
```python
from Engine import Window
from Engine import Label 

window = Window()
window.create()

label = Label(text='Example Text', size=25)
label.setPos(x=100, y=100)

window.winLoop([label.render])
```


You can find other examples [here](Engine/examples/).


## License
Engine is distributed under the MIT license. Detailed information can be found in the [LICENSE](LICENSE) file.