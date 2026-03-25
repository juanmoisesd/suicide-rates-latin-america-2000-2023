from setuptools import setup, find_packages
setup(
    name="suicide-rates-latin-america-2000-2023",
    version="1.0.0",
    description="Evolution of Suicide Rates in Latin America (2000-2023): Analysis by Country, Gender and Age Group. ",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/suicide-rates-latin-america-2000-2023",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)