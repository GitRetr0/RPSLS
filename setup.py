from setuptools import setup

APP = ['RPS2.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'plist': {
        'LSUIElement': True
    },
    'includes': ['pyobjc', 'pyobjc-framework-Cocoa']
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],        
)