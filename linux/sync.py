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
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', help='Define the server directory')
parser.add_argument('-c', '--client', help='Define the client directory')
parser.add_argument('-f', '--force', action=store-true, default=false, help='Overwrite the file(s) in the destination dir if exists')
parser.add_argument('--extension', action=store-false, default=true, help="Check the extension of the files to compare them and verify if they are the same or not. If the flag are specified the script doesn't check the extension and operate the comparision only whit the actual file name. Use carefully")
args = parser.parse_args()

class Operator():

    def erase():
    #cancella i file non esistenti nella cartella dist

    def verify():
    # verifica presenza di file uguali nelle due cartelle


class Sync(Operator):

    def client_sync(server, client):
        check = bool(os.path.isdir(os.path.expanduser(server)) and os.path.isdir(os.path.expanduser(client)))
        if check:
            list_client = os.listdir(os.path.expanduser(client))
            for file in os.listdir(os.path.expanduser(server)):
                f = file
                if not f in list_client:
                    os.chdir(os.path.expanduser(server))
                    shutil.copy2(f, os.path.expanduser(client))
                    print('--> Copying ' + f)
            print('::Client sync complete without errors')

    def server_sync(server, client):
        check = bool(os.path.isdir(os.path.expanduser(server)) and os.path.isdir(os.path.expanduser(client)))
        if check:
            list_server = os.listdir(os.path.expanduser(server))
            for file in os.listdir(os.path.expanduser(client)):
                f = file
                if not f in list_server:
                    os.chdir(os.path.expanduser(client))
                    shutil.copy2(f, os.path.expanduser(server))
                    print('--> Copying ' + f)
            print('::Server sync complete without errors')

    def global_sync(dir1, dir2):
    # copia i file che mancano in una cartella nell'altra e viceversa
