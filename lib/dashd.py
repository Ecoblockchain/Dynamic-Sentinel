#!/usr/bin/env python

"""
darkSilkd interface
----

"""

import os
import config
import subprocess
import json
import sys

def rpc_command(params):
    darksilkcmd = config.darksilkd_path + " --datadir=" + config.datadir
    
    #print "'%s' '%s'" % (darksilkcmd, params)

    proc = subprocess.Popen(darksilkcmd + " " + params, shell=True, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    while (True):
        # Read line from stdout, break if EOF reached, append line to output
        line = proc.stdout.readline()
        line = line.decode()
        if (line == ""): break
        output += line

    return output

class CTransaction():
    tx = {}

    def __init__(self):
        tx = {
            "bcconfirmations" : 0
        }
        return None

    def load(self, txid):
        result = rpc_command("gettransaction " + txid)

        try:
            obj = json.loads(result)
            if obj:
                self.tx = obj
                return True
            else: 
                print "error loading tx"
                return False
        except:
            print "Unexpected error:", sys.exc_info()[0]
            print 
            print "darksilkd result:", result
            print
            return False

    def get_hash(self):
        return None

    def get_confirmations(self):
        return self.tx["bcconfirmations"]
