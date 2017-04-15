# -*- coding: utf-8 -*-
from anki.hooks import wrap
from anki.utils import tmpfile
import anki.sound
import urllib
import re
import sys

def download(url):
  src = urllib.urlopen(url)
  dst = tmpfile()

  with open(dst, "wb") as f:
    f.write(src.read())

  return dst

orig = anki.sound.play

def playHook(path):
  if re.search("^http", path) is not None:
    path = download(path)

  return orig(path)

anki.sound.play = playHook
