import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder1 = glob.glob(base_dir + '10-00*')[0]
device_file1 = device_folder1 + '/w1_slave'

def read_temp_raw1():
    f = open(device_file1, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp1():
    lines = read_temp_raw1()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw1()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

main_str = """
        <html>
        <header><title>Pomiar temperatury</title></header>
        <body bgcolor="silver">
        <b>Witaj, oto program mierzacy temperature w pokoju<b><br><br>
        </body>
        </html>

        <head>
        <meta http-equiv="Refresh" content="5" />
        </head>
        """

norm_str = """
        <font color="green">Temperatura w normie</font>
        <br>
        """

hot_str = """
        <font color="yellow">Jest za goraco, otworz okno!</font>
        <br>
        """

very_hot_str = """
        <font color="red">Jest za goraco, udusisz sie!</font>
        <br>
        """

cold_str = """
        <font color="blue">Zamknij okno, jest za zimno!</font>
        <br>
        """

plik_html = open("/home/skik/skikpw.github.io/index.html", "w")
plik_html.write(main_str)
plik_html.close()
temperature = 0.0

licznik=0
while True:
        licznik+=1
        plik_html = open("/home/skik/skikpw.github.io/index.html", "a+")
        temperature1 = read_temp1()
        plik_html.write(str(temperature1))
        plik_html.write("<br>")

        if temperature1 < 24:
                plik_html.write(cold_str)
        elif temperature1 > 30:
                plik_html.write(very_hot_str)
        elif temperature1 > 27:
                plik_html.write(hot_str)
        else:
                plik_html.write(norm_str)

        print(str(temperature1))
        print(" ")
        plik_html.close()
        if licznik>=20:
                break






