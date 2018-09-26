#!/bin/csh
./buildATarch.py AT.dot; dot -Tpdf -o AT.pdf AT.dot
./buildLSSTarch.py LSST.dot; dot -Tpdf -o LSST.pdf LSST.dot

