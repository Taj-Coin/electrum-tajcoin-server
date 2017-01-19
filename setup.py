from setuptools import setup

setup(
    name="electrum-nevacoin-server",
    version="1.0",
    scripts=['run_electrum_nevacoin_server.py','electrum-nevacoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumnevacoinserver':'src'
        },
    py_modules=[
        'electrumnevacoinserver.__init__',
        'electrumnevacoinserver.utils',
        'electrumnevacoinserver.storage',
        'electrumnevacoinserver.deserialize',
        'electrumnevacoinserver.networks',
        'electrumnevacoinserver.blockchain_processor',
        'electrumnevacoinserver.server_processor',
        'electrumnevacoinserver.processor',
        'electrumnevacoinserver.version',
        'electrumnevacoinserver.ircthread',
        'electrumnevacoinserver.stratum_tcp',
        'electrumnevacoinserver.stratum_http'
    ],
    description="nevacoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="nevacoin",
    maintainer_email="support@nevacoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/nevacoin/electrum-nevacoin-server/",
    long_description="""Server for the Electrum Lightweight nevacoin Wallet"""
)


