"""Utility helpers used across scripts."""
import os
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
