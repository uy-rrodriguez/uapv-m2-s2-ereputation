#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Main
"""

import sys, traceback
import ConfigParser, os


# ############################################################### #
#    Main                                                         #
#                                                                 #
# ############################################################### #

def load_config():
    config = ConfigParser.ConfigParser()
    config.readfp(open("configuration.cfg"))
    return config

def main():
    status = 0

    try:
        cfg = load_config()
        print cfg.get("BDD", "bdd.host")
        print cfg.get("BDD", "bdd.port")
        print cfg.get("BDD", "bdd.login")
        print cfg.get("BDD", "bdd.password")
        print cfg.get("BDD", "bdd.database")

    except (KeyboardInterrupt, SystemExit):
        pass

    except:
        traceback.print_exc()
        status = 1

    sys.exit(status)


if __name__ == "__main__":
    sys.exit(main())
