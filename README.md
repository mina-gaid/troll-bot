# troll-learner

Learn to troll.

This script trains a Markov chain on all posts on all pages of the board specified by the user and generates trolls on command. Posts are saved to a csv file so posts should improve over time. This script makes use of 4chan's read-only JSON API.

## Installation

``` shell
git clone https://github.com/mina-gaid/troll-learn.git
cd troll-learn
pip install -r requirements.txt
```

## Usage

```
usage: troll.py [-h] board

positional arguments:
  board       The board to get trolls from.

optional arguments:
  -h, --help  show this help message and exit
```

### Example

``` shell
python troll.py /pol/
```
