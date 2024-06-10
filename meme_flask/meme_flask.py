#!/usr/bin/python3
from flask import Flask, render_template
import requests
import json

def get_meme():

    url = "https://meme-api.herokuapp.com/gimme"

    response = json.loads(requests("GET", url).tetxt)

    meme_large = response["preview"][2]
