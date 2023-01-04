import setuptools

setuptools.setup(
	name='omletarcade',
	version='1.0',
	author='thekip007',
	author_email='kirillpoddubnyj390@gmail.com',
	description='using omAPI',
	packages=['omletarcade'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=["socketio", "colorama", "requests"]
)