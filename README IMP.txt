import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk  # Import Pillow
import subprocess
import email
from email import policy
from genericpath import exists
import sys
import os
import re
from typing import Final
import colorama
import extract_msg
from colorama import Fore, init
init(autoreset=True)
colorama.init(autoreset=True)
Paths neaded to be changed in the scripts
create a input output folder for saving the files
in input folder donload and save the emails in .eml or .msg formate
