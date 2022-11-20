# ----------------------------------------------------------------------
# SSLCAUDIT - a tool for automating security audit of SSL clients
# Released under terms of GPLv3, see COPYING.TXT
# Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
# ----------------------------------------------------------------------

import logging
from sslcaudit.core.BaseClientAuditController import BaseClientAuditController, HOST_ADDR_ANY
from sslcaudit.core.ConnectionAuditEvent import ConnectionAuditResult

logger = logging.getLogger('SSLCAuditCLI')

DEFAULT_HOST = HOST_ADDR_ANY
DEFAULT_PORT = 8443
DEFAULT_MODULES = 'sslcert'
DEFAULT_LISTEN_ON = '%s:%d' % (DEFAULT_HOST, DEFAULT_PORT)
OUTPUT_FIELD_SEPARATOR = ' '


class SSLCAuditCLI(object):
    def __init__(self, options, file_bag):
        self.options = options
        self.controller = BaseClientAuditController(self.options, file_bag, event_handler=self.event_handler)

    def run(self):
        # print config info to the console before running the controller
        logger.info('filebag location: %s' % str(self.controller.file_bag.base_dir))

        self.controller.start()

        # wait for the controller thread to finish, handle Ctrl-C if any
        interrupted_by_user = False
        while self.controller.isAlive():
            try:
                self.controller.join(1)
            except KeyboardInterrupt:
                logger.info('Got KeyboardInterrupt exception, aborting the program ...')
                self.controller.stop() # graceful death
                interrupted_by_user = True

        # if the program is aborted by the user, return exitcode 1
        if interrupted_by_user:
            return 1
        else:
            return 0

    def stop(self):
        self.controller.stop()

    def event_handler(self, res):
        if isinstance(res, ConnectionAuditResult):
            # dump:
            # * client address and port,
            # * server profile
            # * result
            # all in one line, in fixed width columns
            fields = []
            client_address = '%s:%d' % (res.conn.client_address)
            fields.append('%-16s' % client_address)
            fields.append('%-80s' % (res.profile))
            fields.append(str(res.result))
            print(OUTPUT_FIELD_SEPARATOR.join(fields))
