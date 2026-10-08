"""henriquefy: Henrique Bastos's practices, applied to your code."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("henriquefy")
except PackageNotFoundError:  # running from a checkout without an install
    __version__ = "0.0.0.dev0"
