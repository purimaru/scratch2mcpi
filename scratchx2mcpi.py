#!/usr/bin/env python3

import sys, traceback
import os
import gettext
import mcpi.minecraft as minecraft
import requests
from http.server import HTTPServer  # Changed for Python 3
from http.server import BaseHTTPRequestHandler  # Changed for Python 3
import urllib.parse  # Changed for Python 3
from urllib.parse import urlparse  # Changed for Python 3
import logging

VERSION = "0.0.1"
localedir = os.path.join(os.path.dirname(__file__), 'locale')
_ = gettext.translation(domain = 'scratch2mcpi', localedir = localedir, fallback = True).gettext # Changed for Python 3

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class ScratchX2MCPIServer(BaseHTTPRequestHandler):
    def reset(self, params):
        mc.postToChat('reset the world')
        mc.setBlocks(-100, 0, -100, 100, 63, 100, 0, 0)
        mc.setBlocks(-100, -63, -100, 100, -2, 100, 1, 0)
        mc.setBlocks(-100, -1, -100, 100, -1, 100, 2, 0)
        mc.player.setPos(0, 0, 0)
        return ''

    def postToChat(self, params):
        mc.postToChat(urllib.parse.unquote(params[0])) # Changed for Python 3
        return ''

    def setPos(self, params):
        mc.player.setPos(int(params[0]), int(params[1]), int(params[2]))
        return ''

    def setBlock(self, params):
        mc.setBlock(int(params[0]), int(params[1]), int(params[2]), int(params[3]), int(params[4]))
        return ''

    def setBlocks(self, params):
        mc.setBlocks(int(params[0]), int(params[1]), int(params[2]), int(params[3]), int(params[4]), int(params[5]), int(params[6]), int(params[7]))
        return ''

    def returnExtension(self, params):
        file = open("scratchx2mcpi.js", "r")
        content = file.read()
        file.close()
        return content

    def do_GET(self):
        global mc
        commands = {
            "reset" : self.reset,
            "post_to_chat" : self.postToChat,
            "set_pos" : self.setPos,
            "set_block" : self.setBlock,
            "set_blocks" : self.setBlocks,
            "scratchx2mcpi.js" : self.returnExtension
        }
        parsed_path = urlparse(self.path) # Changed for Python 3 (imported directly)
        query = parsed_path.query
        self.send_response(200)
        self.end_headers()
        command_path = parsed_path[2].split('/')
        handler = commands[command_path[1]]
        result = handler(command_path[2:])
        self.wfile.write(result)
        # Need to encode the result string to bytes for wfile.write in Python 3
        self.wfile.write(result.encode('utf-8'))
        return

if __name__ == '__main__':
    print("=================") # Changed for Python 3
    print("SratchX2MCPI %s" % VERSION) # Changed for Python 3
    print("=================") # Changed for Python 3
    print("") # Changed for Python 3

    try:
        mc = minecraft.Minecraft.create()
    except Exception as e: # Changed for Python 3
        log.exception(f'Unable to connect to Minecraft Pi: {e}') # Changed for Python 3
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    server = HTTPServer(('localhost', 8080), ScratchX2MCPIServer)
    log.info('Starting ScratchX2MCPIServer, use <Ctrl-C> to stop.')
    server.serve_forever()
