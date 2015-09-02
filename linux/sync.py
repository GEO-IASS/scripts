#!/usr/bin/env python

#   Copyright (C) 2015 by Andrea Calzavacca <paranoid.nemo@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

#Import std module(s)
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', help='Define the server directory')
parser.add_argument('-c', '--client', help='Define the client directory')
parser.add_argument('-f', '--force', action=store-true, default=false, help='Overwrite the file(s) in the destination dir if exists')
parser.add_argument('-e', '--extension', action=store-false, default=true, help="Check the extension of the files to compare them and verify if there are the same or not. If the flag are specified the script doesn't check the extension and could operate the comparision only whit the actual file name. Use carefully")
args = parser.parse_args()

class Operator():

    def erase():
    #cancella i file non esistenti nella cartella dist

    def verify():
    # verifica presenza di file nelle due cartelle


class Sync(Operator):

    def client_sync(dir1, dir2):
    # verificare esistenza di dir 1 e 2
    # verificare quali file esistono già in dir 2
    # copiare i file che esistono solo in dir1 in dir2

    def server_sync(dir1, dir2):
    # stesso dell'altro ma al contrario

    def global_sync(dir1, dir2):
    # copia i file che mancano in una cartella nell'altra e viceversa
