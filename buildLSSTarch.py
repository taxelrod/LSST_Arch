#!/usr/bin/env python

import sys
import buildCSCdot as bcsc

if __name__ == "__main__":

    outFileName = sys.argv[1]
    
    dot=bcsc.startDot('Main\ Telescope\ Architecture\ V1\ Sep\ 13,\ 2018')

#
# MTMount
#
    dot=bcsc.addHWCSC(dot, 'MTMount', 'MTMount_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtMCS', 'Code repo:  ?','ICD:  https://ls.st/LTS-159?',  'ICD_differs_for_AT??', 'CSC generic cmds' ,'startTracking', 'trackTarget', 'stopTracking', 'setInstrumentPort'], ['MTMount'], implemented=False)
    
#
# hexapod
#
    dot=bcsc.addHWCSC(dot, 'hexapod', 'Hexapod_HW', ['XML repo: ?','Code repo: https://github.com/lsst-ts/ts_atm2hexapod','ICD: ?', 'CSC generic cmds'], ['M2 Hexapod', 'Camera Hexapod'], implemented=False)
    
#
# Dome
#
    dot=bcsc.addHWCSC(dot, 'Dome', 'Dome_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtDome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'CSC generic cmds', 'Crawl', 'Move','Park','SetLouvers','CloseShutter','OpenShutter','StopShutter'], ['Dome'], implemented=False)
#
# m1m3
#
    dot=bcsc.addHWCSC(dot, 'm1m3', 'm1m3_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['m1m3 cRIO', 'Thermocouples', 'Accelerometers'], implemented=True)
#
# IOTA
# - note connects to tcsWEP
#
    dot=bcsc.addHWCSC(dot, 'IOTA', 'IOTA_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['High Speed CMOS Camera', 'SHWFS' ], implemented=False)
#
# WEP_Server
#
    dot=bcsc.addHWCSC(dot, 'WEP_Server', 'WEP_Server_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Data Processor', 'Storage'], implemented=False)

#    dot=bcsc.addSubHW(dot, 'WEP_Server_HW', ['IOTA'], ['WEP_Server_HW'])

#
# laser tracker
#
#
    dot=bcsc.addHWCSC(dot, 'LaserTracker', 'LaserTracker_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['LaserTracker'], implemented=False)
#
# guider
#
    dot=bcsc.addCSC(dot, 'Guider', ['XML repo: ?','Code repo: ?','ICD: ?','CSC generic cmds'], implemented=False)
    dot=bcsc.addSubHW(dot, 'DAQ', ['Guider'], ['DAQ'])

#
# CalCS
#
    dot=bcsc.addCSC(dot, 'CalCS', ['XML repo: ?','Code repo:  ?','ICD: LSE-139','CSC generic cmds'],implemented=False)

    dot=bcsc.addHWCSC(dot, 'TunableLaser', 'TunableLaser_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['TunableLaser#1','TunableLaser#2'], implemented=False)

    dot=bcsc.addHWCSC(dot, 'WhiteLightSource', 'WhiteLightSource_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['WhiteLightSource'], implemented=False)
    
    dot=bcsc.addHWCSC(dot, 'PhotoDiodes', 'PhotoDiodes_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['PhotoDiodes'], implemented=False)
    
    dot=bcsc.addHWCSC(dot, 'SEDSpectrograph', 'SEDSpectrograph_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['SEDSpectrograph'], implemented=False)

    dot=bcsc.addHWCSC(dot, 'CalibrationScreen', 'CalibrationScreen_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['CalibrationScreen'], implemented=False)
    
    dot=bcsc.addHWCSC(dot, 'CBP', 'CBP_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Collimated Beam Projector'], implemented=False)
    

#
# m2ms
#
    dot=bcsc.addHWCSC(dot, 'm2ms', 'm2_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['m2_controller'], implemented=False)
#
# ECS (Environment Control System)
#
    dot=bcsc.addHWCSC(dot, 'ECS', 'CVAC', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Chillers','AirHandlineUnits','CVACSensors','Fans','Valves'], implemented=False)

#
# EMCS (environmental monitor control system)
#
    dot=bcsc.addHWCSC(dot, 'EMCS', 'environmental_monitoring_HW', ['XML repo: ?','Code repo:  ?','ICD: LSE-139','CSC generic cmds'], ['Seismic_Monitors','Anemometers','Visible_All-Sky Camera','Infrared_All-Sky Camera','DIMM','Weather_Station','GPS_Water_Vapor_Monitor'], implemented=False)

#
# LOVE (LSST Operator Visuzlization Environment)
#
    dot=bcsc.addHWCSC(dot, 'LOVE', 'Visualization_HW', ['Vendor: INRIA','XML repo: ?','Code repo:  ?','ICD: ?', 'Req: LTS-807', 'CSC generic cmds'], ['Visualization Server', 'Displays'], implemented='DM')

#
# rotator
#
    dot=bcsc.addHWCSC(dot, 'Rotator', 'Rotator_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Rotator'], implemented=False)
#
# AO Closed Loop Controller
#
    dot=bcsc.addCSC(dot, 'AOCLC', ['XML repo: ?','Code repo: ?','ICD: ?','CSC generic cmds'], implemented=False)
#
# tcsWEP
#
    dot=bcsc.addCSC(dot, 'tcsWEP', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/develop/sal_interfaces/tcsWEP','Code repo: https://github.com/lsst-ts/ts_tcs_wep','ICD: https://ls.st/LSE-67','ICD: https://ls.st/LTS-163','CSC generic cmds'], implemented='IP')
    dot=bcsc.addSubHW(dot, 'DAQ', ['WEP_Server_HW'], ['DAQ'])
#
# tcsOFC
#
    dot=bcsc.addCSC(dot, 'tcsOFC',  ['XML repo: https://github.com/lsst-ts/ts_xml/tree/develop/sal_interfaces/tcsOfc','Code repo: https://github.com/lsst-ts/ts_tcs_ofc','ICD: https://ls.st/LTS-163','CSC generic cmds'], implemented='IP')
    
#
# headerService
#
    dot=bcsc.addCSC(dot, 'headerService', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atHeaderService','Code repo:  https://github.com/lsst-dm/HeaderService','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='DM')

#
# archiver
#
    dot=bcsc.addHWCSC(dot, 'archiver', 'archiver_HW', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], ['Archiver_CCS_Bridge','Data Processor'], implemented='DM')

#
# catchupArchiver
#
    dot=bcsc.addCSC(dot, 'catchupArchiver', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='DM')
#    dot=bcsc.addSubHW(dot, 'catchupArchiver', ['archiver_HW'], ['catchupArchiver'])
#
# CCS
#
    dot=bcsc.addSubHW(dot, 'DAQ', ['archiver_HW'], ['DAQ'])
    
#
# tcs
#
    dot=bcsc.addCSC(dot, 'TCS', ['XML repo: atcs', 'Code repo: https://github.com/lsst-ts/ts_atcs','ICD: https://ls.st/LSE-73?','ICD_differs_for_AT??','Language: LabView','CSC generic cmds', 'Target', 'Offset', 'SpectrographSetup'], implemented=False)
    
#
# PointingComponent
#
    dot=bcsc.addCSC(dot, 'PointingComponent', ['Vendor:Observatory_Sciences_Ltd','XML repo:?', 'Code repo: ?','ICD: https://ls.st/LTS-583?','Requirements, not ICD?','Language: ?','CSC generic cmds','trackTarget','startTracking','stopTracking','cmds from LTS-583?'], implemented='DM')
    
#
# camera
#
    dot=bcsc.addCSC(dot, 'camera', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atcamera','Code repo:  ?','ICD: https://ls.st/LSE-71','CSC generic cmds' ,'takeImages', 'initImage', 'discardRows',  'startImage','disableCalibration', 'initGuiders', 'enableCalibration','endImage','abort','clear'], implemented=True)

#
# CCS_OCS_Bridge
#
    dot=bcsc.addHWCSC(dot, 'CCS_OCS_Bridge', 'CCS', ['XML repo: ?','Code repo: ?','ICD: ?','cmds??'], ['CCS'], implemented=True)
    dot=bcsc.addSubHW(dot, 'DAQ', ['CCS'], ['DAQ'])

#
# OCS
#
    dot=bcsc.addCSC(dot, 'OCS', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/ocs', 'Code repo: https://github.com/lsst-ts/ts_ocs_executive','ICD: https://ls.st/LSE-71','Language: java','CSC generic cmds','sequence', 'script'], implemented='IP')

#
# scheduler
#
    dot=bcsc.addCSC(dot, 'scheduler', ['XML repo: ?', 'Code repo: https://github.com/lsst-ts/ts_scheduler','ICD: ?', 'CSC generic cmds'], implemented=True)
#
# EFD-Science Platform
#
    dot=bcsc.addCSC(dot, 'EFD_SciencePlatform', ['Vendor: DM', 'XML repo: ?', 'Code repo: ?','ICD: ?', 'Proposal: https://dmtn-082.lsst.io'], implemented='DM')

#
# legend
#
    dot=bcsc.addCSC(dot, 'LEGEND', ['Boxes with thin edges are CSCs','Boxes with thick edges are hardware', 'CSCs communicate only through SAL', 'A green title box means \"TS responsibility - significant functional capability\"', 'A yellow title box means \"TS responsibility - in progress\"', 'A red title box means \"TS responsibility - design phase\"', 'A purple title box means \"Vendor responsibility - significant functional capability\"', 'An orange entry is flagged as missing or questionable', 'A grey box is hardware', 'CSC generic commands are: abort, disable, enable, enterControl, exitControl, setValue, standby, start, stop'])

#
# connections
#
    dot=bcsc.connectCSCs(dot, 'TCS',  'AOCLC' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'IOTA' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'PointingComponent' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'hexapod' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'Dome' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'LaserTracker' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'Guider' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'm1m3' )
    dot=bcsc.connectCSCs(dot, 'TCS',  'm2ms' )
    dot=bcsc.connectCSCs(dot, 'tcsWEP',  'WEP_Server' )
    dot=bcsc.connectCSCs(dot, 'tcsOFC',  'hexapod' )
    dot=bcsc.connectCSCs(dot, 'tcsOFC',  'm1m3' )
    dot=bcsc.connectCSCs(dot, 'tcsOFC',  'm2ms' )
    dot=bcsc.connectCSCs(dot, 'IOTA', 'tcsWEP')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'TunableLaser')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'WhiteLightSource')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'PhotoDiodes')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'SEDSpectrograph')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'CalibrationScreen')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'CBP')
    dot=bcsc.connectCSCs(dot, 'AOCLC', 'tcsWEP')
    dot=bcsc.connectCSCs(dot, 'AOCLC', 'tcsOFC')
    dot=bcsc.connectCSCs(dot, 'PointingComponent', 'MTMount')
    dot=bcsc.connectCSCs(dot, 'PointingComponent', 'Rotator')
    dot=bcsc.connectCSCs(dot, 'TCS', 'm1m3')
    dot=bcsc.connectCSCs(dot, 'OCS', 'TCS')
    dot=bcsc.connectCSCs(dot, 'OCS', 'scheduler')
    dot=bcsc.connectCSCs(dot, 'OCS', 'headerService')
    dot=bcsc.connectCSCs(dot, 'OCS', 'archiver')
    dot=bcsc.connectCSCs(dot, 'OCS', 'catchupArchiver')
    dot=bcsc.connectCSCs(dot, 'OCS', 'camera')
    dot=bcsc.connectCSCs(dot, 'OCS',  'CalCS' )
    dot=bcsc.connectCSCs(dot, 'OCS',  'ECS' )
    dot=bcsc.connectCSCs(dot, 'OCS',  'EMCS' )
    dot=bcsc.connectCSCs(dot, 'OCS',  'LOVE' )
    dot=bcsc.connectCSCs(dot, 'OCS',  'EFD_SciencePlatform' )
    dot=bcsc.connectCSCs(dot, 'catchupArchiver', 'archiver_HW')
    dot=bcsc.connectCSCs(dot, 'camera', 'CCS_OCS_Bridge')
    dot=bcsc.connectCSCs(dot, 'IOTA', 'WEP_Server')

    dot=bcsc.connectCSCs(dot, 'LEGEND', 'OCS', 'penwidth=\"0\", arrowhead=\"none\"')
    dot=bcsc.connectCSCs(dot, 'LEGEND', 'TCS', 'penwidth=\"0\", arrowhead=\"none\"')

    dot=bcsc.finishDot(dot)
    f=open(outFileName,'w')
    f.writelines(dot)
    f.close()
