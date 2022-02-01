from Ejecutables.Backend.emulator.managerEmu.salasManager import SalasManager
import schedule 
import time

from random import randrange
from configurationEmu.emulatorConfig import ConfigEmu
from managerEmu import salasManager

def initSalas():

    print ("Creando salas...")
    managerSalas = SalasManager()
    
    print ("Random number...")
    number = randrange(10)
    print ("Number " + str(number))

    managerSalas.printStatus()

def job():
    sensorNumber = numberSensor()
    accion = enterOrExit()
    printStatusAccion(accion, sensorNumber)

def printStatusAccion (accion, sensor) :
    if (accion == ConfigEmu.ENTER):
        print("ENTRAR - Sensor" + str(sensor))
    else:
        print("SALIR - Sensor" + str(sensor))

def numberSensor():
    salaNumber = randrange(ConfigEmu.MAX_SALAS)
    return salaNumber

def enterOrExit ():
    typeEnter = randrange(2)
    return typeEnter

salesManager = SalasManager()
schedule.every(ConfigEmu.RELOJ).seconds.do(job)
while True: 
    schedule.run_pending()
    time.sleep(1)