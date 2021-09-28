from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in application_management/__init__.py
from application_management import __version__ as version

setup(
	name="application_management",
	version=version,
	description="Application Management System",
	author="Prabhjot Kaur",
	author_email="misoff2019@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
