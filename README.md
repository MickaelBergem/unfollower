# Unfollower

Find out who unfollow you on Twitter.

This is a very simple and minimalistic script, intended for my personnal use.
Feel free to adapt it to your needs !

In the current version, it will run until you press Ctrl+C (or you kill the process).
Intended to run inside a *tmux* (or other *screen*), for example.

## Installation

    git clone https://github.com/MickaelBergem/unfollower.git && cd unfollower
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

You will then have to get consumer key and access tokens to be able to communicate with the Twitter API.
Procedure described [here](https://github.com/bear/python-twitter#api).

## Usage

You will always need to enter the virtualenv :

    source env/bin/activate

Then :

    python unfollower.py
