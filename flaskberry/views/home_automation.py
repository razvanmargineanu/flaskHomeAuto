# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, flash
import RPi.GPIO as GPIO
import time as theTime
import subprocess


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

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


@mod.route('/turnLightOFF')
def turnLightOFF():
    flash("Turning the lights Off")
    turnTheLightsOFF()
    return redirect(url_for('home_automation.index'))

@mod.route('/turnLightON')
def turnLightON():
    flash("Turning the lights On")
    turnTheLightsON()
    return redirect(url_for('home_automation.index'))


def turnTheLightsON():

    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, True)
    print "Light ON"
    theTime.sleep(0.5)
    GPIO.output(24,False)
    GPIO.cleanup()


def turnTheLightsOFF():


    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, True)
    print "Light ON"
    theTime.sleep(0.5)
    GPIO.output(23,False)
    GPIO.cleanup()