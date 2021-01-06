from setuptools import setup, find_packages

setup(
        name='kafka-grefneva',
        version='1.0',
        author='Kyrylo Shatskyy',
        author_email='kyrylo.shatskyy@gmail.com',
        description='Small example of kafka producer/consumer',
        url='https://github.com/kshtsk/kafka-grefneva',
        packages=find_packages(),
        classifiers=["Kafka"],
        python_requires='>=3.6',
        install_requires=[
            'kafka',
            'docopt',
            'requests',
            'psycopg2-binary',
            ],
        entry_points={
            'console_scripts': [
                'grecha = grecha:main', 
            ],
        }
)
