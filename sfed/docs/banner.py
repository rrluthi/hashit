from cement.utils.version import get_version_banner
from sfed.core.version import get_version
from colorama import Fore as f

INTRO_BANNER = f"""{f.RED}
{f.RED}|=====================================================================|
{f.RED}|{f.YELLOW}           /\__\         /\__\         /\__\         _____          {f.RED} |
{f.RED}|{f.YELLOW}          /:/ _/_       /:/ _/_       /:/ _/_       /::\  \         {f.RED} |
{f.RED}|{f.YELLOW}         /:/ /\  \     /:/ /\__\     /:/ /\__\     /:/\:\  \        {f.RED} |
{f.RED}|{f.YELLOW}        /:/ /::\  \   /:/ /:/  /    /:/ /:/ _/_   /:/  \:\__\       {f.RED} |
{f.RED}|{f.YELLOW}       /:/_/:/\:\__\ /:/_/:/  /    /:/_/:/ /\__\ /:/__/ \:|__|      {f.RED} |
{f.RED}|{f.YELLOW}       \:\/:/ /:/  / \:\/:/  /     \:\/:/ /:/  / \:\  \ /:/  /      {f.RED} |
{f.RED}|{f.YELLOW}        \::/ /:/  /   \::/__/       \::/_/:/  /   \:\  /:/  /       {f.RED} |
{f.RED}|{f.YELLOW}         \/_/:/  /     \:\  \        \:\/:/  /     \:\/:/  /        {f.RED} |
{f.RED}|{f.YELLOW}           /:/  /       \:\__\        \::/  /       \::/  /         {f.RED} |
{f.RED}|{f.YELLOW}           \/__/         \/__/         \/__/         \/__/          {f.RED} |
|=====================================================================|
|     STRING & FILE ENCODER/DECODER/HASHER/UNIQUE STRING GENERATOR    |
|=====================================================================|
| Licence: Mit                                                        |
| Commands: hash, enc, dec, file, help, exit                          |
| Language: {f.CYAN}Python3.12                                        |
| Version: {get_version()} {get_version_banner()}                     |
|=====================================================================|
"""

VERSION_BANNER = f"""
SFED Version: {get_version()} {get_version_banner()}
"""
