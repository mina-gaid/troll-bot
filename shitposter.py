import requests
import re
import csv
import os
import errno
import sys

try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

import markovify
import argparse

h = HTMLParser()


def get_threads(board):
    req = requests.get('https://a.4cdn.org%scatalog.json' % board)
    json = req.json()
    threads = json[2:]
    return threads


def clean_html_string(html_string):
    clean_str = h.unescape(
        re.sub(r'(<(.*)>)', ' ', html_string)).encode('utf-8')
    clean_str = re.sub(r'[:\s]*http\S+(|\s)', '', clean_str).strip()
    return clean_str


def has_post(post_number, csv_file):
    with open(csv_file) as y:
        p = csv.reader(y, delimiter=',')
        for d in p:
            if str(post_number) == str(d[0]):
                return True
        return False


def train(board):
    threads = get_threads(board)
    fn = 'data/%s.csv' % board[1:-1]
    aw = "a+" if os.path.exists(fn) else 'w+'
    q = open(fn, aw)
    writer = csv.writer(q)
    for thread in threads[0]['threads']:
        if 'com' in thread and (not has_post(thread['no'], fn)):
            op = clean_html_string(thread['com'])
            if op and op.strip():
                writer.writerow([thread['no'], op])
        if 'last_replies' in thread:
            for reply in thread['last_replies']:
                if 'com' in reply and (not has_post(reply['no'], fn)):
                    p = clean_html_string(reply['com'])
                    if p and p.strip():
                        writer.writerow([reply['no'], p])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("board", help='The board to get shitposts from.')
    args = parser.parse_args()
    try:
        os.makedirs("data")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print("Training, this may take a while...")
    train(args.board)
    with open('data/%s.csv' % args.board[1:-1]) as f:
        c = csv.reader(f, delimiter=',')
        k = [r[1] for r in c]
        if not k:
            sys.exit("No posts found...")
        text_model = markovify.Text(k, state_size=1)
        sp = text_model.make_sentence()
        print(sp)
