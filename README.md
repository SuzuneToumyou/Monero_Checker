# Monero_Checker
This Python script retrieves Monero (XMR) mining data from Nanopool every 10 minutes and displays the current XMR balance and its equivalent in Japanese Yen (JPY).  It uses live exchange rates for JPY conversion.

## Features
Real-time data: The mining earnings from Nanopool are updated every 10 minutes.
Live conversion: The current value of Monero is converted into Japanese Yen (JPY) using real-time exchange rates.
PyQt5 UI: A simple graphical user interface to view your mining stats and earnings.

## Notes
Make sure you have PyQt5 installed, as it's necessary for the graphical interface.
Replace the placeholder xmr_adress with your actual Nanopool mining address.
This script works by fetching data from Nanopool's API, so ensure you're connected to the internet.
