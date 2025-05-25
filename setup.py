import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='keshore kumar',
    author_email='kishore007026@gmail.com',
    url='https://github.com/Kishore00706/speech-to-sign-convertor.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)