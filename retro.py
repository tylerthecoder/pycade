import os
import glob

RUNCOMMAND = "/opt/retropie/supplementary/runcommand/runcommand.sh"
ROM_PATH = "/home/pi/RetroPie/roms/nes"

def run_rom(system: str, romPath: str):
	print( 'Running rom1: {}'.format( romPath ) )
	cmd = "sudo DISPLAY=:0 {} 0 _SYS_ {} '{}'".format( RUNCOMMAND, system, romPath )
	os.system(cmd)

def get_all_roms():
	return glob.glob(ROM_PATH + "/*")