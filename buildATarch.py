#!/usr/bin/env python

import sys
import buildCSCdot as bcsc

if __name__ == "__main__":

    outFileName = sys.argv[1]
    
    dot=bcsc.startDot('Auxiliary\ Telescope\ Architecture\ V5\ Oct\ 11,\ 2018')
#
# atspectrograph
#
    dot=bcsc.addHWCSC(dot, 'atSpectrograph', 'atSpectrograph_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/spectrograph', 'Code repo: https://github.com/lsst-ts/ts_Spectrograph','ICD: ?','CSC generic cmds','changeFilter','changeFilter','changeDisperser','moveLinearStage','setupSpectrograph'], ['Filter', 'Disperser', 'LinearStage', 'Readout Electronics System (ATSSRS)'], implemented='IP')
    
#
# atFiberSpectrometer
#
    dot=bcsc.addHWCSC(dot, 'atFiberSpectrometer', 'atFiberSpectrometer_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/sedSpectrometer', 'Code repo: https://github.com/lsst-ts/ts_sedspectrometer','ICD: ?','CSC generic cmds', 'captureSpectImage'], ['Avantes fiber spectrograph'], implemented=True)
    
#
# atMonochromator
#
    dot=bcsc.addHWCSC(dot, 'atMonochromator', 'atMonochrometor_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atMonochromator', 'Code repo: https://github.com/lsst-ts/ts_monochromator','ICD: ?','CSC generic cmds', 'ChangeWavelength', 'CalibrateWavelength', 'Power', 'SelectGrating', 'PowerWhiteLight', 'SetCoolingTemperature', 'ChangeLightIntensity', 'ChangeSlitWidth', 'updateMonochromatorSetup'], ['Monochromator', 'Shutter'], implemented=True)

#
# atWhiteLightSource
#
    dot=bcsc.addHWCSC(dot, 'atWhiteLightSource', 'atWhiteLightSource_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atWhiteLight','Code repo:  ?','ICD: ?','CSC generic cmds', 'powerLightOn', 'powerLightOff', 'setLightPower'], ['White LIght Source'], implemented=False)
    
#
# atWhiteLightChiller
#
    dot=bcsc.addHWCSC(dot, 'atWhiteLightChiller', 'atWhiteLightChiller_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/blob/feture/AuxTelCSCs/sal_interfaces/AtWhiteLightChiller','Code repo: https://github.com/lsst-ts/ss_atCooler','ICD: ?','CSC generic cmds', 'setTemperature', 'powerChillerOn', 'powerChillerOff'], ['White LIght Chiller'], implemented=False)
    
#
# atCalibration_Electrometer
#
    dot=bcsc.addHWCSC(dot, 'atCalibration_Electrometer', 'atCalibration_Electrometer_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/calibrationElectrometer','Code repo: https://github.com/lsst-ts/ts_electrometer','ICD: ?', 'CSC generic cmds', 'Power', 'StartScanReachIntensity', 'SetIntegrationTime', 'SetDigitalFilter', 'StartScanDt', 'SetMode', 'StartScan', 'PerformZeroCalib', 'SetRange', 'StopScan'], ['Electrometer'], implemented=True)
    
#
# atMCS
#
    dot=bcsc.addHWCSC(dot, 'atMCS', 'atMount_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtMCS', 'Code repo:  ?','ICD:  https://ls.st/LTS-159?',  'ICD_differs_for_AT??', 'CSC generic cmds' ,'startTracking', 'trackTarget', 'stopTracking', 'setInstrumentPort'], ['mount cRIO','Drive Electronics (vendor)', 'rotator cRIO','Electronics for two rotator drives(vendor)' , 'M3 cRIO'], implemented=False)
    
#
# atPneumatics
#
    dot=bcsc.addHWCSC(dot, 'atPneumatics', 'atPneumatics_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtPneumatics','Code repo:  ?','ICD: ?', 'CSC generic cmds','m1SetPressure', 'm1OpenAirValve', 'm1CloseAirValve', 'openM1CellVents', 'closeM1CellVents', 'openM1Cover', 'closeM1Cover', 'm2SetPressure', 'm2OpenAirValve', 'm2CloseAirValve', 'openInstrumentAirValve', 'closeInstrumentAirValve', 'closeMasterAirSupply', 'openMasterAirSupply'], ['M1 Pneumatics', 'M1 Cover', 'M1 Cell Vents', 'M2_pneumatics'], implemented=False)
    
#
# atM2_Hexapod
#
    hexCmds=['Move', 'MoveLUT', 'Pivot', 'Offset', 'Stop', 'PositionSet', 'ConfigureLimits', 'ConfigureVelocity', 'ConfigureAcceleration', 'ConfigureElevationRawLUT', 'ConfigureAzimuthRawLUT', 'ConfigureTemperatureRawLUT']
    dot=bcsc.addHWCSC(dot, 'atM2_Hexapod', 'atM2_Hexapod_HW', ['Vendor: Moog', 'XML repo: ?','Code repo: https://github.com/lsst-ts/ts_atm2hexapod','ICD: LTS-160', 'CSC generic cmds'] + hexCmds, ['M2 Hexapod', 'Camera Hexapod'], implemented='Vendor')    
