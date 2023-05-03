from setuptools import setup
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name="nb-serverproxy-gradio",
    packages= ['nb_serverproxy_gradio'],
    version='0.0.5',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/fdsf53451001/nb_serverproxy_gradio",
    author="Toby",
    description="Jupyter server proxy wrapper for Gradio",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    entry_points={
        'jupyter_serverproxy_servers': [
            'graio = nb_serverproxy_gradio:setup_gradio',
        ]
    },
    package_data={
        'nb_serverproxy_gradio': ['icons/*'],
    },
)
