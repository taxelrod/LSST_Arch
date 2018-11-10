import re

preamble = """
        digraph G { 
            //  
            // Defaults
            //  

            // Box for entities
            node [shape=none, margin=0]

            // One-to-many relation (from one, to many)
            edge [arrowhead=crow, arrowtail=none, dir=both]

           // title
           labelloc="t";
           label="%s";
           labelfontsize="24";
            //  
            // Entities
            //  
        """

postamble = """
        \n}
        """
def questionable(cmd):
 
    if re.search("\?", cmd):
        return True
    else:
        return False

def stripQuestion(cmd):
    return re.sub("\?", "", cmd, count=1)

def startDot(title):
    return preamble % title

def addHWCSC(dotString, CSCname, HWname, CmdList, HWList, implemented=True):

    if implemented==True:
        color = 'green'
    elif implemented=='Vendor':
        color = 'purple'
    elif implemented=='IP':
        color = 'yellow'
    else:
        color = 'salmon'
        
    CSCtable = """%s [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="%s">%s</td></tr>\n""" % (CSCname, color, CSCname)

    for cmd in CmdList:
        if questionable(cmd):
            CSCtable += '<tr><td align="left" bgcolor="orange">%s</td></tr>\n' % stripQuestion(cmd)
        else:
            CSCtable += '<tr><td align="left">%s</td></tr>\n' % cmd

    CSCtable += '        </table>>]\n'

    HWtable = """%s [label=<
        <table border="2" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="gray">%s</td></tr>\n""" % (HWname, HWname)

    for hw in HWList:
        HWtable += '<tr><td align="left">%s</td></tr>\n' % hw

    HWtable += '        </table>>]\n'

    connector = '%s->%s [penwidth="3"];\n' % (CSCname, HWname)
    
    return dotString + CSCtable + HWtable + connector

def addSubHW(dotString, HWname, ParentHWlist, HWList):
    HWtable = """%s [label=<
        <table border="2" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="gray">%s</td></tr>\n""" % (HWname, HWname)

    for hw in HWList:
        HWtable += '<tr><td align="left">%s</td></tr>\n' % hw

    HWtable += '        </table>>]\n'

    connector =''
    for parent in ParentHWlist:
        connector += '%s->%s [penwidth="3"];\n' % (parent, HWname)
    
    return dotString + HWtable + connector

def addCSC(dotString, CSCname,  CmdList, implemented=True):
    
    if implemented==True:
        color = 'green'
    elif implemented=='IP':
        color = 'yellow'
    elif implemented=='Vendor':
        color = 'purple'
    else:
        color = 'salmon'
        
    CSCtable = """%s [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="%s">%s</td></tr>\n""" % (CSCname, color, CSCname)

    for cmd in CmdList:
        if questionable(cmd):
            CSCtable += '<tr><td align="left" bgcolor="orange">%s</td></tr>\n' % stripQuestion(cmd)
        else:
            CSCtable += '<tr><td align="left">%s</td></tr>\n' % cmd

    CSCtable += '        </table>>]\n'

    return dotString + CSCtable


# Need to add some smarts here - make connector attributes dependent on whether the CSC has hardware or not
# No easy way to do this without instantiating CSC as a class

def connectCSCs(dotString, CSCname1, CSCname2, attrs=None):
    if attrs:
        relationshipString = '%s->%s [%s];\n' % (CSCname1, CSCname2, attrs)
    else:
        relationshipString = '%s->%s [arrowhead="vee"];\n' % (CSCname1, CSCname2)
    return dotString + relationshipString

def finishDot(dotString):
    return dotString+postamble
