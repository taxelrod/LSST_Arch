#!/usr/bin/env python

import sys
import buildCSCdot as bcsc

if __name__ == "__main__":

    outFileName = sys.argv[1]
    
    dot=bcsc.startDot('Auxiliary\ Telescope\ Architecture\ V6.0\ Dec\ 4,\ 2018')
#
# ATSpectrograph
#
    dot=bcsc.addHWCSC(dot, 'ATSpectrograph', 'ATSpectrograph_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/spectrograph', 'Code repo: https://github.com/lsst-ts/ts_Spectrograph','ICD: ?','CSC generic cmds','changeFilter','changeFilter','changeDisperser','moveLinearStage','setupSpectrograph'], ['Filter', 'Disperser', 'LinearStage', 'Readout Electronics System (ATSSRS)'], implemented='IP')
    
#
# atFiberSpectrometer
#
    dot=bcsc.addHWCSC(dot, 'atFiberSpectrometer', 'atFiberSpectrometer_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/sedSpectrometer', 'Code repo: https://github.com/lsst-ts/ts_sedspectrometer','ICD: ?','CSC generic cmds', 'captureSpectImage'], ['Avantes fiber spectrograph'], implemented=True)
    
#
# ATMonochromator
#
    dot=bcsc.addHWCSC(dot, 'ATMonochromator', 'ATMonochrometor_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atMonochromator', 'Code repo: https://github.com/lsst-ts/ts_monochromator','ICD: ?','CSC generic cmds', 'ChangeWavelength', 'CalibrateWavelength', 'Power', 'SelectGrating', 'PowerWhiteLight', 'SetCoolingTemperature', 'ChangeLightIntensity', 'ChangeSlitWidth', 'updateMonochromatorSetup'], ['Monochromator', 'Shutter'], implemented=True)

#
# ATWhiteLight
#
    dot=bcsc.addHWCSC(dot, 'ATWhiteLightSource', 'ATWhiteLight_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atWhiteLight','Code repo:  ?','ICD: ?','CSC generic cmds', 'powerLightOn', 'powerLightOff', 'setLightPower'], ['White LIght Source'], implemented='IP')
    
#
# ATWhiteLightChiller
#
    dot=bcsc.addHWCSC(dot, 'ATWhiteLightChiller', 'ATWhiteLightChiller_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/blob/feture/AuxTelCSCs/sal_interfaces/ATWhiteLightChiller','Code repo: https://github.com/lsst-ts/ss_atCooler','ICD: ?','CSC generic cmds', 'setTemperature', 'powerChillerOn', 'powerChillerOff'], ['White LIght Chiller'], implemented='IP')
    
#
# Electrometer
#
    dot=bcsc.addHWCSC(dot, 'Electrometer', 'Electrometer_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/calibrationElectrometer','Code repo: https://github.com/lsst-ts/ts_electrometer','ICD: ?', 'CSC generic cmds', 'Power', 'StartScanReachIntensity', 'SetIntegrationTime', 'SetDigitalFilter', 'StartScanDt', 'SetMode', 'StartScan', 'PerformZeroCalib', 'SetRange', 'StopScan'], ['Electrometer'], implemented=True)
    
#
# ATMCS
#
    dot=bcsc.addHWCSC(dot, 'ATMCS', 'atMount_HW', ['Vendor: ?', 'XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtMCS', 'Code repo:  ?','ICD:  https://ls.st/LTS-159?',  'ICD_differs_for_AT??', 'CSC generic cmds' ,'startTracking', 'trackTarget', 'stopTracking', 'setInstrumentPort'], ['mount cRIO','Drive Electronics (vendor)', 'rotator cRIO','Electronics for two rotator drives(vendor)' , 'M3 cRIO'], implemented='Vendor')
    
