import zipfile

OUTPUT = "./xapk-unpacked/"

def unpack_xapk(xapk_path):
    with zipfile.ZipFile(xapk_path, 'r') as zip:
        zip.extractall(OUTPUT)

unpack_xapk("./home.cleaning.clean.house.cleanup.game.deep.dream.messy.house.cleanup.games.girl.princess.tidy.tody.xapk")


# Function GetURL(rng As Range) As String
#      On Error Resume Next
#      GetURL = rng.Hyperlinks(1).Address 
# End Function

# https://apkpure.com/app
# CATEGORIES
#
# Art & Design
# Auto & Vehicles
# Beauty
# Books & Reference
# Business
# Comics
# Communication
# Dating
# Education
# Entertainment
# Events
# Finance
# Food & Drink
# Health & Fitness
# House & Home
# Libraries & Demo
# Lifestyle
# Maps & Navigation
# Medical
# Music & Audio
# News & Magazines
# Parenting
# Personalization
# Photography
# Productivity
# Shopping
# Social
# Sports
# Tools
# Travel & Local
# Video Players & Editors
# Weather


# https://apkpure.com/game
# CATEGORIES
#
# Action
# Adventure
# Arcade
# Board
# Card
# Casino
# Casual
# Educational
# Music
# Puzzle
# Racing
# Role
# Playing
# Simulation
# Sports
# Strategy
# Trivia
# Word
# Family