#
# atDome
#
    dot=bcsc.addHWCSC(dot, 'atDome', 'atDome_HW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtDome','Code repo:  ?','ICD: https://ls.st/LTS-158?', 'ICD_differs_for_AT??','CSC generic cmds', 'stopMotionAllAxis', 'moveAzimuth', 'startTracking', 'stopTracking', 'moveShutterDropoutDoor','moveShutterMainDoor','closeShutter', 'openShutter', 'stopShutter'], ['dome cRIO', 'azimuth cRIO'], implemented=False)

#
# atBuilding
#
    dot=bcsc.addHWCSC(dot, 'atBuilding', 'atBuilding_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Vent gate motors', 'Vent gate fans', 'Lights', 'Anemometers', 'Thermocouples'], implemented=False)
    
#
# atHeaderService
#
    dot=bcsc.addCSC(dot, 'atHeaderService', ['Vendor: DM','XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atHeaderService','Code repo:  https://github.com/lsst-dm/HeaderService','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='Vendor')

#
# atArchiver
#
    dot=bcsc.addHWCSC(dot, 'atArchiver', 'atArchiver_HW', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], ['Archiver_CCS_Bridge','Data Processor'], implemented='Vendor')

#
# atCCS
#
    dot=bcsc.addSubHW(dot, 'atDAQ', ['atArchiver_HW'], ['atDAQ'])
    
#
# atTCS
#
    dot=bcsc.addCSC(dot, 'atTCS', ['XML repo: atcs', 'Code repo: https://github.com/lsst-ts/ts_atcs','ICD: https://ls.st/LSE-73?','ICD_differs_for_AT??','Language: LabView','CSC generic cmds', 'Target', 'Offset', 'SpectrographSetup'], implemented=False)
    
#
# atPointingComponent
#
    dot=bcsc.addCSC(dot, 'atPointingComponent', ['Vendor: Observatory_Sciences_Ltd','XML repo:?', 'Code repo: ?','ICD: https://ls.st/LTS-583?','Requirements, not ICD?','Language: ?','CSC generic cmds','trackTarget','startTracking','stopTracking','cmds from LTS-583?'], implemented='Vendor')
    
#
# atAOS
#
    dot=bcsc.addCSC(dot, 'atAOS', ['XML repo:?', 'Code repo: ?','ICD: ?','Language: ?','CSC generic cmds'], implemented=False)
    
#
# atCamera
#
    dot=bcsc.addCSC(dot, 'atCamera', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atcamera','Code repo:  ?','ICD: https://ls.st/LSE-71','CSC generic cmds' ,'takeImages', 'initImage', 'discardRows',  'startImage','disableCalibration', 'initGuiders', 'enableCalibration','endImage','abort','clear'], implemented=True)

#
# CCS_OCS_Bridge
#
    dot=bcsc.addHWCSC(dot, 'CCS_OCS_Bridge', 'atCCS', ['XML repo: ?','Code repo: ?','ICD: ?','cmds??'], ['atCCS'], implemented=True)

#
# OCS
#
    dot=bcsc.addCSC(dot, 'OCS', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/ocs', 'Code repo: https://github.com/lsst-ts/ts_ocs_executive','ICD: https://ls.st/LSE-71','ICD: ?','Language: java','CSC generic cmds','sequence', 'script'], implemented='IP')

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
    dot=bcsc.connectCSCs(dot, 'atTCS',  'atSpectrograph' )
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atFiberSpectrometer')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atMonochromator')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atWhiteLightSource')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atWhiteLightChiller')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atCalibration_Electrometer')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atPointingComponent')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atMCS')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atAOS')
    dot=bcsc.connectCSCs(dot, 'atAOS', 'atM2_Hexapod')
    dot=bcsc.connectCSCs(dot, 'atAOS', 'atPneumatics')
    dot=bcsc.connectCSCs(dot, 'atPointingComponent', 'atMCS')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atPneumatics')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atM2_Hexapod')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atDome')
    dot=bcsc.connectCSCs(dot, 'atTCS', 'atBuilding')
    dot=bcsc.connectCSCs(dot, 'OCS', 'atTCS')
    dot=bcsc.connectCSCs(dot, 'OCS', 'atScheduler')
    dot=bcsc.connectCSCs(dot, 'OCS', 'atHeaderService')
    dot=bcsc.connectCSCs(dot, 'OCS', 'atArchiver')
    dot=bcsc.connectCSCs(dot, 'OCS', 'atCamera')
    dot=bcsc.connectCSCs(dot, 'atCamera', 'CCS_OCS_Bridge')

    dot=bcsc.connectCSCs(dot, 'LEGEND', 'OCS', 'penwidth=\"0\", arrowhead=\"none\"')
    dot=bcsc.connectCSCs(dot, 'LEGEND', 'atTCS', 'penwidth=\"0\", arrowhead=\"none\"')

    dot=bcsc.finishDot(dot)
    f=open(outFileName,'w')
    f.writelines(dot)
    f.close()