#
# ATPneumatics
#
    dot=bcsc.addHWCSC(dot, 'ATPneumatics', 'ATPneumatics_HW', ['Vendor: ?','XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtPneumatics','Code repo:  ?','ICD: ?', 'CSC generic cmds','m1SetPressure', 'm1OpenAirValve', 'm1CloseAirValve', 'openM1CellVents', 'closeM1CellVents', 'openM1Cover', 'closeM1Cover', 'm2SetPressure', 'm2OpenAirValve', 'm2CloseAirValve', 'openInstrumentAirValve', 'closeInstrumentAirValve', 'closeMasterAirSupply', 'openMasterAirSupply'], ['M1 Pneumatics', 'M1 Cover', 'M1 Cell Vents', 'M2_pneumatics'], implemented='Vendor')
    
#
# Hexapod
#
    hexCmds=['Move', 'MoveLUT', 'Pivot', 'Offset', 'Stop', 'PositionSet', 'ConfigureLimits', 'ConfigureVelocity', 'ConfigureAcceleration', 'ConfigureElevationRawLUT', 'ConfigureAzimuthRawLUT', 'ConfigureTemperatureRawLUT']
    dot=bcsc.addHWCSC(dot, 'ATHexapod', 'atM2_Hexapod_HW', ['Vendor: Moog', 'XML repo: ?','Code repo: https://github.com/lsst-ts/ts_atm2hexapod','ICD: LTS-160', 'CSC generic cmds'] + hexCmds, ['M2 Hexapod', 'Camera Hexapod'], implemented='IP')    

#
# ATDome
#
    dot=bcsc.addHWCSC(dot, 'ATDome', 'ATDome_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtDome','Code repo:  ?','ICD: https://ls.st/LTS-158?', 'ICD_differs_for_AT??','CSC generic cmds', 'stopMotionAllAxis', 'moveAzimuth', 'startTracking', 'stopTracking', 'moveShutterDropoutDoor','moveShutterMainDoor','closeShutter', 'openShutter', 'stopShutter'], ['dome cRIO', 'azimuth cRIO'], implemented='IP')

#
# atBuilding
#
    dot=bcsc.addHWCSC(dot, 'atBuilding', 'atBuilding_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Vent gate motors', 'Vent gate fans', 'Lights', 'Anemometers', 'Thermocouples'], implemented=False)
    
