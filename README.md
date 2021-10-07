1.open the i2c
2.set I2C baudrate on /boot/config.txt file
sudo nano /boot/config.txt

add the following in the last line 
dtparam=i2c1_baudrate=1000000

3.reboot raspberrypi

4.python3 mlx90640.py
