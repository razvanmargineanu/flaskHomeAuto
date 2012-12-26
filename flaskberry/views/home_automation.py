# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, flash

import time as theTime
import subprocess



def check_output(*args):
    return subprocess.Popen(*args, stdout=subprocess.PIPE).communicate()[0]
def list_folder(*args):
    return subprocess.Popen(*args, stdout=subprocess.PIPE).communicate()[0]

mod = Blueprint('home_automation', __name__)

@mod.route('/')
def index():
    uptime = check_output(["uptime"])
    list_folder1 = list_folder(['ls'])
    return render_template('home_automation/home_automation.html', uptime=uptime, list_folder = list_folder1)