#
# ATHeaderService
#
    dot=bcsc.addCSC(dot, 'ATHeaderService', ['Vendor: DM','XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/ATHeaderService','Code repo:  https://github.com/lsst-dm/HeaderService','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='Vendor')

#
# ATArchiver
#
    dot=bcsc.addHWCSC(dot, 'ATArchiver', 'ATArchiver_HW', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], ['Archiver_CCS_Bridge','Data Processor'], implemented='Vendor')

#
# atCCS
#
    dot=bcsc.addSubHW(dot, 'atDAQ', ['ATArchiver_HW'], ['atDAQ'])
    
#
# ATTCS
#
    dot=bcsc.addCSC(dot, 'ATTCS', ['XML repo: atcs', 'Code repo: https://github.com/lsst-ts/ts_atcs','ICD: https://ls.st/LSE-73?','ICD_differs_for_AT??','Language: LabView','CSC generic cmds', 'Target', 'Offset', 'SpectrographSetup'], implemented=False)
    
#
# ATPointingComponent
#
    dot=bcsc.addCSC(dot, 'ATPointingComponent', ['Vendor: Observatory_Sciences_Ltd','XML repo:?', 'Code repo: ?','ICD: https://ls.st/LTS-583?','Requirements, not ICD?','Language: ?','CSC generic cmds','trackTarget','startTracking','stopTracking','cmds from LTS-583?'], implemented='Vendor')
    
#
# atAOS
#
    dot=bcsc.addCSC(dot, 'atAOS', ['XML repo:?', 'Code repo: ?','ICD: ?','Language: ?','CSC generic cmds'], implemented='IP')
    
#
# ATCamera
#
    dot=bcsc.addCSC(dot, 'ATCamera', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atcamera','Code repo:  ?','ICD: https://ls.st/LSE-71','CSC generic cmds' ,'takeImages', 'initImage', 'discardRows',  'startImage','disableCalibration', 'initGuiders', 'enableCalibration','endImage','abort','clear'], implemented=True)

#
# CCS_OCS_Bridge
#
    dot=bcsc.addHWCSC(dot, 'CCS_OCS_Bridge', 'atCCS', ['XML repo: ?','Code repo: ?','ICD: ?','cmds??'], ['atCCS'], implemented=True)

#
# ScriptQueue
#
    dot=bcsc.addCSC(dot, 'ScriptQueue', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/ScriptQueue', 'Code repo: https://github.com/lsst-ts/ts_scriptqueue','ICD: ?','Language: python','CSC generic cmds','showAvailableScripts', 'showQueue', 'pause', 'resume', 'add', 'move', 'requeue', 'stopScripts'], implemented=True)

#
# Script
#
    dot=bcsc.addCSC(dot, 'Script', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/Script', 'Code repo: varies','ICD: ?','Language: python','CSC generic cmds', 'configure', 'run', 'resume', 'setLogging', 'setCheckpoints', 'stop'], implemented=True)

#
# atScheduler
#
    dot=bcsc.addCSC(dot, 'atScheduler', ['XML repo: ?', 'Code repo: https://github.com/lsst-ts/ts_scheduler','ICD: ?', 'CSC generic cmds'], implemented=True)

#
# legend
#
    dot=bcsc.addCSC(dot, 'LEGEND', ['Boxes with thin edges are CSCs','Boxes with thick edges are hardware', 'CSCs communicate only through SAL', 'A green title box means \"TS responsibility - significant functional capability\"', 'A yellow title box means \"TS responsibility - in progress\"', 'A red title box means \"TS responsibility - design phase\"', 'A purple title box means \"Vendor responsibility\"', 'An orange entry is flagged as missing or questionable', 'A grey box is hardware', 'CSC generic commands are: abort, disable, enable, enterControl, exitControl, setValue, standby, start, stop'])

#
# connections
#
    dot=bcsc.connectCSCs(dot, 'ATTCS',  'ATSpectrograph' )
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'atFiberSpectrometer')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATMonochromator')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATWhiteLightSource')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATWhiteLightChiller')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'Electrometer')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATPointingComponent')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATMCS')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'atAOS')
    dot=bcsc.connectCSCs(dot, 'atAOS', 'ATHexapod')
    dot=bcsc.connectCSCs(dot, 'atAOS', 'ATPneumatics')
    dot=bcsc.connectCSCs(dot, 'ATPointingComponent', 'ATMCS')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATPneumatics')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'Hexapod')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'ATDome')
    dot=bcsc.connectCSCs(dot, 'ATTCS', 'atBuilding')
    dot=bcsc.connectCSCs(dot, 'ScriptQueue', 'atScheduler')
    dot=bcsc.connectCSCs(dot, 'ScriptQueue', 'Script')
    dot=bcsc.connectCSCs(dot, 'Script', 'ATTCS')
    dot=bcsc.connectCSCs(dot, 'Script', 'ATHeaderService')
    dot=bcsc.connectCSCs(dot, 'Script', 'ATArchiver')
    dot=bcsc.connectCSCs(dot, 'Script', 'ATCamera')
    dot=bcsc.connectCSCs(dot, 'ATCamera', 'CCS_OCS_Bridge')

    dot=bcsc.connectCSCs(dot, 'LEGEND', 'ScriptQueue', 'penwidth=\"0\", arrowhead=\"none\"')
    dot=bcsc.connectCSCs(dot, 'LEGEND', 'ATTCS', 'penwidth=\"0\", arrowhead=\"none\"')

    dot=bcsc.finishDot(dot)
    f=open(outFileName,'w')
    f.writelines(dot)
    f.close()
