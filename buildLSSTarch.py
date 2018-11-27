#!/usr/bin/env python

import sys
import buildCSCdot as bcsc

if __name__ == "__main__":

    outFileName = sys.argv[1]
    
    dot=bcsc.startDot('Main\ Telescope\ Architecture\ V3.0\ Nov\ 25,\ 2018')

#
# MTMount
#
    MCS_cmds = ['moveToTarget','trackTarget', 'enableCamWrap', 'disableCamWrap', 'openMirrorCover', 'closeMirrorCover', 'stopMount', 'clearerror']
    dot=bcsc.addHWCSC(dot, 'MTMount', 'MCS_HW', ['Vendor: Tekniker', 'XML repo: https://github.com/lsst-ts/ts_xml/tree/feture/AuxTelCSCs/sal_interfaces/AtMCS', 'Code repo:  ?','ICD:  https://ls.st/LTS-159?', 'CSC generic cmds'] + MCS_cmds, ['MCS'], implemented='Vendor')
    
#
# Hexapod
#
    hexCmds=['Move', 'MoveLUT', 'Pivot', 'Offset', 'Stop', 'PositionSet', 'ConfigureLimits', 'ConfigureVelocity', 'ConfigureAcceleration', 'ConfigureElevationRawLUT', 'ConfigureAzimuthRawLUT', 'ConfigureTemperatureRawLUT']
    dot=bcsc.addHWCSC(dot, 'Hexapod', 'Hexapod_HW', ['Vendor: Moog', 'XML repo: ?','Code repo: https://github.com/lsst-ts/ts_atm2hexapod','ICD: LTS-160', 'CSC generic cmds'] + hexCmds, ['M2 Hexapod', 'Camera Hexapod'], implemented='Vendor')
    
#
# Dome
#
    dot=bcsc.addCSC(dot, 'Dome', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds', 'Crawl', 'Move','Park','SetLouvers','CloseShutter','OpenShutter','StopShutter'],  implemented='Vendor')
#
    dot=bcsc.addHWCSC(dot, 'DomeLWS', 'Dome_RotatingHW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'], ['Dome Rotating Part cRIO'], implemented='Vendor')
