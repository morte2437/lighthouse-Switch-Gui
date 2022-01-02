# lighthouse-Switch-Gui
GUI for easy light house discovery and power switching works with V1 and V2

Created from code created by [rossbearman](https://github.com/rossbearman) for [Lighthouse-Keeper](https://github.com/rossbearman/lighthouse-keeper)


## Prerequisites
### Binary
* Windows 10
* Bluetooth 4.0/BLE chip (integrated or external), managed by Windows

### Python Script
* Python 3.6
* bleak BLE library, minimum version 0.10.0

## Compiling an Executable
PyInstaller is used to generate an executable from the source. Run the following command in the root folder:

`pyinstaller --onefile .\lighthouse_keeper.py`

If you install PyInstaller via `pip`, Windows Defender will often flag any compiled executables. You can typically fix this by compiling PyInstaller's bootloader yourself and installing it manually, rather than using `pip`.

1. `git clone https://github.com/pyinstaller/pyinstaller`
2. `cd pyinstaller/bootloader`
3. `py ./waf distclean all`
4. `cd ..`
5. `py setup.py install`


## Acknowledgements
[rossbearman](https://github.com/rossbearman) for building the entire code I only made the GUI. [monstermac77](https://github.com/monstermac77) and [PumkinSpice](https://github.com/PumkinSpice) for their work on the [MixedVR Manager](https://github.com/monstermac77/vr), the [WMR MixedVR guide](https://github.com/PumkinSpice/MixedVR/wiki/ReadMe) and their extensive testing of this script.
