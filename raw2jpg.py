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

#import std module(s)
import os, sys
import subprocess
import shutil
import argparse
import time
import fnmatch

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--indir', help='Define the input directory')
parser.add_argument('-o', '--outdir', default='~/foto/convertite', help='Create the output directory')
parser.add_argument('-e', '--extension', default='.CR2', help='Define raw extension')
args = parser.parse_args()

_indir = args.indir
_extension = args.extension
_now = time.strftime('%d-%m-%Y')
_outdir = os.path.join(args.outdir, _now)

def raw2jpg(indir, outdir, extension):

    try:
        os.makedirs(os.path.expanduser(outdir))
    except:
        pass

    try:
        os.chdir(os.path.expanduser(indir))
    except:
        raise FileExistsError("The specified directory doesn't exists")
        sys.exit(1)

    i = 1
    for line in os.listdir(os.path.expanduser(indir)):
        p = line
        e = '*' + extension
        l = len(fnmatch.filter(os.listdir(os.path.expanduser(indir)), e))
        if p.endswith(extension):
            _p = p[:-3] + 'jpg'
            _i = str(i)
            _l = str(l)
            print('(' + _i + '/' + _l + ') --> ' + 'Converting ' + p)
            subprocess.check_call(['convert', p, _p])
        i += 1
    print('\n::Convertion process completed without errors')

    for line in os.listdir(os.path.expanduser(indir)):
        n = line
        if n.endswith('.jpg'):
            shutil.move(n, os.path.expanduser(outdir))
    print('\n::File(s) copied to ' + outdir)

if __name__ == '__main__':
    raw2jpg(_indir, _outdir, _extension)
