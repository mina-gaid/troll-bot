# shitpost-learner

Learn to shitpost.

This script trains a Markov chain on all posts on all pages of the board specified by the user and generates shitposts on command. Posts are saved to a csv file so posts should improve over time. This script makes use of 4chan's read-only JSON API.

## Installation

``` shell
git clone https://github.com/mina-gaid/shitpost-learn.git
cd shitpost-learn
pip install -r requirements.txt
```

## Usage

```
usage: shitposter.py [-h] board

positional arguments:
  board       The board to get shitposts from.

optional arguments:
  -h, --help  show this help message and exit
```

### Example

``` shell
python shitposter.py /pol/
```
