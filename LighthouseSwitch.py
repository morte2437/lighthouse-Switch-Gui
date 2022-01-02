#!/usr/bin/env python3

import asyncio
import logging
from lighthouse import LighthouseV1, LighthouseV2
from locator import LighthouseLocator
from output import output
import PySimpleGUI as sg
from os.path import exists


logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('error')


versionlist = []
lighthouselist = []


layout = [[sg.Button('Discover'), sg.Button('Load Previous'), sg.Button('Clear Previous')],
          [sg.Listbox(values=lighthouselist, size=(30, 3), key='-LIST-')],
          [sg.Button('ON'), sg.Button('OFF')],
          [sg.Output(key='-OUTPUT-', size=(80, 20))]
          ]
window = sg.Window('LightHouse Switcher', layout)


def create_lighthouse(address):
    if "HTC BS" in versionlist:
        return LighthouseV1(address)
    else:
        return LighthouseV2(address)


loop = asyncio.get_event_loop()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close(); del window
        break
    if event == "Discover":

        output.info("Searching for lighthouses, this may take several minutes.")
        lighthouselist = []
        versionlist = []
        while len(lighthouselist) < 2:
            lighthouses = asyncio.run(LighthouseLocator().discover())

            if not lighthouses:
                output.info("No lighthouses found.")
                break

            for lighthouse in lighthouses:
                output.info("Found " + str(lighthouse.version) + ".0 lighthouse '" + lighthouse.name + "' identified by '" + lighthouse.address + "'.")
                lighthouselist.append(str(lighthouse.address))
                versionlist.append(lighthouse.name_prefix)
            window['-LIST-'].update(lighthouselist)
            with open('versionlist.txt', 'w+', encoding='utf-8') as f:
                for items in versionlist:
                    f.write(items+'\n')
            f.close()
            with open('savedlist.txt', 'w', encoding='utf-8') as f:
                for items in lighthouselist:
                    f.write(items+'\n')
            f.close()

    if event == "Load Previous":
        with open('savedlist.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for items in data:
                new_item = items.replace('\n', '')
                lighthouselist.append(new_item)
            window['-LIST-'].update(lighthouselist)
            if data:
                print('Previous MAC addresses loaded')
            else:
                print('Previous data not found')

        with open('versionlist.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for items in data:
                new_item = items.replace('\n', '')
                versionlist.append(new_item)


    if event == "Clear Previous":
        with open('savedlist.txt', 'w+', encoding='utf-8') as f:
            for items in f:
                f.writelines('')
            lighthouselist = []
            window['-LIST-'].update(values=lighthouselist)
            window.refresh()
            print('Previous MAC addresses cleared')
        f.close()
        with open('versionlist.txt', 'w+', encoding='utf-8') as f:
            for items in f:
                f.writelines('')
            versionlist = []
        f.close()


    if event == "OFF":
        for lighthouse in map(create_lighthouse, lighthouselist):
            asyncio.run(lighthouse.run_command(loop, 'off'))
    if event == "ON":
        for lighthouse in map(create_lighthouse, lighthouselist):
            asyncio.run(lighthouse.run_command(loop, 'on'))


if __name__ == "__main__":
    if exists('savedlist.txt'):
        with open('savedlist.txt', 'r', encoding='utf-8') as f:
            event, values = window.read()
            data = f.readlines()
            if data:
                print('Previous MAC addresses loaded')
            for items in data:
                new_item = items.replace('\n', '')
                lighthouselist.append(new_item)
            window['-LIST-'].update(lighthouselist)

        with open('versionlist.txt', 'r', encoding='utf-8') as f:
            event, values = window.read()
            data = f.readlines()
            for items in data:
                new_item = items.replace('\n', '')
                versionlist.append(new_item)
    else:
        with open('savedlist.txt', 'w+', encoding='utf-8') as f:
            event, values = window.read()
            data = f.readlines()
            if data:
                print('Previous MAC addresses loaded')
            for items in data:
                new_item = items.replace('\n', '')
                lighthouselist.append(new_item)
            window['-LIST-'].update(lighthouselist)

        with open('versionlist.txt', 'w+', encoding='utf-8') as f:
            event, values = window.read()
            data = f.readlines()
            for items in data:
                new_item = items.replace('\n', '')
                versionlist.append(new_item)



