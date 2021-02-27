# Find slots

Small bot for checking if there are correction slots on the 42 intranet.

## Technical details

This program uses selenium to launch a Firefox browser.
It will then refresh the page every minute and notify with a sound when there is an available slot on the page.
It also shows progress in the terminal like so : `.....!.` where '.' means that there are no available slots and '!' means the bot found a slot on the page.

## Usage

  Set environment

  ```
  make env
  ```

  Launch

  ```
  make
  ```

## Current requirements

 - [x] python selenium      # main part, actual bot
 - [x] python time          # waiting
 - [x] python chime         # for the sound notifications
 - [x] python signal        # for proper interruption handling
 - [x] Firefox              # browser used by the bot
 - [x] geckodriver          # needed by Selenium

## What you should expect

While the program is working, it is displaying dots, just so you know its active. Once a slot is found, a *!* will appear and you will hear a sound.
