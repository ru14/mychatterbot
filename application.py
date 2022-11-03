#! /usr/bin/python3
from flask import FLask, render_template, requests
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useGoogle, confidenceLevel
from botRespond import getResponse
