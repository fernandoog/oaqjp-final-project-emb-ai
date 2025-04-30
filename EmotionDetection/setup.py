from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Fernando Ortega",
    description="A package for emotion detection using Watson NLP",
    url="https://github.com/fernandoog/oaqjp-final-project-emb-ai",
)