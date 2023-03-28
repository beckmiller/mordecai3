from setuptools import setup, find_packages
setup(
    name = 'mordecai3',
    version='3.0.0a',
    url='http://github.com/ahalterman/mordecai3/',
    author='Andy Halterman',
    author_email='ahalterman0@gmail.com',
    license='MIT',
    packages=['mordecai3'],
    keywords = ['geoparsing', 'nlp', 'geocoding', 'toponym resolution'],
    package_dir = {
        "mordecai3": "mordecai3"
    },
    install_requires = ['typer>=0.3.2,<1.0',
            'spacy-transformers>=1.0.1,<2.0',
            'transformers>=4.2.2,<5.0',
            'spacy>=3.5,<4.0',
            'torch>=1.2.0,<2.0',
            'elasticsearch>=7.11.0,<8.0',
            'elasticsearch-dsl>=7.3.0,<8.0',
            'scikit-learn>=0.24.1',
            'pandas>=1.2.2,<2.0',
            'jellyfish>=0.8.2,<2.0',
            'tqdm>=4.56.1,<5.0',
            'numpy>=1.19.5,<2.0',
            'jsonlines>=3.0.0,<4.0',
            'xmltodict>=0.12.0,<1.0'],
   dependency_links=['https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.5.0/en_core_web_trf-3.5.0.tar.gz'],
   include_package_data=True,
   package_data = {'assets': ['admin1CodesASCII.json',
                             'country_bert_768.npy',
                             'countryInfo.txt',
                             'feature_code_dict.json',
                             'hierarchy.txt',
                             'mordecai_2023-03-28.pt',
                             'wikipedia-iso-country-codes.txt']}
)



#from setuptools import setup
#
#setup(name='mordecai',
#      version='2.1.0',
#      description='Full text geoparsing and event geocoding',
#      url='http://github.com/openeventdata/mordecai/',
#      author='Andy Halterman',
#      author_email='ahalterman0@gmail.com',
#      license='MIT',
#      packages=['mordecai'],
#      keywords = ['geoparsing', 'nlp', 'geocoding', 'toponym resolution'],
#      install_requires = ['editdistance>=0.5.3',
#                          'elasticsearch==5.4.0',
#                          'elasticsearch-dsl==5.3.0',
#                          'h5py>=2.10.0',
#                          'pandas>=0.24.2',
#                          'spacy>=2.3,<3.0',
#                          'tensorflow>=2.2.0',
#                          'tqdm>=4.28.1',
#                          'numpy>=1.12'],
#      dependency_links=['https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.3.1/en_core_web_lg-2.3.1.tar.gz'],
#      include_package_data=True,
#      package_data = {'data': ['admin1CodesASCII.json',
#                             'countries.json',
#                             'nat_df.csv',
#                             'stopword_country_names.json'],
#                    'models' : ['country_model.h5',
#                                'rank_model.h5']}
#     )
