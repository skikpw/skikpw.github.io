import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder1 = glob.glob(base_dir + '28-00*')[0]
device_file1 = device_folder1 + '/w1_slave'

#device_folder2 = glob.glob(base_dir + '28-03168*')[0]
#device_file2 = device_folder2 + '/w1_slave' 

#device_folder3 = glob.glob(base_dir + '28-04168*')[0]
#device_file3 = device_folder3 + '/w1_slave' 


def read_temp_raw1():
    f = open(device_file1, 'r')
    lines = f.readlines()
    f.close()
    return lines

#def read_temp_raw2():
 #   f = open(device_file2, 'r')
  #  lines = f.readlines()
   # f.close()
    #return lines

#def read_temp_raw3():
 #   f = open(device_file3, 'r')
  #  lines = f.readlines()
   # f.close()
    #return lines


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


#def read_temp2():
 #   lines = read_temp_raw2()
  #  while lines[0].strip()[-3:] != 'YES':
   #     time.sleep(0.2)
    #    lines = read_temp_raw2()
    #equals_pos = lines[1].find('t=')
    #if equals_pos != -1:
     #   temp_string = lines[1][equals_pos+2:]
      #  temp_c = float(temp_string) / 1000.0
       # return temp_c

#def read_temp3():
 #   lines = read_temp_raw3()
  #  while lines[0].strip()[-3:] != 'YES':
   #     time.sleep(0.2)
    #    lines = read_temp_raw3()
    #equals_pos = lines[1].find('t=')
    #if equals_pos != -1:
     #   temp_string = lines[1][equals_pos+2:]
      #  temp_c = float(temp_string) / 1000.0
       # return temp_c

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

plik_html = open("/home/pi/strona/skikpw.github.io/index.html", "w")
plik_html.write(main_str)
plik_html.close()
temperature = 0.0

licznik=0
while True:
	licznik+=1
        plik_html = open("/home/pi/strona/skikpw.github.io/index.html","a+")
        temperature1 = read_temp1()
#        temperature2 = read_temp2()
 #       temperature3 = read_temp3()
        plik_html.write(str(temperature1))
        plik_html.write("<br>")
  #      plik_html.write(str(temperature2))
   #     plik_html.write("<br>")
    #    plik_html.write(str(temperature3))
     #   plik_html.write("<br>")

        if temperature1 < 24:
                plik_html.write(cold_str)
        elif temperature1 > 30:
                plik_html.write(very_hot_str)
        elif temperature1 > 27:
                plik_html.write(hot_str)
        else:
                plik_html.write(norm_str)

        print(str(temperature1))
        #print(str(temperature2))       
        #print(str(temperature3))       
        print(" ")
        plik_html.close()
	if licznik>=20:
		break






