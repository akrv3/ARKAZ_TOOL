from setuptools import setup, find_packages

setup(
    name="ARKAZ_MULTIE_TOOL",  
    version="0.1",
    description="Un projet utilisant diverses bibliothèques Python",
    author="AKR",  
    packages=find_packages(),  
    install_requires=[
        'requests',  
        'discord.py', 
        'phonenumbers',  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='> 3.10.0', 
)
