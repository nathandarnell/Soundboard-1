
Python library installation:
pip install pygame

Get the pi user to be able to play audio
sudo usermod -a -G audio pi

Enable it to run at boot:

sudo cp soundboard.service /etc/systemd/system/
sudo systemctl enable soundboard
