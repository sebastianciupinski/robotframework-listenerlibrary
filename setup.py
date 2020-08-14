import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='robotframework-listenerlibrary',  
     version='1.0.post1',
     author="Sebastian Ciupinski",
     author_email="sebastian.ciupinski+robotframework-listenerlibrary@gmail.com",
     description="Robot Framework Listener Library",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sebastianciupinski/robotframework-listenerlibrary",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )