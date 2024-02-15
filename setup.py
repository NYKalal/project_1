from setuptools import find_packages,setup

setup(
    name='mcq_genrator',
    version='0.0.1',
    author='Nagaraj Y',
    author_email='nyk6426@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)