#
    dot=bcsc.addHWCSC(dot, 'DomeADB', 'Dome_FixedHW', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'], ['Dome Fixed Part cRIO'], implemented='Vendor')
#
    dot=bcsc.addCSC(dot, 'DomeTHCS', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'],  implemented='Vendor')
#
    dot=bcsc.addCSC(dot, 'DomeMONCS', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'],  implemented='Vendor')
#
    dot=bcsc.addCSC(dot, 'DomeAPS', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'],  implemented='Vendor')
#
    dot=bcsc.addCSC(dot, 'DomeLouvers', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/master/sal_interfaces/Dome','Code repo:  ?','ICD: https://ls.st/LTS-158', 'Vendor: EIE', 'CSC generic cmds'],  implemented='Vendor')
#
    dot=bcsc.addCSC(dot, 'DomeTrajectory', ['XML repo: ?','Code repo:  ?','ICD: ?', 'CSC generic cmds'],  implemented=False)
#
# MTM1M3
#
    dot=bcsc.addHWCSC(dot, 'MTM1M3', 'MTM1M3_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['MTM1M3 cRIO', 'Thermocouples', 'Accelerometers'], implemented=True)
#
# IOTA
# - note connects to tcsWEP
#
    dot=bcsc.addHWCSC(dot, 'IOTA', 'IOTA_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['High Speed CMOS Camera', 'SHWFS' ], implemented=False)

#
# laser tracker
#
#
    dot=bcsc.addHWCSC(dot, 'LaserTracker', 'LaserTracker_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['LaserTracker'], implemented=False)
#
# guider
#
    dot=bcsc.addCSC(dot, 'Guider', ['XML repo: ?','Code repo: ?','ICD: ?','CSC generic cmds'], implemented=False)
    dot=bcsc.addSubHW(dot, 'DAQ', ['Guider'], ['DAQ_HW', 'TCS_Network', 'OCS_Network', 'CCS_Network'])

#
# CalCS
#
    dot=bcsc.addCSC(dot, 'CalCS', ['XML repo: ?','Code repo:  ?','ICD: LSE-139','CSC generic cmds'],implemented=False)

    dot=bcsc.addHWCSC(dot, 'TunableLaser', 'TunableLaser_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['TunableLaser#1','TunableLaser#2'], implemented=False)

    dot=bcsc.addHWCSC(dot, 'WhiteLightSource', 'WhiteLightSource_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['WhiteLightSource'], implemented=False)
    
    dot=bcsc.addHWCSC(dot, 'Electrometer', 'PhotoDiodes_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['PhotoDiodes'], implemented=True)
    
    dot=bcsc.addHWCSC(dot, 'SEDSpectrograph', 'SEDSpectrograph_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['SEDSpectrograph'], implemented=False)

    dot=bcsc.addHWCSC(dot, 'CBP', 'CBP_HW', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Collimated Beam Projector'], implemented=False)
    

#
# MTM2
#
    m2Cmds = ['ApplyForces', 'PositionMirror']
    dot=bcsc.addHWCSC(dot, 'MTM2', 'm2_HW', ['Vendor: Harris','XML repo: ?','Code repo:  ?','ICD: LTS-162, CR-0130','CSC generic cmds'] + m2Cmds, ['m2_controller', 'm2_cRio'], implemented='Vendor')
#
# EEC (Environment Control System)
#
    dot=bcsc.addHWCSC(dot, 'EEC', 'CVAC', ['XML repo: ?','Code repo:  ?','ICD: ?','CSC generic cmds'], ['Chillers','AirHandlineUnits','CVACSensors','Fans','Valves'], implemented=False)

#
# EMCS (environmental monitor control system)
#
    dot=bcsc.addHWCSC(dot, 'EMCS', 'environmental_monitoring_HW', ['XML repo: ?','Code repo:  ?','ICD: LSE-139','CSC generic cmds'], ['Seismic_Monitors','Anemometers','Visible_All-Sky Camera','Infrared_All-Sky Camera','Weather_Station','GPS_Water_Vapor_Monitor'], implemented=False)

    dot=bcsc.addHWCSC(dot, 'DIMM', 'DIMM_HW', ['XML repo: ?','Code repo:  ?','ICD: LSE-139','CSC generic cmds'], ['DIMM_(Astelco)'], implemented=False)


#
# Rotator
#
    RotatorCmds=['Move', 'MoveConstantVelocty', 'Track', 'Stop', 'TrackStart', 'PositionSet', 'VelocitySet']
    dot=bcsc.addHWCSC(dot, 'Rotator', 'Rotator_HW', ['Vendor: Moog','XML repo: ?','Code repo:  ?','ICD: LTS-160','CSC generic cmds'] + RotatorCmds, ['Rotator'], implemented='Vendor')
#
# AO Closed Loop Controller
#
    dot=bcsc.addCSC(dot, 'AOCLC', ['XML repo: ?','Code repo: ?','ICD: ?','CSC generic cmds'], implemented=False)
#
# MTWEP
#
    dot=bcsc.addCSC(dot, 'MTWEP', ['XML repo: https://github.com/lsst-ts/ts_xml/tree/develop/sal_interfaces/MTWEP','Code repo: https://github.com/lsst-ts/ts_tcs_wep','ICD: https://ls.st/LSE-67','ICD: https://ls.st/LTS-163','CSC generic cmds'], implemented='IP')
#
# MTOFC
#
    dot=bcsc.addCSC(dot, 'MTOFC',  ['XML repo: https://github.com/lsst-ts/ts_xml/tree/develop/sal_interfaces/tcsOfc','Code repo: https://github.com/lsst-ts/ts_tcs_ofc','ICD: https://ls.st/LTS-163','CSC generic cmds'], implemented='IP')
    
#
# MTHeaderService
#
    dot=bcsc.addCSC(dot, 'MTHeaderService', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atHeaderService','Code repo:  https://github.com/lsst-dm/HeaderService','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='Vendor')

#
# MTArchiver
#
    dot=bcsc.addHWCSC(dot, 'MTArchiver', 'MTArchiver_HW', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], ['MTArchiver_CCS_Bridge','Data Processor'], implemented='Vendor')

#
# CatchupArchiver
#
    dot=bcsc.addCSC(dot, 'CatchupArchiver', ['Vendor: DM', 'XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atArchiver', 'Code repo: https://github.com/lsst/ctrl_iip','ICD: https://ls.st/LSE-72','CSC generic cmds'], implemented='Vendor')
#
# Script_DrivenBatch
#
    dot=bcsc.addHWCSC(dot, 'ScriptDrivenBatch', 'DataBackbone', ['Vendor: DM', 'XML repo: ?', 'Code repo: ?','ICD: https://ls.st/LDM-230','CSC generic cmds'], ['DM_Data_Backbone'], implemented='Vendor')

#
# EFD_TransformationService
#
    dot=bcsc.addCSC(dot, 'EFD_TransformationService', ['Vendor: DM', 'XML repo: ?', 'Code repo: ?','ICD: https://ls.st/LDM-230','CSC generic cmds'], implemented='Vendor')

#
# CCS
#
    dot=bcsc.addSubHW(dot, 'DataBackbone', ['MTArchiver_HW'], ['DataBackbone'])
    
#
# MTTCS
#
    dot=bcsc.addCSC(dot, 'MTTCS', ['XML repo: atcs', 'Code repo: https://github.com/lsst-ts/ts_atcs','ICD: https://ls.st/LSE-73?','ICD_differs_for_AT??','Language: LabView','CSC generic cmds', 'Target', 'stopMotion', 'filterChangeRequest', 'wfpCalculate', 'wfpSimulate'], implemented=False)
    
#
# MTPointingComponent
#
    dot=bcsc.addCSC(dot, 'MTPointingComponent', ['Vendor:Observatory_Sciences_Ltd','XML repo:?', 'Code repo: ?','ICD: https://ls.st/LTS-583?','Requirements, not ICD?','Language: ?','CSC generic cmds','trackTarget','startTracking','stopTracking','cmds from LTS-583?'], implemented='Vendor')
    
#
# MTCamera
#
    dot=bcsc.addCSC(dot, 'MTCamera', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/atcamera','Code repo:  ?','ICD: https://ls.st/LSE-71','CSC generic cmds' ,'takeImages', 'initImage', 'discardRows',  'startImage','disableCalibration', 'initGuiders', 'enableCalibration','endImage','abort','clear'], implemented=True)

#
# CCS_OCS_Bridge
#
    dot=bcsc.addHWCSC(dot, 'CCS_OCS_Bridge', 'CCS', ['XML repo: ?','Code repo: ?','ICD: ?','cmds??'], ['CCS'], implemented=True)

#
# ScriptQueue
#
    dot=bcsc.addCSC(dot, 'ScriptQueue', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/ScriptQueue', 'Code repo: https://github.com/lsst-ts/ts_scriptqueue','ICD: ?','Language: python','CSC generic cmds','showAvailableScripts', 'showQueue', 'pause', 'resume', 'add', 'move', 'requeue', 'stopScripts'], implemented=True)

#
# Script
#
    dot=bcsc.addCSC(dot, 'Script', ['XML repo: https://github.com/lsst-ts/ts_xml/sal_interfaces/Script', 'Code repo: varies','ICD: ?','Language: python','CSC generic cmds', 'configure', 'run', 'resume', 'setLogging', 'setCheckpoints', 'stop'], implemented=True)

#
# Watcher
#
    dot=bcsc.addCSC(dot, 'Watcher', ['XML repo: ?', 'Code repo: ?','ICD: ?','Language: python','CSC generic cmds'], implemented=False)

#
# Scheduler
#
    dot=bcsc.addCSC(dot, 'Scheduler', ['XML repo: ?', 'Code repo: https://github.com/lsst-ts/ts_scheduler','ICD: ?', 'CSC generic cmds'], implemented=True)
#
# legend
#
    dot=bcsc.addCSC(dot, 'LEGEND', ['Boxes with thin edges are CSCs','Boxes with thick edges are hardware', 'CSCs communicate only through SAL', 'A green title box means \"TS responsibility - significant functional capability\"', 'A yellow title box means \"TS responsibility - in progress\"', 'A red title box means \"TS responsibility - design phase\"', 'A purple title box means \"Vendor responsibility - significant functional capability\"', 'An orange entry is flagged as missing or questionable', 'A grey box is hardware', 'CSC generic commands are: abort, disable, enable, enterControl, exitControl, setValue, standby, start, stop'])

#
# connections
#
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'AOCLC' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'IOTA' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'MTPointingComponent' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'Hexapod' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'Dome' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'LaserTracker' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'Guider' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'MTM1M3' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'DomeTrajectory' )
    dot=bcsc.connectCSCs(dot, 'MTTCS',  'Watcher' )
    dot=bcsc.connectCSCs(dot, 'DomeTrajectory', 'Dome' )
    dot=bcsc.connectCSCs(dot, 'MTOFC',  'Hexapod' )
    dot=bcsc.connectCSCs(dot, 'MTOFC',  'MTM1M3' )
    dot=bcsc.connectCSCs(dot, 'MTOFC',  'MTM2' )
    dot=bcsc.connectCSCs(dot, 'CalCS', 'TunableLaser')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'WhiteLightSource')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'Electrometer')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'SEDSpectrograph')
    dot=bcsc.connectCSCs(dot, 'CalCS', 'CBP')
    dot=bcsc.connectCSCs(dot, 'AOCLC', 'MTWEP')
    dot=bcsc.connectCSCs(dot, 'AOCLC', 'MTOFC')
    dot=bcsc.connectCSCs(dot, 'MTPointingComponent', 'MTMount')
    dot=bcsc.connectCSCs(dot, 'MTPointingComponent', 'Rotator')
    dot=bcsc.connectCSCs(dot, 'ScriptQueue', 'Scheduler')
    dot=bcsc.connectCSCs(dot, 'ScriptQueue', 'ScriptDrivenBatch')
    dot=bcsc.connectCSCs(dot, 'ScriptQueue', 'Script')
    dot=bcsc.connectCSCs(dot, 'Script', 'MTTCS')
    dot=bcsc.connectCSCs(dot, 'Script', 'MTHeaderService')
    dot=bcsc.connectCSCs(dot, 'Script', 'MTArchiver')
    dot=bcsc.connectCSCs(dot, 'Script', 'CatchupArchiver')
    dot=bcsc.connectCSCs(dot, 'Script', 'MTCamera')
    dot=bcsc.connectCSCs(dot, 'Script',  'CalCS' )
    dot=bcsc.connectCSCs(dot, 'Script',  'EEC' )
    dot=bcsc.connectCSCs(dot, 'Script',  'EMCS' )
    dot=bcsc.connectCSCs(dot, 'Script',  'OCS_DrivenBatch' )
    dot=bcsc.connectCSCs(dot, 'Script',  'EFD_TransformationService' )
    dot=bcsc.connectCSCs(dot, 'EFD_TransformationService', 'DataBackbone', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'CatchupArchiver', 'MTArchiver_HW', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'MTCamera', 'CCS_OCS_Bridge')
    dot=bcsc.connectCSCs(dot, 'MTWEP', 'DAQ', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'MTWEP', 'IOTA_HW', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'MTArchiver_HW', 'DAQ', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'CCS', 'DAQ', attrs='penwidth="3"')

    dot=bcsc.connectCSCs(dot, 'EMCS', 'DIMM')

    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeADB')
    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeMONCS')
    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeAPS')
    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeLWS')
    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeTHCS')
    dot=bcsc.connectCSCs(dot, 'Dome', 'DomeLouvers')
    dot=bcsc.connectCSCs(dot, 'DomeAPS', 'Dome_RotatingHW', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'DomeMONCS', 'Dome_RotatingHW', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'DomeLouvers', 'Dome_RotatingHW', attrs='penwidth="3"')
    dot=bcsc.connectCSCs(dot, 'DomeTHCS', 'Dome_FixedHW', attrs='penwidth="3"')

    dot=bcsc.connectCSCs(dot, 'LEGEND', 'ScriptQueue', attrs='penwidth=\"0\", arrowhead=\"none\"')
    dot=bcsc.connectCSCs(dot, 'LEGEND', 'MTTCS', attrs='penwidth=\"0\", arrowhead=\"none\"')

    dot=bcsc.finishDot(dot)
    f=open(outFileName,'w')
    f.writelines(dot)
    f.close()
