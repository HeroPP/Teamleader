from distutils.core import setup

setup(
    name="teamleader",
    packages=["teamleader"],
    version="1.1.2",
    license="MIT",
    description="A layer on top of the Teamleader v2 API",
    author="Jaap",
    author_email="jaap1@me.com",
    url="https://github.com/HeroPP/Teamleader",
    download_url="https://github.com/HeroPP/Teamleader/archive/refs/tags/v1.1.0.tar.gz",
    keywords=["Teamleader", "API", "CRM"],
    install_requires=[
        "certifi",
        "charset-normalizer",
        "idna",
        "oauthlib",
        "pickle5",
        "ratelimit",
        "requests",
        "requests-oauthlib",
        "urllib3",
    ],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
    ],
)
